from src.infrastructure.recognition.opencv_detector import OpenCVFaceDetector
from src.infrastructure.recognition.opencv_recognizer import OpenCVFaceRecognizer
from src.presentation.cli.main_menu import MainMenu
from src.presentation.camera.camera_manager import CameraManager
from src.infrastructure.database.sqlite_event_storage import SQLiteEventStorage

def main():
    camera = CameraManager()
    event_storage = SQLiteEventStorage()
    
    # Inicializa o menu com armazenamento de eventos
    menu = MainMenu(detector, recognizer, camera, event_storage)
    menu.run()

if __name__ == "__main__":
    main()