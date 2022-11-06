![Logo](nlru.png)
# NLRU Scorekeeper
A simple scorekeeper to be used by the NLRU when live streaming matches to provide a simple score board when using OBS. This application was developed by Liam Warren.

## Setup Instructions
### Python Virtual Environment
These instructions should work but I have not tested them, here is a general [link](https://docs.python.org/3/library/venv.html) on Python Virtual Environments.

`pip install virtualenv`

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

### Facebook API
Here are some [general instructions](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/) on how to obtain the necessary tokens for the Facebook Graph API that is used in this application. Once you have the necessary information you will need to update the below in the `SocialMedia/facebook.py` file 
```        
page_id = 0
facebook_access_token = 'put here'
```

### Twitter API
Here are some [general instructions](https://docs.tweepy.org/en/stable/authentication.html#:~:text=You%20can%20generate%20an%20access,Callback%20%2F%20Redirect%20URI%20%2F%20URL./) on how to obtain the necessary tokens for the Tweepy API that is used in this application. Once you have the necessary information you will need to update the below in the `SocialMedia/twitter.py` file

```        
# Consumer keys and access tokens, used for OAuth
CONSUMER_KEY = 'put here'
CONSUMER_SECRET = 'put here'
ACCESS_KEY = 'put here'
ACCESS_SECRET = 'put here'
```
### OBS
Here is a [YouTube video](https://www.youtube.com/watch?v=j5NRUIYM8gw&ab_channel=Howit%27sDONE%21%21) that walks through how to set up OBS to use this score keeper as a score board.
