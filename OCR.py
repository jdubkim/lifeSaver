import http.client, urllib.request, urllib.parse, urllib.error, base64, json
from config import OCR_ACCESS_KEY

subscription_key = OCR_ACCESS_KEY

class OCR():
    def __init__(self, document):
        self.uri_base = 'westcentralus.api.cognitive.microsoft.com'

    def readCharacter(self, url):
        headers = {
        # Request headers.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
        }

        params = urllib.parse.urlencode({
        # Request parameters. All of them are optional.
        'visualFeatures': 'Categories,Description,Color',
        'language': 'en',
        })

        # Replace the three dots below with the URL of a JPEG image of a celebrity.
        body = url
        #"{'url':'https://upload.wikimedia.org/wikipedia/commons/1/12/Broadway_and_Times_Square_by_night.jpg'}"

        try:
            # Execute the REST API call and get the response.
            conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
            conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
            response = conn.getresponse()
            data = response.read()

        # 'data' contains the JSON data. The following formats the JSON data for display.
            parsed = json.loads(data)
            print ("Response:")
            print (json.dumps(parsed, sort_keys=True, indent=2))
            conn.close()

        except Exception as e:
            print('Error:')
            print(e)
