"""
Módulo de reconhecimento facial usando OpenCV
"""
from .opencv_detector import OpenCVFaceDetector
from .opencv_recognizer import OpenCVFaceRecognizer

__all__ = ['OpenCVFaceDetector', 'OpenCVFaceRecognizer']