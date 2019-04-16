# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/sendgrid.md
import os
import pprint
import tweepy


from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.
from twilio.rest import Client

import json
import requests
import datetime
import statistics

from source.Alpha import GetStockInfo
from spreadsheet import get_products, create_product

headers, contactList = get_products()

for contact in contactList:

    if contact["How would you like to be contacted?"] == "Email":

        if contact["What Stock Ticker Would you Like Information On?"] != "":
            send_email = contact["Email"]
            print (send_email)
            load_dotenv()

            SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
            MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

            API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
            # AUTHENTICATE
            stockTicker = contact["What Stock Ticker Would you Like Information On?"]


            sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

            # COMPILE REQUEST PARAMETERS (PREPARE THE EMAIL)

            from_email = Email(MY_EMAIL_ADDRESS)
            to_email = Email(send_email)
            subject = "Stock Update"
            message_text = GetStockInfo(stockTicker)

            print(message_text)
            content = Content("text/plain", message_text)
            mail = Mail(from_email, subject, to_email, content)

            # ISSUE REQUEST (SEND EMAIL)

            response = sg.client.mail.send.post(request_body=mail.get())

            # PARSE RESPONSE

            pp = pprint.PrettyPrinter(indent=4)


    elif contact["How would you like to be contacted?"] == "Text":

        if contact["What Stock Ticker Would you Like Information On?"] != "":
            send_text = "+" + str(contact["Phone Number"])
            stock = contact["What Stock Ticker Would you Like Information On?"]
        
            TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
            TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
            SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
            RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")

            # AUTHENTICATE

            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

            # COMPILE REQUEST PARAMETERS (PREPARE THE MESSAGE)

            content = GetStockInfo(stock)

            # ISSUE REQUEST (SEND SMS)

            message = client.messages.create(to=send_text, from_=SENDER_SMS, body=content)

            # PARSE RESPONSE

            pp = pprint.PrettyPrinter(indent=4)
    
   
    elif contact["How would you like to be contacted?"] == "Twitter":

        if contact["What Stock Ticker Would you Like Information On?"] != "":
            stock = contact["What Stock Ticker Would you Like Information On?"]
            send_tweet = "@" + str(contact["Twitter"]) + " \n" + GetStockInfo(stock) 

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

            time_now = datetime.datetime.now() # a way for us to implement status uniqueness to avoid subsequent tweets running into ... tweepy.error.TweepError: [{'code': 187, 'message': 'Status is a duplicate.'}]
            time_now_formatted = str(time_now) #> '2019-03-13 16:41:26.282159'
            #status = "My first tweet sent from https://github.com/colin-mills at {}".format(time_now_formatted)
            status = send_tweet 
            response = client.update_status(status=status)

            # PARSE RESPONSES

            pp = pprint.PrettyPrinter(indent=4)
