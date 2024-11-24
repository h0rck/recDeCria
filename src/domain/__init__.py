"""
Definições de interfaces e entidades do domínio.
"""
from .interfaces.face_detector import FaceDetector
from .interfaces.face_recognizer import FaceRecognizer
from .entities.user import User

__all__ = ['FaceDetector', 'FaceRecognizer', 'User']