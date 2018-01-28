import json
import time
from analyser import Analyser

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from config import ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET, TA_ACCESS_KEY

twitter = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

class TwitterReceiver():
    
    def __init__(self, ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET):
        oAuth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        self.twitter_stream = TwitterStream(auth=oAuth)
        self.analyser = Analyser(TA_ACCESS_KEY)

    def receive_tweets(self, nb_items):
        # Read data from json
        fn = 'data.json'
        try:
            f = open(fn, 'r')
        except:
            f = open(fn, 'w')
            f.write('{}')
            f.close()
            f = open(fn, 'r')

        json_data = json.load(f)
        f.close()

        # Set flag isEmpty
        isEmpty = json_data == {}

        if isEmpty:
            json_data["documents"] = []
        # Set an iterator which iterates all visible tweets on Twitter
        iterator = self.twitter_stream.statuses.sample()

        # Iterate the tweets with index
        for idx, tweet in enumerate(iterator):
            if idx == nb_items:
                break
            elif 'created_at' not in tweet:
                print('The signal is tweet deletion')
                continue
            elif not tweet['user']['lang'] == 'en':
                continue
            else:
                if not isEmpty:
                        print(json_data["documents"])   
                        json_data["documents"].append({"id": tweet["user"]["screen_name"], "text": tweet["text"]})
                else:
                        json_data["documents"].append({"id": tweet["user"]["screen_name"], "text": tweet["text"]})

        with open("data.json", 'w') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

    def pop_sent_user(self, username):

        with open("data.json", 'r') as f:
            data = json.load(f)
            print(data)

        del data[username]
        print(username + "got a message and was deleted from json")

        with open('data.json', 'w') as f:
            data = json.dump(data, f, ensure_ascii=False)


if __name__ == "__main__":
    t = TwitterReceiver(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    while (True):

        t.receive_tweets(10)
        with open('data.json', 'r') as f:
            data = json.load(f)
            sentiment = json.loads(t.analyser.getSentiment(data))
            keyphrases = json.loads(t.analyser.getKeyPhrases(data))
            print(sentiment['documents'])
            print(keyphrases['documents'])

            constructed = {'documents': []}

            for i in range(len(sentiment['documents'])):
                constructed['documents'].append(
                    dict(list(sentiment['documents'][i].items()) + list(keyphrases['documents'][i].items())))

            print(constructed)
            time.sleep(10)




