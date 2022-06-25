import requests, os
from datetime import datetime


# enter your information here

GENDER = YOUR_GENDER
WEIGHT_KG = YOUR_WEIGHT
HEIGHT_CM = YOUR_HEIGHT
AGE = YOUR_AGE

# use this API to get APP _ID and API_KEy
# "https://www.nutritionix.com/business/api"

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# use https://sheety.co/ to get your own excersise sheet
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

# method to enter your exercise data in text format
# eg. "1.5 hours of running" or "I did 1.5 hours of running"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM
    
}

response_from_API = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response_from_API.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# bearer token for the sheet API

bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

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

# use the sheet API to enter your exercise data into the sheet
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)