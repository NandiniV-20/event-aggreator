import pandas as pd
from models import Event
def events_to_pdf(events:list[Event])->pd.DataFrame:
    return pd.DataFrame([e.__dict__ for e in events])

def deduplicate(events: list[Event])->list[Event]:
    seen=set()
    unique=[]
    for e in events:
        key=(e.title.lower().strip(),e.source)
        if key not in seen:
            seen.add(key)
            unique.append(e)
    return unique
def save_to_csv(events: list[Event],path:str):
    df = events_to_pdf(events)
    df.to_csv(pathindex=False)