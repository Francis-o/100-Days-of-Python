"""
This code takes in the total biil, tip percent and how many people the bill will be shared with 
and returns the amount each individual would pay
"""

print("Welcome to the tip calculator!")
total_bill = float(input("what was the total bill? ₦"))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people should split the bill? "))
tip_amount = (total_bill * tip_percent) / (100)
payment_each = (total_bill + tip_amount) / num_people
print(f"Each person shoulld pay: ₦{payment_each:.2f}")
