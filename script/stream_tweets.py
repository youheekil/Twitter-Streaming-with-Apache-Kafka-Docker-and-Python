import tweepy
from tweepy.auth import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import logging 

FORMAT = "%(asctime)s | %(name)s - %(levelname)s - %(message)s"
LOG_FILEPATH = "logs/testing.log/"
logging.basicConfig(
    filename=LOG_FILEPATH,
    level=logging.INFO,
    filemode='w',
    format=FORMAT)



# Authenticate to Twitter

class SimpleStreamListener(tweepy.StreamListener):
    """
    Streaming the recent tweets related to the query to Azure Datalake
    """

    def __init__(self, config):
        super(tweepy.StreamListener, self).__init__()

        # Set up configuration
        # Load config.json and get input and output paths


        self.CONSUMER_KEY = credential['twitter_api_key']
        self.CONSUMER_SECRET = credential['twitter_api_secret_key']
        self.ACCESS_TOKEN = credential['twitter_access_token']
        self.ACCESS_TOKEN_SECRET = credential['twitter_access_token_secret']
        self.bearer_token = credential['bearer_token']
    
    

    def on_status(self, status):
        print(status)
    
    
    def main():
        # read credential file
        with open('credential.json','r') as f:
            credential = json.load(f)
        
        # start logging
        logging.info("Started logging")

        # Authenticating twitter API
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)

        # Start Streaming to Azure Synapse
        logging.info("Start streaming tweets")

        twitterStream = tweepy.Stream(auth, stream_listener) 
        twitterStream.filter(track=['autonomous driving', "Autonomous Vehicles"])

        

if __name__=="__main__":
    SimpleStreamListener()
    
    
