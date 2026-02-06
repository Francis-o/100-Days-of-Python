import caeser_cipher_art

print(caeser_cipher_art.banner)
alphabet = [
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z'
]


def caeser(direction, text, shift_amount):
    output_text = ""
    if direction == "decode" or direction == "encode":
        if direction == "decode":
            shift_amount *= -1
        for letter in text:
            if letter in alphabet:
                new_index = alphabet.index(letter) + shift_amount
                new_index %= len(alphabet)
                output_text += alphabet[new_index]
            else:
                output_text += letter
    print(f"Here is the {direction}d result: {output_text}") 

end_of_code = False
while not end_of_code:
    directions = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caeser(direction=directions, text=text, shift_amount=shift)
    continue_cipher = input("Type 'yes' if you want to go again. Otherwise 'no'. \n").lower()
    if continue_cipher == "yes":
        continue
    else:
        end_of_code = True



