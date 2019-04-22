# Help from:
# ... https://developers.google.com/sheets/api/guides/authorizing
# ... https://gspread.readthedocs.io/en/latest/oauth2.html
# ... https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# ... https://github.com/s2t2/birthday-wishes-py/blob/master/app/sheets.py
# ... https://github.com/prof-rossetti/georgetown-opim-243-201901


import json
import os
from dotenv import load_dotenv
import gspread 
from gspread.exceptions import SpreadsheetNotFound 
from oauth2client.service_account import ServiceAccountCredentials


load_dotenv()

DOCUMENT_KEY = os.environ.get("GOOGLE_SHEET_ID", "OOPS Please get the spreadsheet identifier from its URL")
SHEET_NAME = "Form Responses 5"

#CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "client_secret.json")
GOOGLE_API_CREDENTIALS = os.environ.get("GOOGLE_API_CREDENTIALS")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

def get_products():
    try:
        #credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
        credentials = ServiceAccountCredentials._from_parsed_json_keyfile(json.loads(GOOGLE_API_CREDENTIALS), AUTH_SCOPE)
        client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>
        doc = client.open_by_key(DOCUMENT_KEY) #> <class 'gspread.models.Spreadsheet'>
        sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>
        rows = sheet.get_all_records() #> <class 'list'>
    except TypeError:
        print(TypeError)
        rows = sheet = []
    except Exception:
        print(Exception)
        rows = sheet = []
    return sheet, rows #sheet 


if __name__ == "__main__":
    sheet, rows = get_products()

    for row in rows:
        print(row) #> <class 'dict'>

