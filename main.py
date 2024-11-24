from src.infrastructure.recognition.opencv_detector import OpenCVFaceDetector
from src.infrastructure.recognition.opencv_recognizer import OpenCVFaceRecognizer
from src.presentation.cli.main_menu import MainMenu
from src.presentation.camera.camera_manager import CameraManager

def main():
    detector = OpenCVFaceDetector()
    recognizer = OpenCVFaceRecognizer()
    camera = CameraManager()
    
    menu = MainMenu(detector, recognizer, camera)
    menu.run()

if __name__ == "__main__":
    main()