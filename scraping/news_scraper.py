import requests
from bs4 import BeautifulSoup

def scrape_news_headlines(url):
    headlines = []
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    for item in soup.select('h3, h2'):
        text = item.get_text(strip=True)
        if text:
            headlines.append(text)
    return headlines
