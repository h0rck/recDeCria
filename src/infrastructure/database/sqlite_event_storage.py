from domain.interfaces.event_storage import EventStorage
from .database_manager import DatabaseManager

class SQLiteEventStorage(EventStorage):
    def __init__(self):
        self.db = DatabaseManager()
    
    def save_event(self, person_id: str, confidence: float, location: str, 
                  additional_data: dict = None):
        self.db.save_event(person_id, confidence, location, additional_data)
    
    def get_latest_events(self, limit: int = 10):
        return self.db.get_latest_events(limit)