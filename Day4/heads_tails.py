"""
This program generates two random numbers and prints 
out heads or tails based on number generated
"""

import random

num = random.randint(0,1)

if num == 0:
    print("Heads")
elif num == 1:
    print("Tails")

