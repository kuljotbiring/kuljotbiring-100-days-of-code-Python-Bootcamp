import requests

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

