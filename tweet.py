import os
import tweepy
from datetime import datetime

def main():
    client = tweepy.Client(
        consumer_key=os.environ['TWITTER_API_KEY'],
        consumer_secret=os.environ['TWITTER_API_SECRET'],
        access_token=os.environ['TWITTER_ACCESS_TOKEN'],
        access_token_secret=os.environ['TWITTER_ACCESS_SECRET']
    )

    # Add current datetime to make tweet unique
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    tweet_text = f"Hello from GitHub Actions! 🚀 #AutomatedTweet at {now}"
    
    response = client.create_tweet(text=tweet_text)
    print("Tweet posted:", response.data)

if __name__ == "__main__":
    main()
