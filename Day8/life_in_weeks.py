"""
converts years calculated to weeks
"""

def life_in_weeks(age):
    end_age = 90
    years_left = 90 - age
    weeks_left = int(years_left * int((365/7)))
    print(f"You have {weeks_left} weeks left.")
    
life_in_weeks(40)