"""
This program takes a numberr as input and checks if a number is odd or even 
It then prints out odd if the number is odd othrwise it prints even
"""

num = int(input("Enter the number you want to check: "))
if num % 2 == 0:
    print(f"{num} is an even number!")
else:
    print(f"{num} is an odd number!")
