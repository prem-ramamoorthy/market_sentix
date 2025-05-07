import snscrape.modules.twitter as sntwitter
import datetime

def scrape_tweets(query, limit=100):
    tweets = []
    since_date = (datetime.date.today()).isoformat()
    for tweet in sntwitter.TwitterSearchScraper(f'{query} since:{since_date}').get_items():
        if len(tweets) >= limit:
            break
        tweets.append({
            'date': tweet.date,
            'content': tweet.content,
            'username': tweet.user.username,
            'url': tweet.url,
            'retweets': tweet.retweetCount,
            'likes': tweet.likeCount
        })
    return tweets