# news_scraper.py
from gnews import GNews

def scrape_news(query, limit=10):
    google_news = GNews(language='en', max_results=limit)
    results = google_news.get_news(query)
    return [item['title'] + ' ' + item['description'] for item in results]
