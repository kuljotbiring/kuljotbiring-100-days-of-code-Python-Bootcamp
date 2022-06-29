import requests

api_key = "5e4df6c859886cfda134264deb296af3"

LAT = 38.676998
LONG = -121.527946

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

response.raise_for_status()

data = response.json()

print(data)




