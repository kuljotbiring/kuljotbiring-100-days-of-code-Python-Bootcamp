import requests
from datetime import datetime

MY_LAT = 38.637241
MY_LONG = -121.512604

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# get the sunrise and sunset from the API and then just grab the first hour using split and list indices
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

# use date time to get the current time
time_now = datetime.now()

# only get the hour from datetime current time
print(time_now.hour)
