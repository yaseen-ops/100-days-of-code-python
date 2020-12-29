# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # To Avoid if statement in encrypt function

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction not in ["encode", "decode"]:
    print("Rerun and Type 'encode' to encrypt, type 'decode' to decrypt ")
    exit()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def ceaser_cipher(user_text, shift_amount, cipher_direction):
#     code_text = ""
#     for letter in user_text:
#         letter_index = alphabet.index(letter)
#         if direction == "encode":
#             new_letter_index = letter_index + shift_amount
#             if new_letter_index > 25:
#                 new_letter_index = new_letter_index - 26
#         elif direction == "decode":
#             new_letter_index = letter_index - shift_amount
#             if new_letter_index < 0:
#                 new_letter_index = new_letter_index + 26
#         code_text += alphabet[new_letter_index]
#     print(f"The encoded text is {code_text}")

########### OR ####################

def caesar_cipher(user_text, shift_amount, cipher_direction):
    code_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in user_text:
        letter_index = alphabet.index(letter)
        new_letter_index = letter_index + shift_amount  # Usually this will not work, for this you have to change the
        # list variable at the top. Better i recommend the best format of function is above one only.
        code_text += alphabet[new_letter_index]
    print(f"The {cipher_direction}d text is {code_text}")


caesar_cipher(user_text=text, shift_amount=shift, cipher_direction=direction)
