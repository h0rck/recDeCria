import cv2
import numpy as np
import os
import pickle

class ReconhecimentoFacial:
    def __init__(self):
        # Carrega o classificador para detecção facial
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        
        # Inicializa o reconhecedor
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        
        # Diretório para salvar as imagens de treino
        self.diretorio_fotos = 'fotos_cadastro'
        os.makedirs(self.diretorio_fotos, exist_ok=True)
        
        # Carrega o modelo se existir
        self.arquivo_modelo = 'modelo_facial.yml'
        self.arquivo_nomes = 'nomes.pkl'
        self.nomes = []
        self.carregar_modelo()
    
    def carregar_modelo(self):
        """Carrega o modelo treinado se existir"""
        if os.path.exists(self.arquivo_modelo):
            self.recognizer.read(self.arquivo_modelo)
            with open(self.arquivo_nomes, 'rb') as f:
                self.nomes = pickle.load(f)
            print(f"Modelo carregado com {len(self.nomes)} pessoas")
    
    def cadastrar_pessoa(self):
        """Cadastra uma nova pessoa usando a webcam"""
        nome = input("Digite seu nome: ")
        if nome in self.nomes:
            print("Nome já cadastrado!")
            return
        
        print("\nPosicione seu rosto na frente da câmera")
        print("Serão capturadas 30 fotos diferentes")
        print("Mova um pouco seu rosto entre as capturas")
        print("Pressione 'c' para começar a captura ou 'q' para sair")
        
        webcam = cv2.VideoCapture(0)
        if not webcam.isOpened():
            print("Erro ao acessar a webcam!")
            return
        
        fotos_capturadas = 0
        faces_capturadas = []
        
        while True:
            ret, frame = webcam.read()
            if not ret:
                break
            
            # Converte para escala de cinza
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detecta faces
            faces = self.face_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
            )
            
            # Desenha retângulo na face detectada
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Mostra quantidade de fotos capturadas
            cv2.putText(frame, f'Fotos: {fotos_capturadas}/30', (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.imshow('Cadastro', frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('c') and len(faces) == 1:
                x, y, w, h = faces[0]
                face_img = gray[y:y+h, x:x+w]
                face_img = cv2.resize(face_img, (150, 150))
                faces_capturadas.append(face_img)
                fotos_capturadas += 1
                
                if fotos_capturadas >= 30:
                    break
        
        webcam.release()
        cv2.destroyAllWindows()
        
        if fotos_capturadas < 30:
            print("Cadastro cancelado!")
            return
        
        # Treina o reconhecedor com as novas fotos
        id_pessoa = len(self.nomes)
        for face_img in faces_capturadas:
            self.recognizer.update([face_img], np.array([id_pessoa]))
        
        # Salva o modelo e os nomes
        self.nomes.append(nome)
        self.recognizer.write(self.arquivo_modelo)
        with open(self.arquivo_nomes, 'wb') as f:
            pickle.dump(self.nomes, f)
        
        print(f"Cadastro de {nome} realizado com sucesso!")
    
    def iniciar_reconhecimento(self):
        """Inicia o reconhecimento em tempo real"""
        if not self.nomes:
            print("Nenhuma pessoa cadastrada!")
            return
        
        print("\nIniciando reconhecimento...")
        print("Pressione 'q' para sair")
        
        webcam = cv2.VideoCapture(0)
        if not webcam.isOpened():
            print("Erro ao acessar a webcam!")
            return
        
        while True:
            ret, frame = webcam.read()
            if not ret:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
            )
            
            for (x, y, w, h) in faces:
                face_img = gray[y:y+h, x:x+w]
                face_img = cv2.resize(face_img, (150, 150))
                
                try:
                    id_pessoa, confianca = self.recognizer.predict(face_img)
                    nome = self.nomes[id_pessoa] if confianca < 100 else "Desconhecido"
                    cor = (0, 255, 0) if nome != "Desconhecido" else (0, 0, 255)
                    
                    cv2.rectangle(frame, (x, y), (x+w, y+h), cor, 2)
                    cv2.putText(frame, f'{nome} ({confianca:.1f}%)', 
                              (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, cor, 2)
                except:
                    pass
            
            cv2.imshow('Reconhecimento Facial', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        webcam.release()
        cv2.destroyAllWindows()

def main():
    sistema = ReconhecimentoFacial()
    
    while True:
        print("\nSistema de Reconhecimento Facial")
        print("1 - Cadastrar nova pessoa")
        print("2 - Iniciar reconhecimento")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            sistema.cadastrar_pessoa()
        elif opcao == '2':
            sistema.iniciar_reconhecimento()
        elif opcao == '3':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()