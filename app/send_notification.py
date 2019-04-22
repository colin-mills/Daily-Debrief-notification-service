from source.Alpha import GetStockInfo
from source.NYTimes import GetNYTArticles
from source.OpenWeatherMap import getWeatherInfo
from source.SportRadar import getSportsInfo
from spreadsheet import get_products
from message_sender import send_email, send_text, send_tweet

#Retrieves user information from google sheet and reads into list of dictionaries
headers, contactList = get_products()
if contactList == "":
    print("ERROR: Contact List is empty, either there is an unexpected error or the spreadsheet is empty.")
else:
    for contact in contactList:

        if contact["How would you like to be contacted?"] == "Email":
            name = contact["Name"]
            contact_email = contact["Email"]

            #Default for messages that are added to themselves
            newsInfo = ""
            stockInfo = ""
            
            if contact["Would you like stock information?"] == "Yes":
                for stock in range(int(contact["Number of stocks"])):
                    stockTicker = contact["Stock " + str(stock + 1)]
                    stockInfo = stockInfo + GetStockInfo(stockTicker, 1) + "<br>"
            else:
                stockInfo = "No stock information chosen"
            
            if contact["Would you like news information?"] == "Yes":
                for article in range(int(contact["How many articles would you like to see?"])):
                    newsInfo = newsInfo + GetNYTArticles(article, email=1, tweet=0)
            else:
                newsInfo = "No news information chosen"

            if contact["Would you like weather information?"] == "Yes":
                zipCode = contact["Zip code"]
                weatherInfo = getWeatherInfo(zipCode, email=1)
            else:
                weatherInfo = "No weather information chosen"

            if contact["Would you like sports information?"] == "Yes":
                sport = contact["Which sport would you like updates on?"]
                sportsInfo = getSportsInfo(sport, email=1)
            else:
                sportsInfo = "No sports information chosen"

            send_email(name, contact_email, stockInfo, newsInfo, weatherInfo, sportsInfo)

        elif contact["How would you like to be contacted?"] == "Text":
            number = "+" + str(contact["Phone number"])
            content = ""

            #Default for messages that are added to themselves
            newsInfo = ""
            stockInfo = ""

            if contact["Would you like weather information?"] == "Yes":
                zipCode = contact["Zip code"]
                weatherInfo = getWeatherInfo(zipCode)
                send_text(number, weatherInfo)
            
            if contact["Would you like news information?"] == "Yes":
                for article in range(int(contact["How many articles would you like to see?"])):
                    newsInfo = newsInfo + GetNYTArticles(article, email=0 , tweet=0)
                send_text(number, newsInfo)

            if contact["Would you like stock information?"] == "Yes":
                for stock in range(int(contact["Number of stocks"])):
                    stockTicker = contact["Stock " + str(stock + 1)]
                    stockInfo = stockInfo + GetStockInfo(stockTicker) + "\n"
                send_text(number, stockInfo)

            if contact["Would you like sports information?"] == "Yes":
                sport = contact["Which sport would you like updates on?"]
                sportsInfo = getSportsInfo(sport)
                send_text(number, sportsInfo)
        
        elif contact["How would you like to be contacted?"] == "Twitter":
            Handle = "@" + str(contact["Twitter"])

            if contact["Would you like weather information?"] == "Yes":
                zipCode = contact["Zip code"]
                weatherInfo = getWeatherInfo(zipCode)
                send_tweet(Handle, weatherInfo)

            if contact["Would you like news information?"] == "Yes":
                for article in range(int(contact["How many articles would you like to see?"])):
                    newsInfo = GetNYTArticles(article, email=0, tweet=1)
                    send_tweet(Handle, newsInfo)

            if contact["Would you like stock information?"] == "Yes":
                for stock in range(int(contact["Number of stocks"])):
                    stockTicker = contact["Stock " + str(stock + 1)]
                    stockInfo =  GetStockInfo(stockTicker)
                    send_tweet(Handle, stockInfo)

            if contact["Would you like sports information?"] == "Yes":
                sport = contact["Which sport would you like updates on?"]
                sportsInfo = getSportsInfo(sport)
                send_tweet(Handle, sportsInfo)

if __name__ == "__main__":
    print("headers:", headers)
    print("\n\nContacts:", contactList)

