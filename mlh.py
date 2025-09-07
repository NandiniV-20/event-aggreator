import requests
from bs4 import BeautifulSoup

def scrape_mlh():
    url="https://mlh.io/seasons/2025/events"
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    events=[]
    for card in soup.select(".event-wrapper"):
        title=card.select_one(".event-name").text.strip()
        link=card.select_one("a")["href"]
        location=card.select_one(".event-location").text.strip()
        date=card.select_one(".event-date").text.strip()
        events.append({
            "title":title,
            "link":link,
            "source":"MLH",
            "category":"Hackathon",
            "location":location,
            "date":date,
            "description":" "
        })
    return events