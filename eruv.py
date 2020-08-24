import tweepy
import os
from datetime import datetime
# import pytz

from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

#
# CONSTANTS
#

TWITTER_KEY = os.environ["TWITTER_KEY"]
TWITTER_SECRET = os.environ["TWITTER_SECRET"]
TWILIO_VOICE = "man"
DAYS_ERUV_STATUS_IS_GOOD = 5
CONCLUSION = 'Shabbat Shalom'
PREAMBLE = "Thank you for calling the Edison Highland Park Eruv Hotline. "

NOT_CHECKED = """The eruv status has not been determined. 
The status is usually determined about 2 hours before candle lighting.
Sometimes it may be later. Please call back later."""

def getTweet():
    auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
    api = tweepy.API(auth)
    user = api.get_user('hp_eruv')
    tweet = api.user_timeline(user.id, count=1, tweet_mode='extended')[0]
    tweetText = tweet.full_text
    #
    # DETERMINE TWEET DATE
    #
    tweetDate = tweet.created_at
    date_of_tweet = tweetDate.strftime("%A, %B %e")
    
    now = datetime.utcnow()
    daysSinceTweet = (now - tweetDate).days
    
    if daysSinceTweet < DAYS_ERUV_STATUS_IS_GOOD:
        return PREAMBLE + date_of_tweet + ". " + tweetText + CONCLUSION
    else:
        return NOT_CHECKED


def lambda_handler(event, context):
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    tweet = getTweet()
    message = tweet
    resp.say(message, voice=TWILIO_VOICE)
    
    response = {
        "headers": {"content-type": "text/xml"},
        "statusCode": 200,
        "body": str(resp),
    }

    return response
