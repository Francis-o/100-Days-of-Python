import pandas
#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

p_alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
p_list = [p_alphabet_dict[letter.upper()] for letter in user_input]
print(p_list)

