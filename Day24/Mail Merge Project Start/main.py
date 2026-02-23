#TODO: Create a letter using starting_letter.txt 
with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    content = letter_file.read()

with open("input/Names/invited_names.txt", "r") as name_file:
    name_list = name_file.readlines()
    for name in name_list:
        name = name.strip("\n")
        print()
        
        # ceate and save personalized letters
        with open(f"Output/ReadyToSend/letter_for_{name}", "w") as editted_letter:
            editted_letter.write(content.replace("[name]", name))
