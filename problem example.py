import tweepy
import os
import random
import time
from datetime import datetime, timedelta
import pytz
import requests

# Define your proxy server
proxy_server = 'example.proxyserver.com'  # Replace with your proxy server
proxy_port = 8080  # Replace with your proxy port (e.g., 8080)

# Replace with your own API keys and access tokens
consumer_key = 'your_consumer_key'  # Replace with your API key
consumer_secret = 'your_consumer_secret'  # Replace with your API secret key
access_token = 'your_access_token'  # Replace with your access token
access_token_secret = 'your_access_token_secret'  # Replace with your access token secret

# Replace with your Twitter username
twitter_username = 'your_twitter_username'  # Replace with your Twitter username

# Function to set up proxy for requests
def set_proxy():
    proxies = {
        "http": f"http://{proxy_server}:{proxy_port}",
        "https": f"http://{proxy_server}:{proxy_port}"
    }
    session = requests.Session()
    session.proxies = proxies
    return session

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to post a tweet with an image
def post_tweet_with_image(tweet_text, image_path, session):
    try:
        media = api.media_upload(image_path)
        api.update_status(status=tweet_text, media_ids=[media.media_id])
        print(f"Tweeted: {tweet_text}")
    except tweepy.TweepError as e:
        print(f"Error posting tweet: {e}")
    finally:
        # Disconnect from the proxy after posting or encountering an error
        session.close()

# Function to schedule tweets at a specific time in US Pacific Standard Time (PST)
def schedule_tweets(image_folder, text_file):
    pacific_timezone = pytz.timezone('US/Pacific')

    while True:
        current_time = datetime.now(pacific_timezone)

        # Check if it's your desired time to tweet
        if (current_time.hour == 12 and current_time.minute == 0):  # Replace with your desired time
            print(f"Scheduling tweet for {current_time.strftime('%I:%M %p')} PST")
            
            # Rest of your code...

        # Sleep until the next minute
        time.sleep(60)  # Sleep for 1 minute before checking again

# Specify the folder where your images are stored
image_folder = 'C:/Users/yourusername/Desktop/images'  # Replace with your image folder path

# Specify the path to the text file with tweet content
text_file = 'C:/Users/yourusername/Desktop/tweets.txt'  # Replace with your text file path

# Start scheduling tweets
schedule_tweets(image_folder, text_file)
