import cv2
import numpy as np
from typing import List, Tuple, Optional
from ...domain.interfaces.face_recognizer import FaceRecognizer

class OpenCVFaceRecognizer(FaceRecognizer):
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.trained = False
        self.user_ids = {}
        self.next_id = 0
    
    def train(self, face_images: List[np.ndarray], user_id: str) -> None:
        if user_id not in self.user_ids.values():
            self.user_ids[self.next_id] = user_id
            numeric_id = self.next_id
            self.next_id += 1
        else:
            numeric_id = list(self.user_ids.keys())[
                list(self.user_ids.values()).index(user_id)
            ]
        
        gray_images = []
        labels = []
        
        for img in face_images:
            if len(img.shape) == 3:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            else:
                gray = img
            gray_images.append(gray)
            labels.append(numeric_id)
        
        if not self.trained:
            self.recognizer.train(gray_images, np.array(labels))
            self.trained = True
        else:
            self.recognizer.update(gray_images, np.array(labels))
    
    def predict(self, face_image: np.ndarray) -> Tuple[Optional[str], float]:
        if not self.trained:
            return None, 0.0
        
        try:
            if len(face_image.shape) == 3:
                face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
            
            numeric_id, confidence = self.recognizer.predict(face_image)
            user_id = self.user_ids.get(numeric_id)
            
            return user_id, confidence
        except Exception as e:
            print(f"Erro na predição: {e}")
            return None, 0.0