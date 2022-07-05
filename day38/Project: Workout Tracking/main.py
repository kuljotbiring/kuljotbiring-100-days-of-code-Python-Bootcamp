import requests

APP_ID = "b54e4ff0"

API_KEY = "c9dd34d38290af55d6ad636b34ae46fc"

GENDER = "male"
WEIGHT_KG = 90.7
HEIGHT_CM = 177.8
AGE = 40

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

excercise_text = input("Tell me which exercise you did: ")

body = {
    "query": excercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(exercise_endpoint, json=body, headers=headers)
result = response.json()
print(result)
