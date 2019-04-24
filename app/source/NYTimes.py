import os
from dotenv import load_dotenv
import json
import requests


def GetNYTArticles(ArticleNum = 0, email = 0,tweet = 0):

        try:
                message_text = ""

                #If first message
                if ArticleNum == 0:
                        if email == 1:
                                message_text = "Top NY Times articles for today:<br>"
                        else:
                                message_text = "\nTop NY Times articles for today:"    

                load_dotenv()

                API_KEY = os.environ.get("NYTIMES_API_KEY")

                # AUTHENTICATE

                #stockTicker = ChosenStockTicker

                request_url = "https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={}".format( API_KEY)
                #parses this data from json to dict
                response = requests.get(request_url)
                parsed_response = json.loads(response.text)


                index = ArticleNum + 1
                #Append apropriate message format depending on type of message being sent
                if email == 1:
                        message_text = message_text + str(index) + ": " + parsed_response["results"][ArticleNum]["abstract"] + "<br>URL :" + parsed_response["results"][ArticleNum]["url"] + "<br>"
                elif tweet == 1:
                        message_text = message_text + "\n" + str(index) + ": "  + "URL: " + parsed_response["results"][ArticleNum]["url"] + "\n" + parsed_response["results"][ArticleNum]["abstract"] + "\n"
                else:
                        message_text = message_text + "\n" + str(index) + ": " + parsed_response["results"][ArticleNum]["abstract"] + "\nURL :" + parsed_response["results"][ArticleNum]["url"] + "\n"
                
        
        except KeyError as key:
                print(KeyError)
                message_text = "Sorry we can't gather news information at this moment"
                print("Error sent from NYTimes.py")
                print(message_text)
                print(key.__cause__)
        except Exception as e:
                print(Exception)
                message_text = "Something unexpected went wrong while gathering news information."
                print("Error sent from NYTimes.py")
                print(message_text)
                print(e.__cause__)
        return message_text

#testing
if __name__ == "__main__":
        x=0
        for x in range(5):
                message = GetNYTArticles(x,1,0)
                print(message)
                x = x+1
