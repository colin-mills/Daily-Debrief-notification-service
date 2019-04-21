# adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/sendgrid.md
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

        #Default for messages that are added to themselves
        newsInfo = ""
        stockInfo = ""
        
        if contact["Would you like stock information?"] == "Yes":
            for stock in range(int(contact["How many stocks would you like?"])):
                stockTicker = contact["Stock " + str(stock + 1)]
                stockInfo = stockInfo + "<br>" + GetStockInfo(stockTicker, 1)
        else:
            stockInfo = "No stock information chosen"
        
        if contact["Would you like news information?"] == "Yes":
            for article in range(int(contact["How many articles would you like to see?"])):
                newsInfo = newsInfo + GetNYTArticles(article, 1)
        else:
            newsInfo = "No news information chosen"

        if contact["Would you like weather information?"] == "Yes":
            weatherInfo = "weather info in here"
        else:
            weatherInfo = "No weather information chosen"

        if contact["Would you like sports information?"] == "Yes":
            sportsInfo = "sports info in here"
        else:
            sportsInfo = "No sports information chosen"

        if contact["Would you like music information?"] == "Yes":
            musicInfo = "music info in here"
        else:
            musicInfo = "No music information chosen"

        #send_email(name, contact_email, stockInfo, newsInfo, weatherInfo, sportsInfo, musicInfo)

    elif contact["How would you like to be contacted?"] == "Text":
        number = "+" + str(contact["Phone number"])
        content = ""

        #Default for messages that are added to themselves
        newsInfo = ""
        stockInfo = ""

        if contact["Would you like weather information?"] == "Yes":
            weatherInfo = "weather info in here"
            #send_text(number, weatherInfo)
        
        if contact["Would you like news information?"] == "Yes":
            for article in range(int(contact["How many articles would you like to see?"])):
                newsInfo = newsInfo + GetNYTArticles(article, email=0 , tweet=0)
            send_text(number, newsInfo)

        if contact["Would you like stock information?"] == "Yes":
             for stock in range(int(contact["How many stocks would you like?"])):
                stockTicker = contact["Stock " + str(stock + 1)]
                stockInfo = stockInfo + GetStockInfo(stockTicker)
             #send_text(number, stockInfo)

        if contact["Would you like sports information?"] == "Yes":
            sportsInfo = "sports info in here"
            #send_text(number, sportsInfo)
        if contact["Would you like music information?"] == "Yes":
            musicInfo = "music info in here"
            #send_text(number, musicInfo)
    
    elif contact["How would you like to be contacted?"] != "Twitter":
        Handle = "@" + str(contact["Twitter"])

        if contact["Would you like weather information?"] == "Yes":
            weatherInfo = "weather info in here"
            #send_tweet(Handle, weatherInfo)

        if contact["Would you like news information?"] == "Yes":
            for article in range(int(contact["How many articles would you like to see?"])):
                newsInfo = GetNYTArticles(article, email=0, tweet=1)
                send_tweet(Handle, newsInfo)

        if contact["Would you like stock information?"] == "Yes":
             for stock in range(int(contact["How many stocks would you like?"])):
                stockTicker = contact["Stock " + str(stock + 1)]
                stockInfo =  GetStockInfo(stockTicker)
                send_tweet(Handle, stockInfo)

        if contact["Would you like sports information?"] == "Yes":
            sportsInfo ="sports info in here"
            #send_tweet(Handle, sportsInfo)

        if contact["Would you like music information?"] == "Yes":
            musicInfo = "music info in here"
            #send_tweet(Handle, musicInfo)

if __name__ == "__main__":
    print("headers:", headers)
    print("\n\nContacts:", contactList)

