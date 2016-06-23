from secrets import *

import json
import tweepy, webapp2
from tweepy.streaming import StreamListener
from tweepy import Stream

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(getConsumerKey(), getConsumerSecret())
    auth.secure = True
    auth.set_access_token(getAccessToken(), getAccessTokenSecret())

    stream = Stream(auth, l)
    stream.filter(track=['football'])