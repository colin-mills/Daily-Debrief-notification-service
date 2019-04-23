# Daily-Debrief-notification-service

## Intructions to use service as a user

1. Fill out google form found at https://forms.gle/1i3dyhMygPTP1VNu7

2. Wait until 8AM EST and receive your personalized news update!

## Intructions to create this service as a provider

### Setup

* Ensure that your python is working in version 3.7
```
python --version
```

* Clone or download this repository into a local directory 

* Create a developer account for these follwing websites and record the provided API keys
  * https://developer.nytimes.com
  * https://openweathermap.org/api
  * https://developer.sportradar.com
    * Select apis for NFL Classic Trial, MLB Trial v6, NHL Official Trial, and NBA Trial
  * https://www.alphavantage.co
  * https://developer.twitter.com/en/docs.html
  * https://www.twilio.com
  * https://sendgrid.com
  * Follow instructions to create working google development sheet at: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html 

### Intructions

### Deployment

#### Heroku Command Line

#### Heroku Environment Configuration

#### Deploy

```
python app/send_notification.py
```
