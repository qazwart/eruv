# Eruv

# NAME
Eruv

# SYNOPSIS
Twitter/Twilio/AWS Lambda Interface

# DESCRIPTION
This was part of a package to setup an Eruv hotline that was automated. In Highland Park, we use Twitter as
our official means of distributing the Eruv's status. One of those means is a phone number hotline that
reads out the last tweet from the Eruv's Twitter account.

This program uses a phone number provided by Twilio using Programmable Voice to execute a program on 
AWS Lambda. The phone number does an HTTPS POST to the program. The program responds by creating a
specialized XML file called a TwiIML format and returns that for Twilio to read to the caller.

# ENVIRONMENT
* `TWITTER_KEY`: The Twitter key used by the Twitter API Developer's account.
* `TWITTER_SECRET`: The *secret key* that is used. This should not be shared.

# FILES
* `Eruv/eruv.py`: The Python Program called by the HTTPS POST
* `Twilio_API_Layer-8bc98bc7-3217-4d5c-8f6a-7a3de806c3cf.zip`: The Python packages needed, but
   not provided by AWS Lambda. Basically Tweepy and Twilio APIs
   
