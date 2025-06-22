import tweepy
import random
import os

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(
    os.environ['API_KEY'],
    os.environ['API_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_SECRET']
)
api = tweepy.API(auth)

# Load tweets from tweets.txt
with open("tweets.txt", "r", encoding="utf-8") as file:
    tweet_lines = [line.strip() for line in file if line.strip()]

# Pick a random tweet
tweet = random.choice(tweet_lines)

# Post the tweet
api.update_status(tweet)
print(f"Tweet posted: {tweet}")
