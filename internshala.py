import requests
from bs4 import BeautifulSoup
from models import Event
BASE_URL = "https://internshala.com/internships/keywords-{}"

def scrape_internshala(role: str="data-science")->list[Event]:
    events=[]
    url=BASE_URL.format(role.replace(" ","-"))
    r=requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    
    for card in soup.select(".individual_internship"):
        title = card.select_one("h3 a").get_text(strip=True)
        link="https://internshala.com"+card.select_one("h3 a")["href"]
        deadline=card.select_one(".status")
        deadline_text = deadline.get_text(strip=True) if deadline else "N/A"
        
        events.append(
            Event(
                title=title,
                link=link,
                source="Internshala",
                category="Internship",
                deadline=deadline_text
            )
        )
    return events
    