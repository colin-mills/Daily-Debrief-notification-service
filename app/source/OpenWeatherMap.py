import os
from dotenv import load_dotenv
import json
import requests

def getWeatherInfo(zip, country):

    message_text = ""
    load_dotenv()

    API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")
    # AUTHENTICATE
    zipCode = zip

    request_url = "api.openweathermap.org/data/2.5/forecast/daily?zip={},{}&appid={}".format(zipCode,country,API_KEY)
    #https://samples.openweathermap.org/data/2.5/forecast/daily?id=524901&appid=b1b15e88fa797225412429c1c50c122a1
    #parses this data from json to dict
    response = requests.get(request_url)
    print(response)
    parsed_response = json.loads(response.text)

    print(parsed_response)
    
if __name__ == "__main__":
    getWeatherInfo("20057", "us")