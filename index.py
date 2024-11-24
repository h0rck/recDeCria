import cv2
import face_recognition
import numpy as np
from datetime import datetime
import os

class SistemaReconhecimentoFacial:
    def __init__(self, diretorio_fotos_conhecidas):
        self.rostos_conhecidos = []
        self.nomes_conhecidos = []
        self.carregar_rostos_conhecidos(diretorio_fotos_conhecidas)

    def carregar_rostos_conhecidos(self, diretorio):
        """Carrega as imagens de referência do diretório especificado"""
        for arquivo in os.listdir(diretorio):
            if arquivo.endswith((".jpg", ".jpeg", ".png")):
                imagem = face_recognition.load_image_file(os.path.join(diretorio, arquivo))
                encoding = face_recognition.face_encodings(imagem)[0]
                self.rostos_conhecidos.append(encoding)
                self.nomes_conhecidos.append(os.path.splitext(arquivo)[0])

    def processar_frame(self, frame):
        """Processa cada frame do vídeo para reconhecimento facial"""
        # Redimensiona o frame para processamento mais rápido
        frame_pequeno = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        
        # Converte BGR (OpenCV) para RGB (face_recognition)
        rgb_frame = frame_pequeno[:, :, ::-1]
        
        # Localiza faces no frame
        localizacoes_faces = face_recognition.face_locations(rgb_frame)
        encodings_faces = face_recognition.face_encodings(rgb_frame, localizacoes_faces)

        nomes = []
        for encoding_face in encodings_faces:
            # Compara com rostos conhecidos
            matches = face_recognition.compare_faces(self.rostos_conhecidos, encoding_face)
            nome = "Desconhecido"

            if True in matches:
                primeiro_match_index = matches.index(True)
                nome = self.nomes_conhecidos[primeiro_match_index]

            nomes.append(nome)

        # Desenha os resultados
        for (top, right, bottom, left), nome in zip(localizacoes_faces, nomes):
            # Escala de volta ao tamanho original
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Desenha um retângulo ao redor do rosto
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Desenha o nome abaixo do rosto
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, nome, (left + 6, bottom - 6), 
                        cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)

        return frame

    def iniciar_camera(self, camera_id=0):
        """Inicia a captura de vídeo da câmera especificada"""
        video_capture = cv2.VideoCapture(camera_id)
        
        try:
            while True:
                ret, frame = video_capture.read()
                if not ret:
                    break

                frame_processado = self.processar_frame(frame)
                
                cv2.imshow('Video', frame_processado)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            video_capture.release()
            cv2.destroyAllWindows()

# Exemplo de uso
if __name__ == "__main__":
    sistema = SistemaReconhecimentoFacial("diretorio_fotos_conhecidas")
    sistema.iniciar_camera()