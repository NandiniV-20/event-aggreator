from scrapers.mlh import scrape_mlh
# from scrapers.devpost import scrape_devpost
# from scrapers.kaggle import scrape_kaggle
# from scapers.internshala import scrape_internshala

from db import Event, SessionLocal

def run_pipeline():
    db=SessionLocal()
    events=[]
    
    try:
        events.extend(scrape_mlh())
        # events.extend(scrape_devpost())
        # events.extend(scrape_kaggle())
        # events.extend(scrape_internshala())
        
        for ev in events:
            exists = db.query(Event).filter_by(title=ev["title"],source=ev["source"]).first()
            if not exists:
                db.add(Event(**ev))
        db.commit()
        
    finally:
        db.close()