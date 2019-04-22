import os
from dotenv import load_dotenv
import json
import requests
import datetime
import statistics

def GetStockInfo(ChosenStockTicker, email = 0):
    try:
            
        message_text = ""
        load_dotenv()

        API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
        # AUTHENTICATE
        stockTicker = ChosenStockTicker

        request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}".format(stockTicker, API_KEY)
        #parses this data from json to dict
        response = requests.get(request_url)
        parsed_response = json.loads(response.text)

        #The Time Series (Daily) dict of the larger dict
        tsd = parsed_response["Time Series (Daily)"] #> 'dict'

        #Gets list of all keys in tsd (days) and converts to list  
        day_keys = tsd.keys() #> 'dict_keys' of all the day values
        days = list(day_keys) #> 'list' of all the day values


        timeStamps = []
        opens = []
        highs = []
        lows = []
        closes = []
        volumes = []

        #Loops through all stocks to append to previous lists 
        for date in days:
            timeStamps.append(date)
            opens.append(tsd[date]["1. open"])
            highs.append(float(tsd[date]["2. high"]))
            lows.append(float(tsd[date]["3. low"]))
            closes.append(tsd[date]["4. close"])
            volumes.append(tsd[date]["5. volume"])

        

        if email == 1:
            #Lists name
            stock = "<br>Stock: " + ChosenStockTicker
            #Gets date into readable datetime format
            newestDate = datetime.datetime.today() #fromisoformat(days[0])
            dataTime = "<br>Latest data from: " + str(newestDate.month) + "/" + str(newestDate.day) + "/" + str(newestDate.year)

            #Statistics help from: https://docs.python.org/3/library/statistics.html 

            #Closing stock price
            closingStock = tsd[days[0]]["4. close"]
            closingStock_USD = "${0:,.2f}".format(float(closingStock))
            ClosePrice = "<br>The latest closing price is: ".ljust(35) + closingStock_USD.rjust(10)

            #recent average high
            recentHigh = max(highs)
            recentHigh_USD = "${0:,.2f}".format(recentHigh)
            High = "<br>The recent high price is: ".ljust(35) + recentHigh_USD.rjust(10)

            #recent average low
            recentLow = min(lows)
            recentLow_USD = "${0:,.2f}".format(recentLow)
            Low = "<br>The recent low price is: ".ljust(35) + recentLow_USD.rjust(10)
        else:
            #Lists name
            stock = "\nStock: " + ChosenStockTicker
            #Gets date into readable datetime format
            newestDate = datetime.datetime.today() #fromisoformat(days[0])
            dataTime = "\nLatest data from: " + str(newestDate.month) + "/" + str(newestDate.day) + "/" + str(newestDate.year)

            #Statistics help from: https://docs.python.org/3/library/statistics.html 

            #Closing stock price
            closingStock = tsd[days[0]]["4. close"]
            closingStock_USD = "${0:,.2f}".format(float(closingStock))
            ClosePrice = "\nThe latest closing price is: ".ljust(35) + closingStock_USD.rjust(10)

            #recent average high
            recentHigh = max(highs)
            recentHigh_USD = "${0:,.2f}".format(recentHigh)
            High = "\nThe recent high price is: ".ljust(35) + recentHigh_USD.rjust(10)

            #recent average low
            recentLow = min(lows)
            recentLow_USD = "${0:,.2f}".format(recentLow)
            Low = "\nThe recent low price is: ".ljust(35) + recentLow_USD.rjust(10)

        
        message_text = message_text.join([stock, dataTime, ClosePrice, High, Low])
    except requests.exceptions.ConnectionError:
        message_text = "Sorry we can't find any trading data for " + stockTicker + "."
    except KeyError as key:
        message_text = "Sorry we can't find any trading data for " + stockTicker + "."
        print("Error sent from Alpha.py")
        print(message_text)
        print(key.__cause__)
    except Exception as e:
        print(Exception)
        message_text = "Something unexpected went wrong while gathering stock information."
        print("Error sent from Alpha.py")
        print(message_text)
        print(e.__cause__)
    return message_text



