from abc import ABC, abstractmethod
import numpy as np
from typing import List, Tuple

class FaceDetector(ABC):
    @abstractmethod
    def detect_faces(self, image: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """
        Detecta faces em uma imagem
        Args:
            image: Imagem numpy array (BGR)
        Returns:
            Lista de tuplas (x, y, width, height) para cada face
        """
        pass