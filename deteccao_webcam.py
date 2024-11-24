import cv2
import numpy as np

def iniciar_webcam():
    # Carrega o classificador de face
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    
    # Inicia a captura de vídeo (0 é a webcam padrão)
    print("Iniciando a webcam...")
    webcam = cv2.VideoCapture(0)
    
    if not webcam.isOpened():
        print("Erro: Não foi possível acessar a webcam!")
        return
    
    print("Webcam iniciada com sucesso!")
    print("Pressione 'q' para sair")
    
    while True:
        # Captura frame por frame
        ret, frame = webcam.read()
        
        if not ret:
            print("Erro ao capturar o frame!")
            break
            
        # Converte para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detecta as faces no frame
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        # Desenha um retângulo ao redor de cada face detectada
        for (x, y, w, h) in faces:
            # Retângulo verde ao redor do rosto
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Adiciona contador de pessoas
            texto = f"Pessoas detectadas: {len(faces)}"
            cv2.putText(frame, texto, (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, 
                       (0, 255, 0), 2)
        
        # Mostra o frame com as detecções
        cv2.imshow('Detecção de Pessoas', frame)
        
        # Verifica se 'q' foi pressionado para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libera os recursos
    webcam.release()
    cv2.destroyAllWindows()
    print("Programa finalizado!")

if __name__ == "__main__":
    iniciar_webcam()