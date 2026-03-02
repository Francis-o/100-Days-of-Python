import pandas
import datetime as dt
import random
import smtplib

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

birthday_data = pandas.read_csv("birthdays.csv")
current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day
for index, content in birthday_data.iterrows():
    birth_month = content["month"]
    birth_day = content["day"]
    if birth_month == current_month and  birth_day == current_day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        celebrants_name = content["name"]
        celebrants_email = content["email"]
        my_email = ""
        my_password = ""
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r")  as letter_file:
            content = letter_file.read()
            new_letter = content.replace("[NAME]", celebrants_name)

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(from_addr=my_email, to_addrs=celebrants_email, msg=f"Subject: Happy Birthday!\n\n{new_letter}")

