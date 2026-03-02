import requests
from datetime import datetime
import smtplib
from time import sleep

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

#If the ISS is close to my current position
def iss_close():


    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    return MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <=iss_longitude <= MY_LONG+5

def is_dark():
    
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    current_hour = time_now.hour
    return current_hour < sunrise or current_hour > sunset

def send_mail():
    my_email = ""
    my_password = ""
    with smtplib.SMTP("smtp.gmail.com",  port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: LOOK UP\n\nISS close!!")

search_on = True
cycle_count = 0

while search_on:
    cycle_count += 1
    if iss_close() and is_dark():
        send_mail()
        search_on = False
    print(f"{cycle_count} cycles")
    sleep(60)




