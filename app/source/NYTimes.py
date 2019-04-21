import os
from dotenv import load_dotenv
import json
import requests


def GetNYTArticles(ArticleNum = 0, email = 0):

        if ArticleNum == 0:
                if email == 1:
                        message_text = "Top NY Times articles for today:<br>"
                else:
                        message_text = "\nTop NY Times articles for today:\n"    

        load_dotenv()

        API_KEY = os.environ.get("NYTIMES_API_KEY")

        # AUTHENTICATE

        #stockTicker = ChosenStockTicker

        request_url = "https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={}".format( API_KEY)
        #parses this data from json to dict
        response = requests.get(request_url)
        parsed_response = json.loads(response.text)


        index = ArticleNum + 1
        if email == 1:
                message_text = message_text + str(index) + ": " + parsed_response["results"][ArticleNum]["abstract"] + "<br>URL:" + parsed_response["results"][ArticleNum]["url"] + "<br>"
        else:
                message_text = message_text + str(index) + ": " + parsed_response["results"][ArticleNum]["abstract"] + "\nURL:" + parsed_response["results"][ArticleNum]["url"] + "\n"
        if __name__ == "__main__":
            
                print(type(parsed_response))
                print(parsed_response.keys())
                x = 1

                for result in parsed_response["results"]:
                        #print(x, ": ", result.keys())
                        if x <= 3:
                                print(x, ": ", result["url"])
                                print(result["abstract"])
                        x = x + 1
                        #print(parsed_response)

        return message_text
        

if __name__ == "__main__":
    GetNYTArticles()
