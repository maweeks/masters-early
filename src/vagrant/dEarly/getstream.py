from secrets import *

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, TimeCount

import json
import tweepy, webapp2
from tweepy.streaming import StreamListener
from tweepy import Stream

initialData = True
currentTime = ""
timeCounter = 0

def storeData(time, count):
    print time + " " + str(count)
    engine = create_engine('sqlite:///dEarly.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Add DateTime
    timenum = TimeCount(timestamp=datetime.strptime((time[0:19] + time[25:30]), '%a %b %d %H:%M:%S %Y'), count=count)
    session.add(timenum)
    session.commit()

    print "Database populated."

def processData(dataJSON):
    global currentTime
    global initialData
    global timeCounter
    if initialData:
        if ('created_at' in dataJSON):
            initialData = False
            currentTime = dataJSON['created_at']
            timeCounter += 1
    else:
        # print(data)
        # print(str(dataJSON['user']['name'].encode("utf-8")))
        # print(dataJSON['created_at'])
        # print(data)
        # for tag in dataJSON['entities']['hashtags']:
        #     print '#' + tag['text'].encode("utf-8")
        # print(dataJSON['text'].encode("utf-8") + "\n")
        if ('created_at' in dataJSON):
            if currentTime == dataJSON['created_at']:
                timeCounter += 1
            elif currentTime <= dataJSON['created_at']:
                storeData(currentTime, timeCounter)
                timeCounter = 1
                currentTime = dataJSON['created_at']
            else:
                print "Redacted"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        processData(json.loads(data))
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(getConsumerKey(), getConsumerSecret())
    auth.secure = True
    auth.set_access_token(getAccessToken(), getAccessTokenSecret())

    stream = Stream(auth, l)
    stream.filter(track=['GameofThrones'])