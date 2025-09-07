import requests
from bs4 import BeautifulSoup
from models import Event

BASE_URL = "https://devpost.com/hackathoms"

def scrape_devpost()-> list[Event]:
    events=[]
    r=requests.get(BASE_URL)
    soup = BeautifulSoup(r.text,"html.parser")
    
    for card in soup.select(".hackathon-title"):
        title=card.select_one(".title").get_text(strip=True)
        link=card.select_one("a")["href"]
        deadline = card.select_one(".submission-deadline")
        deadline_text = deadline.get_text(strip=True) if deadline else "N/A"
        
        events.append(
            Event(
                title=title,
                link=link,
                source="Devpost",
                category="Hackathon",
                deadline=deadline_text,
            )
        )
    return events