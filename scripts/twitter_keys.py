from requests_oauthlib import OAuth1

# authentication pieces
client_key    = '' # Insert your key here
client_secret = '' # Insert your key here
token         = '' # Insert your key here
token_secret  = '' # Insert your key here

# the base for all Twitter calls
base_twitter_url = 'https://api.twitter.com/1.1/'

# setup authentication
oauth = OAuth1(client_key, client_secret, token, token_secret)
