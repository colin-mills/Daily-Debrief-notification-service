#https://developer.sportradar.com

import os
from dotenv import load_dotenv
import json
import requests
import datetime

def getSportsInfo(sportLeague, email = 0):

    try:

        message_text = ""
        sport = sportLeague
        load_dotenv()

        Date = datetime.datetime.now()

        if sport == "NFL":
            
            #Determines current season
            if Date.month < 9:
                Season = str(int(Date.year) - 1)
            else:
                Season = str(Date.year)

            API_KEY = os.environ.get("NFL_API_KEY")
            request_url = "http://api.sportradar.us/nfl-t1/teams/{}/rankings.json?api_key={}".format(Season,API_KEY)
            
            response = requests.get(request_url)

            #Convert to dictionary
            parsed_response = json.loads(response.text)

            #appropriate line breaks for each type of messasge
            if email == 1:
                message_text = "Rankings for the " + sport + " " + Season + " season: <br>"
                for conference in parsed_response["conferences"]:
                    message_text = message_text + conference["name"] + ": <br>"
                    for division in conference["divisions"]:
                        message_text =  message_text + "The number one team in the " + division["name"] + " is the " + division["teams"][0]["name"] + " (conference: " + str(division["teams"][0]["rank"]["conference"]) + ")<br>"
            else:
                message_text = "Rankings for the " + sport + " " + Season + " season: \n"
                for conference in parsed_response["conferences"]:
                    message_text = message_text + conference["name"] + ": \n"
                    for division in conference["divisions"]:
                        message_text =  message_text + "The number one team in the " + division["name"] + " is the " + division["teams"][0]["name"] + " (conference: " + str(division["teams"][0]["rank"]["conference"]) + ")\n"

        elif sport == "NBA":
            
            #Determines current season
            if Date.month < 10:
                Season = str(int(Date.year) - 1)
            else:
                Season = str(Date.year)


            API_KEY = os.environ.get("NBA_API_KEY")
            request_url = "http://api.sportradar.us/nba/trial/v5/en/seasons/{}/REG/rankings.json?api_key={}".format(Season,API_KEY)

            response = requests.get(request_url)

            #Convert to dictionary
            parsed_response = json.loads(response.text)

            #appropriate line breaks for each type of messasge
            if email == 1:
                message_text = "Rankings for the " + sport + " " + Season + " season: <br>"
                for conference in parsed_response["conferences"]:
                    message_text = message_text + conference["name"] + ": <br>"
                    for division in conference["divisions"]:
                        message_text =  message_text + "The number one team in the " + division["name"] + " is the " + division["teams"][0]["name"] + " (conference: " + str(division["teams"][0]["rank"]["conference"]) + ")<br>"
            else:
                message_text = "Rankings for the " + sport + " " + Season + " season: \n"
                for conference in parsed_response["conferences"]:
                    message_text = message_text + conference["name"] + ": \n"
                    for division in conference["divisions"]:
                        message_text =  message_text + "The number one team in the " + division["name"] + " is the " + division["teams"][0]["name"] + " (conference: " + str(division["teams"][0]["rank"]["conference"]) + ")\n"
                    
        elif sport == "NHL":
            
            #Determines current season
            if Date.month < 10:
                Season = str(int(Date.year) - 1)
            else:
                Season = str(Date.year)

            API_KEY = os.environ.get("NHL_API_KEY")
            request_url = "http://api.sportradar.us/nhl/trial/v6/en/seasons/{}/REG/rankings.json?api_key={}".format(Season,API_KEY)
            response = requests.get(request_url)
           
            #Convert to dictionary
            parsed_response = json.loads(response.text)

            #appropriate line breaks for each type of messasge
            if email == 1:
                message_text = "Rankings for the " + sport + " " + Season + " season: <br>"
                for conference in parsed_response["conferences"]:
                    message_text = message_text + conference["name"] + ": <br>"
                    for division in conference["divisions"]:
                        message_text =  message_text + "The number one team in the " + division["name"] + " is the " + division["teams"][0]["name"] + " (conference: " + str(division["teams"][0]["rank"]["conference"]) + ")<br>"
                        message_text =  message_text + "The number two team in the " + division["name"] + " is the " + division["teams"][1]["name"] + " (conference: " + str(division["teams"][1]["rank"]["conference"]) + ")<br>"
            else:
                message_text = "Rankings for the " + sport + " " + Season + " season: \n"
                for conference in parsed_response["conferences"]:
                    message_text = message_text + conference["name"] + ": \n"
                    for division in conference["divisions"]:
                        message_text =  message_text + "The number one team in the " + division["name"] + " is the " + division["teams"][0]["name"] + " (conference: " + str(division["teams"][0]["rank"]["conference"]) + ")\n"
                        message_text =  message_text + "The number two team in the " + division["name"] + " is the " + division["teams"][1]["name"] + " (conference: " + str(division["teams"][1]["rank"]["conference"]) + ")\n"
        elif sport == "MLB":

            #Determines current season
            if Date.month < 3:
                Season = str(int(Date.year) - 1)
            else:
                Season = str(Date.year)

            API_KEY = os.environ.get("MLB_API_KEY")
            request_url = "http://api.sportradar.us/mlb/trial/v6.5/en/seasons/{}/REG/rankings.json?api_key={}".format(Season,API_KEY)

            #Convert to dictionary
            response = requests.get(request_url)
            parsed_response = json.loads(response.text)

            
            #appropriate line breaks for each type of messasge
            if email == 1:
                message_text = "Rankings for the " + sport + " " + Season + " season: <br>"
                for league in parsed_response["league"]["season"]["leagues"]:
                    message_text = message_text + league["name"] + ": <br>"
                    for division in league["divisions"]:
                        message_text =  message_text + "The number one team in the " + division["name"] + " is the " + division["teams"][0]["name"] + " (league: " + str(division["teams"][0]["rank"]["league"]) + ")<br>"     
            else:
                message_text = "Rankings for the " + sport + " " + Season + " season: \n"
                for league in parsed_response["league"]["season"]["leagues"]:
                    message_text = message_text + league["name"] + ": \n"
                    for division in league["divisions"]:
                        message_text =  message_text + "The number one team in the " + division["name"] + " is the " + division["teams"][0]["name"] + " (league: " + str(division["teams"][0]["rank"]["league"]) + ")\n"     

    except KeyError as key:
        print(KeyError)
        message_text = "Sorry we can't gather sports information at this moment"
        print("Error sent from SportRadar.py")
        print(message_text)
        print(key.__cause__)
    except Exception as e:
        print(Exception)
        message_text = "Something unexpected went wrong while gathering sports information."
        print("Error sent from SportRadar.py")
        print(message_text)
        print(e.__cause__)
    return message_text

#testing
if __name__ == "__main__":
    message = getSportsInfo("NFL")
    print(message)

    message = getSportsInfo("NBA")
    print(message)

    message = getSportsInfo("NHL")
    print(message)

    message = getSportsInfo("MLB")
    print(message)