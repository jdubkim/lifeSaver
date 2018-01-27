import json
import urllib
import http.client as htlib
from config import TA_ACCESS_KEY


accessKey = TA_ACCESS_KEY

class Analyser():

    def __init__(self, accessKey):
        self.accessKey = accessKey
        self.uri = 'westcentralus.api.cognitive.microsoft.com'

    def getSentiment(self, documents):
        "Gets the sentiments for a set of documents and returns the information."
        path = '/text/analytics/v2.0/sentiment'
        headers = {'Ocp-Apim-Subscription-Key': accessKey}
        conn = htlib.HTTPSConnection(self.uri)
        body = json.dumps(documents)
        conn.request("POST", path, body, headers)
        response = conn.getresponse()
        return response.read()

    def getKeyPhrases(self, documents):
        "Gets the sentiments for a set of documents and returns the information."
        path = '/text/analytics/v2.0/keyPhrases'
        headers = {'Ocp-Apim-Subscription-Key': accessKey}
        conn = htlib.HTTPSConnection(self.uri)
        body = json.dumps(documents)  # change documents into json file (IN the tweet, we don't have to do that)
        conn.request("POST", path, body, headers)
        response = conn.getresponse()
        return response.read()

    def convertToDecision(self, documents):

        tweets = []

        for tweet in documents["documents"]:
            #if tweet["score"] < 0.02:
                # serious

            #elif tweet["score"] < 0.1:
                #little bit serious

            if tweet["score"] < 0.5:
                # good
                tweets.append(tweet["name"])
            else:
                # don't consider
                tweets.append(tweet["name"])

analyser = Analyser(accessKey)
documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': 'I am a trash. I dont deserve anything.' },
    { 'id': '2', 'language': 'en', 'text': 'Just because you are trash does not mean you cannot do great things. It is called garbage can, not garbage cant.' }
]}

print(analyser.getSentiment(documents))
print(analyser.getKeyPhrases(documents))
