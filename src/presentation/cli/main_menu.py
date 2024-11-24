import cv2
from domain.interfaces.face_detector import FaceDetector
from domain.interfaces.face_recognizer import FaceRecognizer
from domain.interfaces.event_storage import EventStorage
from ..camera.camera_manager import CameraManager

class MainMenu:
    def __init__(
        self,
        face_detector: FaceDetector,
        face_recognizer: FaceRecognizer,
        camera: CameraManager,
        event_storage: EventStorage
    ):
        self.face_detector = face_detector
        self.face_recognizer = face_recognizer
        self.camera = camera
        self.event_storage = event_storage
    
    def cadastrar_pessoa(self):
        nome = input("Digite o nome da pessoa: ")
        print("Pressione 'c' para capturar ou 'q' para sair")
        
        fotos = []
        while len(fotos) < 30:
            frame = self.camera.capture_frame()
            if frame is None:
                continue
            
            faces = self.face_detector.detect_faces(frame)
            
            frame_com_faces = frame.copy()
            for (x, y, w, h) in faces:
                cv2.rectangle(frame_com_faces, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            cv2.putText(frame_com_faces, f'Fotos: {len(fotos)}/30', (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.imshow('Cadastro', frame_com_faces)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('c') and len(faces) == 1:
                x, y, w, h = faces[0]
                face_img = frame[y:y+h, x:x+w]
                fotos.append(face_img)
                print(f"Foto {len(fotos)} capturada!")
        
        cv2.destroyAllWindows()
        
        if len(fotos) == 30:
            self.face_recognizer.train(fotos, nome)
            print(f"Cadastro de {nome} realizado com sucesso!")
        else:
            print("Cadastro cancelado!")
    
    def iniciar_reconhecimento(self):
        print("Iniciando reconhecimento... Pressione 'q' para sair")
        
        while True:
            frame = self.camera.capture_frame()
            if frame is None:
                continue
            
            faces = self.face_detector.detect_faces(frame)
            
            for (x, y, w, h) in faces:
                face_img = frame[y:y+h, x:x+w]
                
                nome, confianca = self.face_recognizer.predict(face_img)
                cor = (0, 255, 0) if nome else (0, 0, 255)
                texto = nome if nome else "Desconhecido"
                
                cv2.rectangle(frame, (x, y), (x+w, y+h), cor, 2)
                cv2.putText(frame, texto, (x, y-10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.9, cor, 2)
            
            cv2.imshow('Reconhecimento', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cv2.destroyAllWindows()
    
    def run(self):
        while True:
            print("\nSistema de Reconhecimento Facial")
            print("1 - Cadastrar nova pessoa")
            print("2 - Iniciar reconhecimento")
            print("3 - Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.cadastrar_pessoa()
            elif opcao == '2':
                self.iniciar_reconhecimento()
            elif opcao == '3':
                break
            else:
                print("Opção inválida!")