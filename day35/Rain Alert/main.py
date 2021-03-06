import requests
import os
from twilio.rest import Client

"""
To create an environment variable, go to the terminal and type:
export NAME_OF_KEY=KeyThatYouWantToSave
press enter

import the os module

to access the key in the code set it to a variable like so:
api_key = os.environ.get("NAME_OF_KEY")
"""

api_key = os.environ.get("OWM_API_KEY")

account_sid = "ENTER YOU ACCOUNT SID HERE"
auth_token = os.environ.get("AUTH_TOKEN")

LAT = 38.676998
LONG = -121.527946

parameters = {
    "lat": LAT,
    "lon": LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

response.raise_for_status()

data = response.json()

# place the first 12 results for the hours into a list
weather_slice = data["hourly"][:12]

will_rain = False

# loop through the list
for hour in weather_slice:
    # using id from API to determine if rain or snow
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# check if any of those times it is raining and inform user
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+15017122661',
        to='+15558675310'
)


