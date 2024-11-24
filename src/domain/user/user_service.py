from typing import List, Optional
import cv2
import json
import os
import numpy as np
from datetime import datetime
from .user import User
from infrastructure.recognition.opencv_detector import OpenCVFaceDetector
from infrastructure.recognition.opencv_recognizer import OpenCVFaceRecognizer

class UserService:
    def __init__(self):
        self.data_file = "data/users.json"
        self.photos_dir = "data/user_photos"
        self.face_detector = OpenCVFaceDetector()
        self.face_recognizer = OpenCVFaceRecognizer()
        
        self._ensure_directories()
        self._load_data()
    
    def _ensure_directories(self):
        os.makedirs(self.photos_dir, exist_ok=True)
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
    
    def _load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.users = json.load(f)
        else:
            self.users = {}
    
    def _save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.users, f)
    
    def create_user(self, name: str, photos: List[np.ndarray]) -> Optional[User]:
        if name in self.users:
            return None
            
        user = User(name=name, photos=photos)
        
        # Salva as fotos
        for i, photo in enumerate(photos):
            photo_path = os.path.join(self.photos_dir, f"{name}_{i+1}.jpg")
            cv2.imwrite(photo_path, photo)
        
        # Treina o reconhecedor
        self.face_recognizer.train(photos, name)
        
        # Salva os dados do usuário
        self.users[name] = {
            'created_at': user.created_at.isoformat(),
            'photo_paths': [f"{name}_{i+1}.jpg" for i in range(len(photos))]
        }
        self._save_data()
        
        return user
    
    def get_user(self, name: str) -> Optional[User]:
        if name not in self.users:
            return None
            
        user_data = self.users[name]
        photos = []
        for photo_path in user_data['photo_paths']:
            full_path = os.path.join(self.photos_dir, photo_path)
            if os.path.exists(full_path):
                photos.append(cv2.imread(full_path))
        
        return User(
            name=name,
            photos=photos,
            created_at=datetime.fromisoformat(user_data['created_at'])
        )