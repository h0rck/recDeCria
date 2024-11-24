from abc import ABC, abstractmethod
from typing import Dict, List

class EventStorage(ABC):
    @abstractmethod
    def save_event(self, person_id: str, confidence: float, location: str, 
                  additional_data: dict = None):
        """Salva um evento de reconhecimento"""
        pass
    
    @abstractmethod
    def get_latest_events(self, limit: int = 10) -> List[Dict]:
        """Retorna os últimos eventos"""
        pass

  