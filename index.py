import cv2
import mediapipe as mp
import numpy as np
import os

class ReconhecimentoFacialMVP:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils
        self.face_detection = self.mp_face_detection.FaceDetection(
            model_selection=1, min_detection_confidence=0.5
        )
        
    def iniciar_reconhecimento(self):
        """
        Inicia o reconhecimento facial pela webcam
        """
        print("Iniciando webcam...")
        video_capture = cv2.VideoCapture(0)
        
        if not video_capture.isOpened():
            print("Erro ao acessar a webcam!")
            return
            
        print("Reconhecimento iniciado! Pressione 'q' para sair...")
        
        while video_capture.isOpened():
            success, image = video_capture.read()
            if not success:
                break
                
            # Converte a imagem para RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            # Detecta as faces
            results = self.face_detection.process(image)
            
            # Desenha as detecções
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            if results.detections:
                for detection in results.detections:
                    # Desenha o retângulo ao redor da face
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, _ = image.shape
                    bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                           int(bboxC.width * iw), int(bboxC.height * ih)
                    cv2.rectangle(image, bbox, (0, 255, 0), 2)
                    
                    # Adiciona um rótulo "Pessoa Detectada"
                    cv2.rectangle(image, 
                                (bbox[0], bbox[1] - 20), 
                                (bbox[0] + 120, bbox[1]), 
                                (0, 255, 0), 
                                -1)
                    cv2.putText(image, 
                              "Pessoa Detectada", 
                              (bbox[0], bbox[1] - 5),
                              cv2.FONT_HERSHEY_SIMPLEX, 
                              0.5, 
                              (255, 255, 255), 
                              2)
            
            # Mostra o resultado
            cv2.imshow('Detecção Facial', image)
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
                
        video_capture.release()
        cv2.destroyAllWindows()

# Exemplo de uso
if __name__ == "__main__":
    sistema = ReconhecimentoFacialMVP()
    sistema.iniciar_reconhecimento()