# -*- coding: utf-8 -*-

import urllib
import http.client as httplib
import json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the accessKey string value with your valid access key.
accessKey = '6509333f34564524b892bc9bc52d505d'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your access keys.
# For example, if you obtained your access keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial access keys are generated in the westcentralus region, so if you are using
# a free trial access key, you should not need to change this region.
uri = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'

def GetSentiment (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

def GetKeyPhrases (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps(documents)  # change documents into json file (IN the tweet, we don't have to do that)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': 'I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable.' },
    { 'id': '2', 'language': 'es', 'text': 'I had a terrible day today.' },
    { 'id': '3', 'language': 'en', 'text': 'I want to kill myself.'}
]}

print ('Please wait a moment for the results to appear.\n')

result = GetSentiment (documents)
print (json.dumps(json.loads(result), indent=4))

