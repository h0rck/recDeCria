import cv2
import numpy as np
from typing import List, Tuple
from ...domain.interfaces.face_detector import FaceDetector

class OpenCVFaceDetector(FaceDetector):
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
    
    def detect_faces(self, image: np.ndarray) -> List[Tuple[int, int, int, int]]:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        return [tuple(face) for face in faces]

# src/infrastructure/recognition/opencv_recognizer.py
import cv2
import numpy as np
from typing import Tuple, Optional, List
from ...domain.interfaces.face_recognizer import FaceRecognizer

class OpenCVFaceRecognizer(FaceRecognizer):
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.trained = False
    
    def train(self, face_images: List[np.ndarray], user_id: str) -> None:
        gray_images = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
                      if len(img.shape) == 3 else img 
                      for img in face_images]
        
        if not self.trained:
            self.recognizer.train(gray_images, np.array([hash(user_id)]))
            self.trained = True
        else:
            self.recognizer.update(gray_images, np.array([hash(user_id)]))
    
    def predict(self, face_image: np.ndarray) -> Tuple[Optional[str], float]:
        if not self.trained:
            return None, 0.0
            
        gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY) \
               if len(face_image.shape) == 3 else face_image
               
        try:
            label, confidence = self.recognizer.predict(gray)
            return str(label), confidence
        except:
            return None, 0.0