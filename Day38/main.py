import requests
import os
import datetime

nutrition_app_id = os.getenv("nutrition_app_id")
nutrition_api_key = os.getenv("nutrition_api_key")
query = input("Tell me which exercise you did today: ")

nutrition_url = os.getenv("NUTRI_URL")

headers = {
    "Content-Type": "application/json",
    "x-app-id": nutrition_app_id,
    "x-app-key": nutrition_api_key,
}

data = {
    "query": query,
}
nutrion_response = requests.post(url=nutrition_url, json=data, headers=headers)

date = datetime.date.today().strftime(f"%d/%m/%y")
time = str(datetime.datetime.now().time()).split(".")
nutrion_response.raise_for_status()

exercise_data = nutrion_response.json()["exercises"][0]

sheety_url = os.getenv("SHEETY_URL")
sheety_header = {
    "Authorization": f"Bearer {os.getenv("SHEETY_BEARER")}",
} 

sheety_data = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise_data["name"],
        "duration": exercise_data["duration_min"],
        "calories": exercise_data["nf_calories"],
    }
}

sheety_response = requests.post(sheety_url, headers=sheety_header, json= sheety_data)
sheety_response.raise_for_status()

