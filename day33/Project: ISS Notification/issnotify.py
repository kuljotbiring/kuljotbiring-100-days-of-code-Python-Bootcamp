import requests
from datetime import datetime

# make a get request
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# will print the response code 200 is OK
# response code 404 is not found
# 1XX: Hold On
# 2XX: Good
# 3XX: Do not have permission
# 4XX: Users Errors
# 5XX: Server Errors
print(response)

# you can get details on the response instead of just the response object
print(response.status_code)

# handle errors using the request module to generate the exception
response.raise_for_status()

# once we are sure the request is good we can get a hold of the data returned
data = response.json()
print(data)

# access the dictionary results to store the longitude and latitude
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# make a tuple of the ISS position
iss_position = (longitude, latitude)

print(iss_position)

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
