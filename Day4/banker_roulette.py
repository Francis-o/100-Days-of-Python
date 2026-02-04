"""
picks one a name randomly from the list to pay the bills
"""

import random

friends = ["Adebola", "Chinedu", "Amina", "Sadiq", "Funke"]

# random_name = random.choice(friends)
#subtracts one because python starts counting from zero
random_name = friends[random.randint(0, (len(friends) - 1))]
print(random_name)