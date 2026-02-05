import random
import hangman_words
import hangman_art


word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)
total_lives = 6
remaianing_lives = total_lives
print(hangman_art.hangman_title)
placeholder = "_" * len(chosen_word)

#converts placehollder to list to make it easier to change values
placeholder_list = list(placeholder)
# print(placeholder)

end_of_game = False

while not end_of_game:
    print(f"***************** {remaianing_lives}/6 LIVES LEFT*************************")
    display = "".join(placeholder_list)
    print(f"Word to guess: {display}")
    guess = input("Guess a letter: ").lower()
    #adjust index so ascii can start from the beginning
    art_index = (total_lives - remaianing_lives)


    for index in range(len(chosen_word)):
        #checks if letter has been guessed and replaces with guess if it hasn't
        if guess == chosen_word[index] and placeholder_list[index] == "_":
            placeholder_list[index] = guess
            break

        #checks guess is the same as the letter in current index and checks if there are no other occurences in the chosen word list
        elif guess == chosen_word_list[index] and guess not in chosen_word_list[index  + 1: ]:
            print(f"You have guess all {guess}'s present")
            break
        
        #checks if user guesses wrong and subtracts one life
        elif guess not in chosen_word_list:
            remaianing_lives -= 1
            # display = "".join(placeholder_list)
            # print(display)
            break

    if remaianing_lives < total_lives:
        #prints out hangman ascii
        print(hangman_art.stages[art_index])
        
    #End game
    if "_" not in placeholder_list:
        print(hangman_art.you_win)
        end_of_game = True
    elif remaianing_lives < 0:
        print(hangman_art.you_lose)
        print(f"The word was {chosen_word}")
        end_of_game = True
