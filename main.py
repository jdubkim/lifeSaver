import json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from config import ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.sample()

tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    print (json.dumps(tweet))

    if tweet_count <= 0:
        break

