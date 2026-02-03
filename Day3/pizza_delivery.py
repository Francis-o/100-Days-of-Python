"""
This program gets final bill by adding user preference
"""
print("Welcome to Python Pizza Delivery")
size = input("What size of pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill  += 15
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3

#add cheese if yes to bill
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")