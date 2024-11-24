import cv2
from domain.user.user_service import UserService
from presentation.camera.camera_manager import CameraManager

class UserCLI:
    def __init__(self):
        self.user_service = UserService()
        self.cameraManager = CameraManager()
    
    def register_user(self):
        while True:
            name = input("Digite o nome do usuário: ").strip()
            if not name:
                print("Nome não pode estar vazio!")
                continue
                
            if name in self.user_service.users:
                print(f"Já existe um usuário cadastrado com o nome '{name}'!")
                continue_input = input("Deseja tentar com outro nome? (s/n): ")
                if continue_input.lower() != 's':
                    return
                continue
            break
        
        print("Pressione 'c' para capturar ou 'q' para sair")
        photos = []
        
        while len(photos) < 30:
            frame = self.cameraManager.capture_frame()
            if frame is None:
                continue
            
            faces = self.user_service.face_detector.detect_faces(frame)
            
            frame_with_faces = frame.copy()
            for (x, y, w, h) in faces:
                cv2.rectangle(frame_with_faces, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            cv2.putText(frame_with_faces, f'Fotos: {len(photos)}/30', (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.imshow('Cadastro', frame_with_faces)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('c') and len(faces) == 1:
                x, y, w, h = faces[0]
                face_img = frame[y:y+h, x:x+w]
                photos.append(face_img)
                print(f"Foto {len(photos)} capturada!")
        
        cv2.destroyAllWindows()
        
        if len(photos) == 30:
            user = self.user_service.create_user(name, photos)
            if user:
                print(f"Cadastro de {name} realizado com sucesso!")
            else:
                print("Erro ao cadastrar usuário!")
        else:
            print("Cadastro cancelado!")