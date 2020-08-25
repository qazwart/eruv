# Eruv

# Name
Eruv

# Synopsis
Twitter/Twilio/AWS Lambda Interface

#Authors
Original Author: Shalom Kaplan
Updated by: David Weintraub (david@weintraub)

# Description
This was part of a package to setup an Eruv hotline that was automated. In Highland Park, we use Twitter as
our official means of distributing the Eruv's status. One of those means is a phone number hotline that
reads out the last tweet from the Eruv's Twitter account.

This program uses a phone number provided by Twilio using Programmable Voice to execute a program on 
AWS Lambda. The phone number does an HTTPS POST to the program. The program responds by creating a
specialized XML file called a TwiIML format and returns that for Twilio to read to the caller.

1. You need a [Twitter](https://twitter.com) account.
2. You will need a register for the [Twitter API](https://developer.twitter.com).
2. You need a [Twilio](https://twilio.com) *Programable Voice* account. This account will require
   a credit card and charges $1.00 per month and .013¢ per phone call.
3. You need an [AWS](https://aws.amazon.com) account. Unless you expect more than 1,000,000
   calls per month, you may use the free tier.
   
* Setup an *App* in the Twitter API. You need to do this to get a *Twitter API Key* and a *Twitter API Secret Key*.
  These two keys will be setup in your AWS Lambda environment.
* Setup your *Twilio* account. You need to create an app to get the two TWILIO api keys needed. You will fill
  in the programable voice URL later.
* Set up your AWS account, and go to Lambda services. You need to create a *Function*.
* Add in the Python Script under the `Eruv` directory
* Add in the `Twilio_API_Layer.zip` file under the Layer tab.
* Find the URL of your program uses to execute it.
* Try executing it via the `Test` button.
* Try executing it remotely via a `curl` or `wget` command.


# Environment
* `TWITTER_KEY`: The Twitter key used by the Twitter API Developer's account.
* `TWITTER_SECRET`: The *secret key* that is used. This should not be shared.
* `PYTHON_PATH`: `/opt`
* `TWILIO_ACCOUNT_SID`: From Twilio
* `TWILIO_AUTH_TOKEN`: From Twilio

# Files
* `Eruv/eruv.py`: The Python Program called by the HTTPS POST
* `Twilio_API_Layer.zip`: The Python packages needed, but
   not provided by AWS Lambda. Basically Tweepy and Twilio APIs
   
