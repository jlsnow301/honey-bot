import tweepy
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    access_token=access_token,
    access_token_secret=access_token_secret,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
)

accounts = [
    "instagram",
    "youtube",
    "twitter",
    "facebook",
    "tiktok",
    "snapchat",
    "reddit",
    "twitch",
    "pinterest",
    "linkedin",
    "tumblr",
    "quora",
    "flickr",
    "myspace",
]

actions = [
    "suspended",
    "banned",
    "hacked",
    "stolen",
]


print("creating a bait tweet")
bait = client.create_tweet(
    text=f"my {random.choice(accounts)} account was {random.choice(actions)}"
)

print("waiting 30 minutes")
time.sleep(1800)

print("let's see who replied")
users = client.get_tweet(id=bait["id"], user_auth=True)

usernames = ""
for user in users:
    usernames += f"@{user['username']} "

print("adding the tweet to the pinned tweet")
client.create_tweet(
    text=f"{usernames} {random.choice(actions)}",
    in_reply_to_tweet_id=os.getenv("PINNED_TWEET_ID"),
)
