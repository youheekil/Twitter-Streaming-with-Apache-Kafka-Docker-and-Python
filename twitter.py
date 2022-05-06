import tweepy
import json
import logging 

FORMAT = "%(asctime)s | %(name)s - %(levelname)s - %(message)s"
LOG_FILEPATH = "logs/testing.log/"
logging.basicConfig(
    filename=LOG_FILEPATH,
    level=logging.INFO,
    filemode='w',
    format=FORMAT)


# Load config.json and get input and output paths
with open('config.json','r') as f:
    config = json.load(f) 

twitter_api_key = config['twitter_api_key']
twitter_api_secret_key = config['twitter_api_secret_key']
twitter_access_token = config['twitter_access_token']
twitter_access_token_secret = config['twitter_access_token_secret']
bearer_token = config['bearer_token']


if __name__ == "__main__":
    print(bearer_token)
    logging.info('printing bearer token')