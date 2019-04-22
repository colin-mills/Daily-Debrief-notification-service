#https://developer.sportradar.com

import os
from dotenv import load_dotenv
import json
import requests
import datetime

def getSportsInfo(sportLeague, email = 0):

    message_text = ""
    sport = sportLeague
    load_dotenv()

    Date = datetime.datetime.now()

    print(Date.year)

    #API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")
    MLB_API = os.environ.get("MLB_API_KEY")
    NBA_API = os.environ.get("NBA_API_KEY")
    NHL_API = os.environ.get("NHL_API_KEY")

    if sport == "NFL":

        if Date.month > 2 and Date.month < 9:
            NFL_Season = str(int(Date.year) - 1)
        else:
            NFL_Season = str(Date.year)

        #print(NFL_Season)
        NFL_API = os.environ.get("NFL_API_KEY")
        request_url = "http://api.sportradar.us/nfl-t1/teams/{}/rankings.json?api_key={}".format(NFL_Season,NFL_API)
        #print(request_url)
        response = requests.get(request_url)
        print(response)

        parsed_response = json.loads(response.text)

        #(['season', 'type', 'conferences']
        #print("\nseason: ", parsed_response["season"])
        #print("\ntype: ", parsed_response["type"])
        #print("\nconferences: ",type(parsed_response["conferences"]))

        for conference in parsed_response["conferences"]:
            #print(teams["divisions"]) #["name"] , teams["divisions"]["rank"]["conference"], teams["divisions"]["rank"]["conference"])
            message_text = message_text + conference["name"] + ": \n"
            for division in conference["divisions"]:
                #print(division["name"], ": ")
                message_text =  message_text + "The number one team in the " + division["name"] + " is the " + division["teams"][0]["name"] + " (conference: " + str(division["teams"][0]["rank"]["conference"]) + ")\n"

        print(message_text)
    

    



    #request_url = "api.openweathermap.org/data/2.5/forecast/daily?zip={},{}&appid={}".format(zipCode,country,API_KEY)
    ##https://samples.openweathermap.org/data/2.5/forecast/daily?id=524901&appid=b1b15e88fa797225412429c1c50c122a1
    ##parses this data from json to dict
    #response = requests.get(request_url)
    #print(response)
    #parsed_response = json.loads(response.text)
#
    #print(parsed_response)

if __name__ == "__main__":
    getSportsInfo("NFL")