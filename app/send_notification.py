# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/sendgrid.md

#import json
#import requests
#import datetime
#import statistics

from source.Alpha import GetStockInfo
from source.NYTimes import GetNYTArticles
from spreadsheet import get_products
from message_sender import send_email, send_text, send_tweet

#Retrieves user information from google sheet and reads into list of dictionaries
headers, contactList = get_products()

for contact in contactList:

    if contact["How would you like to be contacted?"] == "Email":

        name = contact["Name"]
        contact_email = contact["Email"]
        stockInfo = "No stock information chosen"
        newsInfo = "No news information chosen"
        weatherInfo = "No weather information chosen"
        sportsInfo = "No sports information chosen"
        musicInfo = "No music information chosen"


        #TODO: Change this requirement to allow for input of different APIs for each method
        if contact["Would you like stock information?"] == "Yes":
            stockTicker = contact["Stock Ticker"]
            stockInfo = GetStockInfo(stockTicker, 1)

            #passes along relevant information to be sent
        
        if contact["Would you like news information?"] == "Yes":
            if contact["News"] == "NY Times":
                newsInfo = GetNYTArticles(1)

        if contact["Would you like weather information?"] == "Yes":

        if contact["Would you like sports information?"] == "Yes":

        if contact["Would you like music information?"] == "Yes":

        
        #send_email(name, contact_email, stockInfo, newsInfo, weatherInfo, sportsInfo, musicInfo)

    elif contact["How would you like to be contacted?"] == "Text":
        number = "+" + str(contact["Phone number"])
        content = ""

        if contact["Would you like stock information?"] == "Yes":
            stock = contact["Stock Ticker"]
            content = content + GetStockInfo(stock)
        
        if contact["Would you like news information?"] == "Yes":
            if contact["News"] == "NY Times":
                content = content + GetNYTArticles()

        #passes along relevant information to be sent
        send_text(number, content)
    
    elif contact["How would you like to be contacted?"] == "Twitter":
        message = "@" + str(contact["Twitter"]) + " \n"

        if contact["Would you like stock information?"] == "Yes":
            stock = contact["Stock Ticker"]
            message = message + GetStockInfo(stock) 

        if contact["Would you like news information?"] == "Yes":
            if contact["News"] == "NY Times":
                message = message + GetNYTArticles()

        
            
        #passes along relevant information to be sent
        send_tweet(message)

if __name__ == "__main__":
    print("headers:", headers)
    print("\n\nContacts:", contactList)

