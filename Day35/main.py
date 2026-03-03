import requests
import smtplib

MY_LATT = -15.562220
MY_LONG = -49.945179
api_key = ""

parameters = {
    "q": "London,Uk",
    "appid": api_key,
    "lat": MY_LATT,
    "lon": MY_LONG,
    # "cnt": 4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data_list = weather_data["list"]


for weather_data in weather_data_list:
    weather_id = weather_data["weather"][0]["id"]
    weather_descr = weather_data["weather"][0]["description"]
    if weather_id < 700:
        email = ""
        password = ""
        msg = "It's going to rain today. Remember to bring an ☂️"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(email,  password)
            connection.sendmail(to_addrs="@gmail.com", from_addr=email, msg=f"Subject: It's going to rain\n\n{msg}")
    break
   
    
