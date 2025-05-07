from scraping.twitter_scraper import scrape_tweets
from preprocessing.cleaner import clean_text

if __name__ == "__main__":
    tweets = scrape_tweets("AAPL OR TSLA OR MSFT", limit=20)
    for tweet in tweets:
        print(f"\nOriginal: {tweet['content']}")
        print(f"Cleaned: {clean_text(tweet['content'])}")
