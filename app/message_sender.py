# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/sendgrid.md
#General packages
import os
from dotenv import load_dotenv
import json

#Used for sending email through sendgrid
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.
from sendgrid import SendGridAPIClient

#used for sending texts
import twilio
from twilio.rest import Client

#used for tweeting 
import math
import tweepy

def send_email(name, email, stockInfo, newsInfo, weatherInfo, sportsInfo):

    #Config nescesary environment variables        
    load_dotenv()
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
    MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

    ## COMPILE REQUEST PARAMETERS (PREPARE THE EMAIL)
    fromEmail = Email(MY_EMAIL_ADDRESS)
    toEmail = Email(email)
    subjectT = "Daily Debrief Service"
    message_text = "Not nescesary"

    Hcontent = Content("text/html", message_text)
    mail = Mail(fromEmail, subjectT, toEmail, Hcontent)

    mail.template_id = 'd-b8e619d4d2b046af9c76cd18740ab021'
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)

    # ISSUE REQUEST (SEND EMAIL)
    #HELP with request building from https://github.com/sendgrid/sendgrid-python/issues/591
    request_body = mail.get()

    # attach whatever data you want directly...
    request_body['personalizations'][0]['dynamic_template_data']  = {
    "name": name,
    "stock_info": stockInfo,
    "news_info": newsInfo,
    "weather_info": weatherInfo,
    "sports_info": sportsInfo
    }
    
    try:
        response = sg.client.mail.send.post(request_body=request_body)
    except TypeError:
        print(TypeError)
        print("Error sending Email")
        print(response)
    except Exception:
        print(Exception)
        print("Error sending Email")
        print(response)

    if __name__ == "__main__":
        print(request_body)
        print(response.status_code)
        print(response.body)
        print(response.headers)

def send_text(number, message):

    #config nescesary env variables
    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
    TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
    SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
    #RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")

    # AUTHENTICATE
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    #COMPILE REQUEST PARAMETERS (PREPARE THE MESSAGE)
    send_text = number
    content = message

    try:
        # ISSUE REQUEST (SEND SMS)
        message = client.messages.create(to=send_text, from_=SENDER_SMS, body=content)
    except Exception:
        print(Exception)
        print("Error sending Text")
        print(message)
    
def send_tweet (twitterHandle, message):

    #config nescesary env variables
    CONSUMER_KEY = os.environ.get("TWITTER_API_KEY")
    CONSUMER_SECRET = os.environ.get("TWITTER_API_SECRET")
    ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

    # AUTHENTICATE
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    #user = client.me() # get information about the currently authenticated user

    # INITIALIZE API CLIENT
    client = tweepy.API(auth)

    # ISSUE REQUEST(S)
    status = twitterHandle + "\n" + message 
    tempStatus = message

    try:

        if int(len(status)) > 240:
            start = 0
            end = 0
            numberTweets = math.ceil(len(status)/200)
            #breaks tweets up into strings of 200 characters to not exceed tweet character limit
            for x in range(numberTweets):
                status = tempStatus

                start = (x) * 200

                if ((x+1) * 200) > len(status):
                    end = int(len(status))
                else:
                    end = (x+1) * 200
                status= status[start:end] + "\nTweet " + str(x + 1) + "/" + str(numberTweets)
                response = client.update_status(status=status)
        else:
            response = client.update_status(status=status)
    except tweepy.error.TweepError:
        print("Already been posted")
    except Exception:
        print(Exception)
        print("Error posting Tweet")
        print(response)



