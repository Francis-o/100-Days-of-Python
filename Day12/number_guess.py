"""
Let's user guess randomly generated number with a limited amount of trials
"""

import random
import number_guess_art

def number_guess():
    #range within which the number can be gotten
    print(number_guess_art.GAME_NAME)
    min_range = 1
    max_range = 100
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {min_range} and {max_range}.")
    attempts = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("You entered an invalid value")
        return
    number = random.randrange(min_range, max_range + 1) 

    end_of_game = False
    while not end_of_game:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if attempts  == 1 and guess != number:
            print("You have run out of guesses. Game Over.")
            end_of_game = True
        elif number == guess:
            print(f"You got it! The answer was {number}.")
            end_of_game = True
        elif guess > number:
            print("Too high. \nGuess again.")
            attempts -= 1
        elif guess < number:
            print("Too low. \nGuess again.")
            attempts -= 1   
 

        

number_guess()