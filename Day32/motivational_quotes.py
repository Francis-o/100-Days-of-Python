import smtplib
import datetime as dt
import random


# connnection = smtplib.SMTP("smtp.gmail.com", port=587)
# connnection.starttls()
# connnection.login(user=email, password=password)
# connnection.sendmail(from_addr=email, to_addrs="programtest15@gmail.com", msg="Hello")
# connnection.close()

date = dt.datetime.now()
day = date.weekday()

if day == 0:
    email = ""
    password = ""

    with open("quotes.txt", "r") as quotes_file:
        quotes =  quotes_file.readlines()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="programtest15@gmail.com", msg=f"Subject:QUote of the day\n\n{random.choice(quotes)}")
