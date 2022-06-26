import requests

# put the parameters in a dictionary to use in GET request
parameters = {
    "amount": 10,
    "type": "boolean"
}

# use GET to call the API
response = requests.get("https://opentdb.com/api.php", params=parameters)

# check for errors
response.raise_for_status()
# put the response in the JSON format
data = response.json()
# get just the information inside a list by accessing the resulting dictionary
question_data = data["results"]

