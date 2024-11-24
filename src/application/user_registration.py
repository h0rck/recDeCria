# src/application/user_registration.py
from datetime import datetime
import uuid
from ..domain.entities.user import User
from ..domain.interfaces.face_detector import FaceDetector
from ..domain.interfaces.face_recognizer import FaceRecognizer
from ..domain.interfaces.user_repository import UserRepository
from ..domain.interfaces.image_repository import ImageRepository

class UserRegistrationService:
    def __init__(
        self,
        face_detector: FaceDetector,
        face_recognizer: FaceRecognizer,
        user_repository: UserRepository,
        image_repository: ImageRepository
    ):
        self.face_detector = face_detector
        self.face_recognizer = face_recognizer
        self.user_repository = user_repository
        self.image_repository = image_repository
    
    def register_user(self, name: str, face_images: List[np.ndarray]) -> User:
        # Gera ID único
        user_id = str(uuid.uuid4())
        
        # Verifica e processa as imagens faciais
        processed_images = []
        for image in face_images:
            faces = self.face_detector.detect_faces(image)
            if len(faces) != 1:
                continue
            x, y, w, h = faces[0]
            face_image = image[y:y+h, x:x+w]
            processed_images.append(face_image)
        
        if not processed_images:
            raise ValueError("Nenhuma face válida detectada nas imagens")
        
        # Treina o reconhecedor
        self.face_recognizer.train(processed_images, user_id)
        
        # Salva as imagens
        image_ids = [
            self.image_repository.save_image(user_id, img)
            for img in processed_images
        ]
        
        # Cria e salva o usuário
        user = User(
            id=user_id,
            name=name,
            created_at=datetime.now(),
            face_data=image_ids[0]  # Usa primeira imagem como referência
        )
        
        self.user_repository.save(user)
        return user