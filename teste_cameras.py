import cv2
import time

def testar_camera(camera_id):
    print(f"\nTestando câmera {camera_id}...")
    
    # Tenta abrir a câmera
    webcam = cv2.VideoCapture(camera_id)
    
    # Verifica se abriu
    if not webcam.isOpened():
        print(f"Erro: Não foi possível acessar a câmera {camera_id}")
        return False
        
    # Obtém informações da câmera
    largura = webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
    altura = webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = webcam.get(cv2.CAP_PROP_FPS)
    
    print(f"Câmera {camera_id} aberta com sucesso!")
    print(f"Resolução: {largura}x{altura}")
    print(f"FPS: {fps}")
    print("Pressione 'q' para fechar esta câmera e testar a próxima")
    
    # Carrega o detector facial
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    
    start_time = time.time()
    frames = 0
    
    while True:
        # Lê um frame
        ret, frame = webcam.read()
        
        if not ret:
            print(f"Erro ao capturar frame da câmera {camera_id}")
            break
            
        # Converte para escala de cinza para detecção facial
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detecta faces
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        # Desenha retângulos nas faces detectadas
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'Rosto Detectado', (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Adiciona informações na imagem
        frames += 1
        time_elapsed = time.time() - start_time
        fps_atual = frames / time_elapsed
        
        cv2.putText(frame, f'Camera: {camera_id}', (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f'FPS: {fps_atual:.2f}', (10, 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f'Rostos detectados: {len(faces)}', (10, 90), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Mostra o frame
        cv2.imshow(f'Camera {camera_id}', frame)
        
        # Verifica se 'q' foi pressionado
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libera os recursos
    webcam.release()
    cv2.destroyAllWindows()
    return True

def main():
    print("Iniciando teste das câmeras...")
    
    # Testa a primeira câmera
    sucesso_cam0 = testar_camera(0)
    
    # Testa a segunda câmera
    sucesso_cam1 = testar_camera(1)
    
    print("\nResultado dos testes:")
    print(f"Câmera 0: {'Funcionou' if sucesso_cam0 else 'Falhou'}")
    print(f"Câmera 1: {'Funcionou' if sucesso_cam1 else 'Falhou'}")

if __name__ == "__main__":
    main()