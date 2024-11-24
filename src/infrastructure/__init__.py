"""
Implementações concretas dos componentes do sistema.
"""
from .recognition.opencv_detector import OpenCVFaceDetector
from .recognition.opencv_recognizer import OpenCVFaceRecognizer

__all__ = ['OpenCVFaceDetector', 'OpenCVFaceRecognizer']