# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/sendgrid.md
import os
import pprint

from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.

import json
import requests
import datetime
import statistics

from source.Alpha import GetStockInfo
from spreadsheet import get_products, create_product

headers, contactList = get_products()

for contact in contactList:

    print(contactList)

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

        #print("----------------------")
        #print("EMAIL")
        #print("----------------------")
        #print("RESPONSE: ", type(response))
        #print("STATUS:", response.status_code) #> 202 means success
        #print("HEADERS:")
        #pp.pprint(dict(response.headers))
        #print("BODY:")
        #print(response.body) #> this might be empty. it's ok.)