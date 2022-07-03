import requests
import os

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "pixelaapipass90210",
    "username": "kuljotbiring",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# this will create the user
response = requests.post(url=pixela_endpoint, json=user_params)
# now we check if the command went through
print(response.text)

