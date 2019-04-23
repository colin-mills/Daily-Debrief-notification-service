import os
from dotenv import load_dotenv
import json
import requests

def getWeatherInfo(zip, email = 0):

    try:
        message_text = ""
        load_dotenv()

        API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")
        zipCode = zip

        request_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}&units=imperial".format(zipCode,API_KEY)

        response = requests.get(request_url)

        #parses this data from json to dict
        parsed_response = json.loads(response.text)
        city = str(parsed_response["name"])

        #appropriate line breaks for each type of messasge
        if email == 1:
            message_text = message_text + "City: " + city + "<br>"
            message_text = message_text + "Temperature: " + str(parsed_response["main"]["temp"]) + " degrees fahrenheit <br>"
            message_text = message_text + "Wind speed: " + str(parsed_response["wind"]["speed"]) + " MPH <br>"
            message_text = message_text + "Cloud coverage: " + str(parsed_response["clouds"]["all"]) + "%<br>"
            message_text = message_text + "Description: " + parsed_response["weather"][0]["description"] + "<br>"
        else:
            message_text = "Daily weather report: \n"
            message_text = message_text + "City: " + city + "\n"
            message_text = message_text + "Temperature: " + str(parsed_response["main"]["temp"]) + " degrees fahrenheit \n"
            message_text = message_text + "Wind speed: " + str(parsed_response["wind"]["speed"]) + " MPH \n"
            message_text = message_text + "Cloud coverage: " + str(parsed_response["clouds"]["all"]) + "%\n"
            message_text = message_text + "Description: " + parsed_response["weather"][0]["description"] + "\n"


    except KeyError as key:
        print(KeyError)
        message_text = "Sorry we can't gather weather information at this moment"
        print("Error sent from OpenWeatherMap.py")
        print(message_text)
        print(key.__cause__)
    except Exception as e:
        print(Exception)
        message_text = "Something unexpected went wrong while gathering weather information."
        print("Error sent from OpenWeatherMap.py")
        print(message_text)
        print(e.__cause__)
    return message_text

#testing
if __name__ == "__main__":
    weather = getWeatherInfo("20057")
    print(weather)