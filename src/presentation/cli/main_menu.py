import cv2
from domain.interfaces.face_detector import FaceDetector
from domain.interfaces.face_recognizer import FaceRecognizer
from domain.interfaces.event_storage import EventStorage
from presentation.camera.camera_manager import CameraManager
from presentation.cli.user_cli import UserCLI

class MainMenu:
    def __init__(
        self,
        face_detector: FaceDetector,
        face_recognizer: FaceRecognizer,
        camera: CameraManager,
        event_storage: EventStorage,
        user_cli = UserCLI()
    ):
        self.face_detector = face_detector
        self.face_recognizer = face_recognizer
        self.camera = camera
        self.event_storage = event_storage
        self.user_cli = user_cli
    
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
    
    # funcao que tras os eventos salvos no sqlite
    def listar_eventos(self):
        print("Listando eventos...")
        eventos = self.event_storage.get_latest_events()
        print("Eventos:")
        print(eventos)
        # for evento in eventos:
        #     print(f"{evento}")


    def run(self):
        while True:
            print("\nSistema de Reconhecimento Facial")
            print("1 - Cadastrar nova pessoa")
            print("2 - Iniciar reconhecimento")
            print("3 - Listar eventos")
            print("4 - Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.user_cli.register_user()
            elif opcao == '2':
                self.iniciar_reconhecimento()
            elif opcao == '3':
                self.listar_eventos()
            elif opcao == '4':
                break
            else:
                print("Opção inválida!")