import cv2

class CameraManager:
    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.camera = None
    
    def start(self):
        if self.camera is None:
            self.camera = cv2.VideoCapture(self.camera_id)
            if not self.camera.isOpened():
                raise Exception("Erro ao acessar a câmera!")
    
    def stop(self):
        if self.camera is not None:
            self.camera.release()
            self.camera = None
    
    def capture_frame(self):
        if self.camera is None:
            self.start()
        
        ret, frame = self.camera.read()
        if not ret:
            return None
        
        return frame
    
    def __del__(self):
        self.stop()