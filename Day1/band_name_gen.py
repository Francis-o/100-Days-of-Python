"""
This progrsm tskes name of city and pet and concatenates the string
to give suggested band name
"""

print("Welcome to the Band Name Genertor.")
city_name = input("What's the name of the city you grew up in? \n")
pet_name = input("What's your pet's name?\n")
band_name = city_name + " " + pet_name
print(f"Your band name could be {band_name.title()}")