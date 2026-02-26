import pandas
#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

p_alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.



def generate_phonetics():
    user_input = input("Enter a word: ")
    try:
        p_list = [p_alphabet_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetics()
    else:
        print(p_list)

generate_phonetics()