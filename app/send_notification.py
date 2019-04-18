# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/sendgrid.md

#import json
#import requests
#import datetime
#import statistics

from source.Alpha import GetStockInfo
from spreadsheet import get_products
from message_sender import send_email, send_text, send_tweet

#Retrieves user information from google sheet and reads into list of dictionaries
headers, contactList = get_products()

for contact in contactList:

    if contact["How would you like to be contacted?"] == "Email":

        #TODO: Change this requirement to allow for input of different APIs for each method
        if contact["What Stock Ticker Would you Like Information On?"] != "":
            contact_email = contact["Email"]
            stockTicker = contact["What Stock Ticker Would you Like Information On?"]
            message_text = GetStockInfo(stockTicker)

            #passes along relevant information to be sent
            send_email(contact_email, message_text)

    elif contact["How would you like to be contacted?"] == "Text":

        if contact["What Stock Ticker Would you Like Information On?"] != "":
            number = "+" + str(contact["Phone number"])
            stock = contact["What Stock Ticker Would you Like Information On?"]
            content = GetStockInfo(stock)
        
            #passes along relevant information to be sent
            send_text(number, content)
    
    elif contact["How would you like to be contacted?"] == "Twitter":

        if contact["What Stock Ticker Would you Like Information On?"] != "":
            stock = contact["What Stock Ticker Would you Like Information On?"]
            message = "@" + str(contact["Twitter"]) + " \n" + GetStockInfo(stock) 
            
            #passes along relevant information to be sent
            send_tweet(message)

if __name__ == "__main__":
    print("headers:", headers)
    print("\n\nContacts:", contactList)

