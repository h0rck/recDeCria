import cv2
import cv2
import json
import os
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
        # Carrega os dados salvos
        if os.path.exists('data/users.json'):
            with open('data/users.json', 'r') as f:
                usuarios_salvos = json.load(f)
                
            # Carrega as fotos e treina o reconhecedor para cada usuário
            for nome, dados in usuarios_salvos.items():
                fotos = []
                for foto_path in dados['photo_paths']:
                    caminho_completo = os.path.join('data/user_photos', foto_path)
                    if os.path.exists(caminho_completo):
                        foto = cv2.imread(caminho_completo)
                        if foto is not None:
                            fotos.append(foto)
                
                if fotos:
                    self.face_recognizer.train(fotos, nome)
                    print(f"Usuário {nome} carregado com sucesso!")
        
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
                
                if nome and confianca < 100:  # Ajuste esse threshold conforme necessário
                    texto = f"{nome} ({confianca:.1f}%)"
                else:
                    texto = "Desconhecido"
                    cor = (0, 0, 255)
                
                cv2.rectangle(frame, (x, y), (x+w, y+h), cor, 2)
                cv2.putText(frame, texto, (x, y-10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.9, cor, 2)
            
            # Mostra o número de usuários cadastrados
            if 'usuarios_salvos' in locals():
                n_usuarios = len(usuarios_salvos)
                cv2.putText(frame, f"Usuarios cadastrados: {n_usuarios}", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
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