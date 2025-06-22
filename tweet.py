import os
import tweepy

def main():
    client = tweepy.Client(
        consumer_key=os.environ['TWITTER_API_KEY'],
        consumer_secret=os.environ['TWITTER_API_SECRET'],
        access_token=os.environ['TWITTER_ACCESS_TOKEN'],
        access_token_secret=os.environ['TWITTER_ACCESS_SECRET']
    )

    # Your tweet text here
    tweet_text = "Hello from GitHub Actions! 🚀 #AutomatedTweet"

    response = client.create_tweet(text=tweet_text)
    print("Tweet posted:", response.data)

if __name__ == "__main__":
    main()
