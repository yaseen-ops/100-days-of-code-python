import caesarArt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # To Avoid if statement in encrypt function


def caesar_cipher(user_text, shift_amount, cipher_direction):
    code_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in user_text:
        if char not in alphabet:
            code_text += char
        else:
            letter_index = alphabet.index(char)
            new_letter_index = letter_index + shift_amount  # Usually this will not work, for this you have to change the
            # list variable at the top. Better i recommend the best format of function is above one only.
            code_text += alphabet[new_letter_index]
    print(f"The {cipher_direction}d text is {code_text} \n\n")


print(caesarArt.logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction not in ["encode", "decode"]:
        print("Rerun and Type 'encode' to encrypt, type 'decode' to decrypt ")
        exit()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # if int(shift) >= 26:
    #     print("Rerun and Please enter the shift number from 0 to 25")
    #     exit()
    # Or you don't need to warn or exit if the user enters a range out of box, you can compress the range by using
    # modulus "shift = shift % 26"

    shift = shift % 26
    caesar_cipher(user_text=text, shift_amount=shift, cipher_direction=direction)
    user_continue = input("Type 'yes' if you want to go again. Otherwise type 'no' : ")
    if user_continue == "no":
        should_continue = False
        print("\nGood Bye!")
