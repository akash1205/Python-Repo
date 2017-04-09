import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream

consumer_key = '1DgIaZnhH6O4VangHxk2j7Q6Y'
consumer_secret = 'sI1d4s54fhjb7ixnZR9iFNgzDJV3bMGWLJliI0T6pj5YefMGHs'
access_token = '159892593-SbG8wcuYpkb1LTQkF51g707hzXDOQbf0XbjG2gAo'
access_secret = 'jF1w2oml56Dclo52qwkFAzbLaMmShoWaOAUaatlZsCJrv'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('bigfar.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#india'])
