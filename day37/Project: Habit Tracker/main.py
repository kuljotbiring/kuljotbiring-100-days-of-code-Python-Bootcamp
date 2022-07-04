import requests
from datetime import datetime

USER_NAME = "kuljotbiring"
TOKEN = "pixelaapipass90210"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # this will create the user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# # now we check if the command went through
# print(response.text)

# create a graph
# create the graph endpoint
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
# set the arguments for the graph
graph_config = {
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "miles",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# make the post request
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# the graph can be viewed at https://pixe.la/v1/users/kuljotbiring/graphs/graph1.html

# make a data point on the graph
data_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()

data_config = {
    # use date format to change datetime format to API specs
    # https://www.w3schools.com/python/gloss_python_date_format_codes.asp
    "date": today.strftime("%Y%m%d"),
    "quantity": "6.25",
}

# make the post request
response = requests.post(url=data_endpoint, json=data_config, headers=headers)
print(response.text)
