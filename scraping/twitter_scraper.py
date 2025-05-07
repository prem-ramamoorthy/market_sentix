# twitter_scraper.py (new version using Tweepy)
import tweepy
import time
# Replace with your credentials
bearer_token = "AAAAAAAAAAAAAAAAAAAAAOFk1AEAAAAAVhd%2F2vEmnqnX1y7fPEtR3GKyr3w%3DaYv9UeXfT6Lg8SCIbcr2XENiwzvVLGcbdcjIjgfMB18j2Mv1bo"

client = tweepy.Client(bearer_token=bearer_token)

def scrape_tweets(query, limit=20):
    time.sleep(1) 
    tweets = client.search_recent_tweets(query=query, max_results=limit, tweet_fields=["text"])
    return [tweet.text for tweet in tweets.data if tweets.data]
