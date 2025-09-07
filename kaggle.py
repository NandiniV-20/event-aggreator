import requests
from bs4 import BeautifulSoup
from models import Event

BASE_URL = "https://www.kaggle.com/competitions"

def scrape_kaggle()->list[Event]:
    events=[]
    r=requests.get(BASE_URL)
    soup=BeautifulSoup(r.text,"html.parser")
    
    for comp in soup.select("div.sc-c44e4e70-0"):
        title=comp.get_text(strip=True)
        link_tag = comp.find("a")
        link = "https://www.kaggle.com"+ link_tag["href" if link_tag else BASE_URL]
        
        events.append(
            Event(
                title=title,
                link=link,
                source="Kaggle",
                category="Competitions",
                deadline="N/A",
            )
        )
    return events