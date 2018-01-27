import json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from config import ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET

twitter = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

class TwitterReceiver():
    
    def __init__(self, ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET):
        oAuth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        self.twitter_stream = TwitterStream(auth=oAuth)

    def receive_tweets(self, twitter, nb_items):
        # Set an iterator which iterates all visible tweets on Twitter
        iterator = self.twitter_stream.statuses.sample()

        # Iterate the tweets with index
        for idx, tweet in enumerate(iterator):
            if idx == nb_items - 1:
                break
            else:
                print(json.dumps(tweet, indent=4))

if __name__ == "__main__":
    t = TwitterReceiver(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    t.receive_tweets(t, 5)

