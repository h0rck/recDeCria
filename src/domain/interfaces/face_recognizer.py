from abc import ABC, abstractmethod
import numpy as np
from typing import List, Tuple, Optional

class FaceRecognizer(ABC):
    @abstractmethod
    def train(self, face_images: List[np.ndarray], user_id: str) -> None:
        """
        Treina o reconhecedor com imagens de um usuário
        Args:
            face_images: Lista de imagens de face
            user_id: Identificador único do usuário
        """
        pass
    
    @abstractmethod
    def predict(self, face_image: np.ndarray) -> Tuple[Optional[str], float]:
        """
        Reconhece uma face
        Args:
            face_image: Imagem de uma face
        Returns:
            Tupla (user_id, confiança) ou (None, 0.0) se não reconhecido
        """
        pass