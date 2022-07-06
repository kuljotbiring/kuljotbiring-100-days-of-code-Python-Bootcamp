import requests
from datetime import datetime

APP_ID = "b54e4ff0"

API_KEY = "c9dd34d38290af55d6ad636b34ae46fc"

GENDER = "male"
WEIGHT_KG = 90.7
HEIGHT_CM = 177.8
AGE = 40

sheety_url = "https://api.sheety.co/e16bd98df5e37971e300376e218ae6fe/workoutTracking/workouts"

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

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_url, json=sheet_inputs)

    print(sheet_response.text)
