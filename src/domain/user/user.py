from dataclasses import dataclass
from datetime import datetime
from typing import List
import cv2
import numpy as np

@dataclass
class User:
    name: str
    photos: List[np.ndarray]
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()