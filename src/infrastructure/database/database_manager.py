import sqlite3
from pathlib import Path
from datetime import datetime
import json

class DatabaseManager:
    def __init__(self, db_file="recognition_events.db"):
        # Garante que o diretório data existe
        Path("data").mkdir(exist_ok=True)
        self.db_file = f"data/{db_file}"
        self.init_database()
    
    def init_database(self):
        """Inicializa o banco de dados com as tabelas necessárias"""
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS recognition_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    person_id TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    location TEXT NOT NULL,
                    timestamp DATETIME NOT NULL,
                    additional_data TEXT
                )
            ''')
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_person_id 
                ON recognition_events(person_id)
            ''')
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_timestamp 
                ON recognition_events(timestamp)
            ''')
            conn.commit()
    
    def save_event(self, person_id: str, confidence: float, location: str, 
                  additional_data: dict = None):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO recognition_events 
                (person_id, confidence, location, timestamp, additional_data)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                person_id,
                confidence,
                location,
                datetime.now().isoformat(),
                json.dumps(additional_data) if additional_data else None
            ))
            conn.commit()
    
    def get_latest_events(self, limit: int = 10):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM recognition_events 
                ORDER BY timestamp DESC 
                LIMIT ?
            ''', (limit,))
            return cursor.fetchall()