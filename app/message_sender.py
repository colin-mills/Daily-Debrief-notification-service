import os
from dotenv import load_dotenv

#Used for sending email through sendgrid
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.
from sendgrid import SendGridAPIClient

#used for sending texts
import twilio
from twilio.rest import Client

#used for tweeting 
import tweepy

def send_email(email, message):
    send_email = email #contact["Email"]
            
    load_dotenv()
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
    MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
    
    # AUTHENTICATE
    #stockTicker = contact["What Stock Ticker Would you Like Information On?"]

    #sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)

    ## COMPILE REQUEST PARAMETERS (PREPARE THE EMAIL)
    from_email = Email(MY_EMAIL_ADDRESS)
    to_email = Email(send_email)
    subject = "Stock Update"
    message_text = message

    #print(message_text)
    content = Content("text/plain", message_text)
    mail = Mail(from_email, subject, to_email, content)

    # ISSUE REQUEST (SEND EMAIL)
    response = sg.client.mail.send.post(request_body=mail.get())
    #response = sg.client.mail.send.post(mail.get())

def send_text(number, message):

    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
    TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
    SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
    #RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")

    # AUTHENTICATE
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # COMPILE REQUEST PARAMETERS (PREPARE THE MESSAGE)
    send_text = number
    content = message

    # ISSUE REQUEST (SEND SMS)
    message = client.messages.create(to=send_text, from_=SENDER_SMS, body=content)

def send_tweet (message):

    CONSUMER_KEY = os.environ.get("TWITTER_API_KEY")
    CONSUMER_SECRET = os.environ.get("TWITTER_API_SECRET")
    ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

    # AUTHENTICATE

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # INITIALIZE API CLIENT

    client = tweepy.API(auth)

    # ISSUE REQUEST(S)

    user = client.me() # get information about the currently authenticated user

    status = message 
    tempStatus = message

    try:

        if int(len(status)) > 240:
            start = 0
            end = 0
            numberTweets = math.ceil(len(status)/200)
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



