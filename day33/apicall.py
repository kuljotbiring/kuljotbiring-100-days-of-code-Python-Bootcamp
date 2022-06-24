import requests

# make a get request
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# will print the response code 200 is OK
print(response)
