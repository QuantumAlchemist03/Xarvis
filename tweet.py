import os
import tweepy
from datetime import datetime
import random

TWEET_FILE = "tweets.txt"
COUNTER_FILE = "tweet_counter.txt"

def load_tweets():
    if not os.path.exists(TWEET_FILE):
        raise FileNotFoundError(f"{TWEET_FILE} not found.")
    with open(TWEET_FILE, "r", encoding="utf-8") as f:
        tweets = [line.strip() for line in f if line.strip()]
    return tweets

def get_next_tweet(tweets):
    if not os.path.exists(COUNTER_FILE):
        index = 0
    else:
        with open(COUNTER_FILE, "r") as f:
            try:
                index = int(f.read().strip())
            except ValueError:
                index = 0

    # Wrap around if index exceeds tweet count
    index = index % len(tweets)

    # Save the next index
    with open(COUNTER_FILE, "w") as f:
        f.write(str(index + 1))

    return tweets[index]

def post_tweet(text):
    client = tweepy.Client(
        consumer_key=os.environ['TWITTER_API_KEY'],
        consumer_secret=os.environ['TWITTER_API_SECRET'],
        access_token=os.environ['TWITTER_ACCESS_TOKEN'],
        access_token_secret=os.environ['TWITTER_ACCESS_SECRET']
    )

    # Append timestamp for uniqueness
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    tweet = f"{text}\n\n🕒 {now}"

    response = client.create_tweet(text=tweet)
    print("Tweet posted:", response.data)

def main():
    try:
        tweets = load_tweets()
        tweet_text = get_next_tweet(tweets)
    except Exception as e:
        print("Sequential selection failed, using random fallback:", e)
        tweets = load_tweets()
        tweet_text = random.choice(tweets)

    post_tweet(tweet_text)

if __name__ == "__main__":
    main()
