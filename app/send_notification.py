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

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
# AUTHENTICATE
stockTicker = "AMZN"

sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

# COMPILE REQUEST PARAMETERS (PREPARE THE EMAIL)

from_email = Email(MY_EMAIL_ADDRESS)
to_email = Email(MY_EMAIL_ADDRESS)
subject = "Stock Update"
message_text = ""

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

#Gets date into readable datetime format
newestDate = datetime.datetime.fromisoformat(days[0])
dataTime = "Latest data from: " + str(newestDate.strftime("%B")) + " " + str(newestDate.day) + ", " + str(newestDate.year)

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

message_text = message_text.join([dataTime, ClosePrice, High, Low])
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