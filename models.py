from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:
    title:str
    link:str
    source:str
    category:str
    deadline:str
    created_at:datetime=datetime.utcnow()
    