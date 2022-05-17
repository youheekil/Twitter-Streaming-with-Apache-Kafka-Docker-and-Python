BROKER_URL = "localhost:9092"
TOPIC_NAME = "testing2"

### twitter
import tweepy
from tweepy.auth import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import logging 


### logging 
FORMAT = "%(asctime)s | %(name)s - %(levelname)s - %(message)s"
LOG_FILEPATH = "/workspace/twitter_topic_analysis_dashboard/logs/testing.log"
logging.basicConfig(
    filename=LOG_FILEPATH,
    level=logging.INFO,
    filemode='w',
    format=FORMAT)

### Authenticate to Twitter
with open('src/credential.json','r') as f:
    credential = json.load(f)

CONSUMER_KEY = credential['twitter_api_key']
CONSUMER_SECRET = credential['twitter_api_secret_key']
ACCESS_TOKEN = credential['twitter_access_token']
ACCESS_TOKEN_SECRET = credential['twitter_access_token_secret']
BEARER_TOKEN = credential['bearer_token']



from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
    value_serializer=lambda v: v.encode('utf-8')) #Same port as your Kafka server


topic_name = "twitter_data"


class twitterAuth():
    """SET UP TWITTER AUTHENTICATION"""

    def authenticateTwitterApp(self):
        auth = OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        return auth



class TwitterStreamer():

    """SET UP STREAMER"""
    def __init__(self):
        self.twitterAuth = twitterAuth()

    def stream_tweets(self):
        while True:
            listener = ListenerTS() 
            auth = self.twitterAuth.authenticateTwitterApp()
            stream = Stream(auth, listener)
            stream.filter(track=["Starbucks"], stall_warnings=True, languages= ["en"])


class ListenerTS(StreamListener):

    def on_status(self, status):
        tweet = json.dumps({
            'id': status.id, 
            'name': status.user.name, 
            'user_location':status.user.location, 
            'text': status.text, 
            'fav': status.favorite_count, 
            'tweet_date': status.created_at.strftime("%Y-%m-%d %H:%M:%S"), 
            'tweet_location': status.place.full_name if status.place else None
        }, default=str)  

        producer.send(topic_name, tweet)
        return True


if __name__ == "__main__":
    TS = TwitterStreamer()
    TS.stream_tweets()

