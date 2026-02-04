"""
Prints out highest score in a list using for loop
"""

student_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
max_score = 0
for number in student_score:
    if number > max_score:
        max_score = number
print(max)
