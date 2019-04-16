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
SHEET_NAME = "Form Responses 1"

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "client_secret.json")
#GOOGLE_API_CREDENTIALS = os.environ.get("GOOGLE_API_CREDENTIALS")
AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

def get_products():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
    #credentials = ServiceAccountCredentials._from_parsed_json_keyfile(json.loads(GOOGLE_API_CREDENTIALS), AUTH_SCOPE)
    client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>
    #print("GETTING PRODUCTS FROM THE SPREADSHEET...")
    doc = client.open_by_key(DOCUMENT_KEY) #> <class 'gspread.models.Spreadsheet'>
    sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>
    rows = sheet.get_all_records() #> <class 'list'>
    return sheet, rows #sheet 

# example product_attributes: {'name': 'Product CLI', 'department': 'snacks', 'price': 4.99, 'availability_date': '2019-01-01'}
def create_product(product_attributes, sheet=None, products=None):
    if not (sheet and products):
        #print("OH, PREFER TO PASS PREVIOUSLY-OBTAINED SHEET AND PRODUCTS, FOR FASTER PERFORMANCE!")
        sheet, products = get_products()

    print(f"DETECTED {len(products)} EXISTING CONTACTS")
    print("NEW PRODUCT ATTRIBUTES:", product_attributes)
    next_id = len(products) + 1 # number of records, plus one. TODO: max of current ids, plus one
    contact = {
        "email": "cgm71@georgetown.edu",
        "Stock": "AAPL",
    }
    next_row = list(contact.values()) #> [13, 'Product CLI', 'snacks', 4.99, '2019-01-01']
    next_row_number = len(products) + 2 # number of records, plus a header row, plus one

    response = sheet.insert_row(next_row, next_row_number)
    return response

if __name__ == "__main__":
    sheet, rows = get_products()

    for row in rows:
        print(row) #> <class 'dict'>

