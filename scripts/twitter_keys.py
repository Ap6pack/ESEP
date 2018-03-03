from requests_oauthlib import OAuth1

# authentication pieces
CONSUMER_KEY = '' # Insert your key here
CONSUMER_SECRET = '' # Insert your key here
key = '' # Insert your key here
secret = '' # Insert your key here
url = 'https://api.twitter.com/1.1/'

# setup authentication
oauth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, key, secret)
