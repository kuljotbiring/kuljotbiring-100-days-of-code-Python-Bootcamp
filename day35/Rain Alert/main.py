import requests

api_key = "5e4df6c859886cfda134264deb296af3"

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
    print("Bring an umbrella")




