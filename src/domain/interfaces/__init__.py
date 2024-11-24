"""
Interfaces do sistema de reconhecimento facial
"""
from .face_detector import FaceDetector
from .face_recognizer import FaceRecognizer

__all__ = ['FaceDetector', 'FaceRecognizer']