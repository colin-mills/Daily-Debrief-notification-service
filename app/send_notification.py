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
        if contact["Would you like stock information?"] == "Yes":
            contact_email = contact["Email"]
            stockTicker = contact["Stock Ticker"]
            stockInfo = GetStockInfo(stockTicker, 1)
            name = contact["Name"]

            #passes along relevant information to be sent
            send_email(name, contact_email) #, stockInfo)

    elif contact["How would you like to be contacted?"] == "Text":

        if contact["Would you like stock information?"] == "Yes":
            number = "+" + str(contact["Phone number"])
            stock = contact["Stock Ticker"]
            content = GetStockInfo(stock)
        
            #passes along relevant information to be sent
            send_text(number, content)
    
    elif contact["How would you like to be contacted?"] == "Twitter":

        if contact["Would you like stock information?"] == "Yes":
            stock = contact["Stock Ticker"]
            message = "@" + str(contact["Twitter"]) + " \n" + GetStockInfo(stock) 
            
            #passes along relevant information to be sent
            send_tweet(message)

if __name__ == "__main__":
    print("headers:", headers)
    print("\n\nContacts:", contactList)

