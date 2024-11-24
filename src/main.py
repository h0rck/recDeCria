import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from infrastructure.recognition.opencv_detector import OpenCVFaceDetector
from infrastructure.recognition.opencv_recognizer import OpenCVFaceRecognizer
from presentation.cli.main_menu import MainMenu
from presentation.camera.camera_manager import CameraManager
from infrastructure.database.sqlite_event_storage import SQLiteEventStorage

def main():
    detector = OpenCVFaceDetector()
    recognizer = OpenCVFaceRecognizer()
    camera = CameraManager()
    event_storage = SQLiteEventStorage()
    
    menu = MainMenu(detector, recognizer, camera, event_storage)
    menu.run()

if __name__ == "__main__":
    main()
