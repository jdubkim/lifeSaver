from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from config import ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET

class TwitterSender():
    
    def __init__(self, ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET):
        oAuth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        self.twitter =  Twitter(auth=oAuth)

    def send_message(self, user, text):
        self.twitter.direct_messages.new(user=user, text=text)

if __name__ == "__main__":
    t = TwitterSender(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    t.send_message('@twit_reva', '!!')

