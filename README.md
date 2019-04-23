# Daily-Debrief-notification-service

## Intructions to use service as a user

1. Fill out google form found at https://forms.gle/1i3dyhMygPTP1VNu7

2. Wait until 8AM EST and receive your personalized news update!

* If you wish to unsubcscribe send an email to cgm71@georgetown with your name you used on the google form

## Intructions to create this service as a provider

### Setup

1. Clone or download this repository into a local directory 

2. Create a developer account for these follwing websites and record the provided API keys
  * https://developer.nytimes.com
  * https://openweathermap.org/api
  * https://developer.sportradar.com
    * Select apis for NFL Classic Trial, MLB Trial v6, NHL Official Trial, and NBA Trial
  * https://www.alphavantage.co
  * https://developer.twitter.com/en/docs.html
  * https://www.twilio.com
  * https://sendgrid.com
  * Follow instructions to create working google development sheet at: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html 
    * Ensure the client_secret.json file is in your root directory
    
3. Make a linked google form by following this link https://docs.google.com/forms/d/1C19R3RZLThIrF_-gaqKUbxOXsmQxUxhFz8-jmfILAmQ/edit?usp=sharing and copying it into your own drive. Select "link answers to existing spreadsheet" and select the spreadsheet you just made.

4. Make a Heroku account at https://signup.heroku.com/login 
### Intructions
1. Create or activate enironment were you can manage packages from
   * If using Anaconda as your language version manager 
   ```
   conda create -n yourenvname python=3.7
   ```

2. Ensure that your python is working in version 3.7
   ```
   python --version
   ```
3. Install all required packages
   ```
   pip install requirements.txt
   ```

4. create a .env file in your root directory for your environment variables and model it as thus with your own API keys:

 **ALPHA Vantage API Key**
 ```
 ALPHAVANTAGE_API_KEY="Key"
```
 **NY Times API Key**
 ```
 NYTIMES_API_KEY="Key"
 NYTIMES_SECRET="SecretKey"
```
 **Open Weather API**
 ```
 OPEN_WEATHER_API_KEY="Key"
```
 **Sports Radar**
 ```
 MLB_API_KEY="MLBKey"
 NBA_API_KEY="NBAKey"
 NFL_API_KEY="NFLKey"
 NHL_API_KEY="NHLKey"
```
 **for email capabilities**
 ```
 SENDGRID_API_KEY="Key" 
 MY_EMAIL_ADDRESS="Email" # use the email address you associated with the SendGrid service
```
 **for SMS capabilities**
 ```
 TWILIO_ACCOUNT_SID="Key"
 TWILIO_AUTH_TOKEN="Token"
 SENDER_SMS="TwilioNumber"
```
 **for tweeting capabilities**
 ```
 TWITTER_API_KEY="Key"
 TWITTER_API_SECRET="SecretKey"
 TWITTER_ACCESS_TOKEN="Token"
 TWITTER_ACCESS_TOKEN_SECRET="SecretToken"
```
 **GOOGLE Sheets credential**
 ```
 GOOGLE_SHEET_ID="Google Seet ID"
 SHEET_NAME="name of sheet with user information"
 ```
 5. Save and commit all changes and test working functionality from command line
 ```
 pytest
 ```

### Deployment

#### Heroku Command Line

If you have not used Heroku before go to https://devcenter.heroku.com/articles/heroku-cli#download-and-install to install comand line functionality

You can test if it is working by issuing these commands from the command line
```
heroku login

heroku apps:list
```

#### App Server Creation

Create a remote Heroku server:
```
heroku apps:create name-of-app
```

Go to the Heroku online dashboard and find the app's "heroku git url" and subsequently associate this with your git repository: 
```
git remote add heroku REMOTE_ADDRESS 
```
Ensure this step worked by issuing
```
git remote -v
```
#### Heroku Environment Configuration

1. Configure the entire json file "client_secret.json" as an environment variable
```
heroku config:set GOOGLE_API_CREDENTIALS="$(< /client_secret.json)" 
```
2. In spreadsheet.py change 
```python
server = False
```
To
```python
server = True
```
2.For each environment variable in your .env issue a respective heroku command such as
```
heroku config:set ALPHAVANTAGE_API_KEY="Key"
```
#### Deploy

```
git push heroku master
```

Once deployed you will need to activate the heroku scheduler to run this command everyday at your desired time.
```
python app/send_notification.py
```

### Continous Integration Testing
To enable continous integration to run on each updated commit you will need to navigate to https://travis-ci.com and go to the settings of your repository and configure each of these environment variables once more.
