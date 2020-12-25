import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
letter_pass = ""
for letter in range(1, 5):
    password_letter = random.randint(0, len(letters) - 1)
    letter_pass += str(letters[password_letter])
# print(letter_pass)

number_pass = ""
for number in range(1, 5):
    password_number = random.randint(0, len(numbers) - 1)
    number_pass += str(numbers[password_number])
# print(number_pass)

symbol_pass = ""
for symbol in range(1, 5):
    password_symbol = random.randint(0, len(symbols) - 1)
    symbol_pass += str(symbols[password_symbol])
# print(symbol_pass)

# password_temp = str(letter_pass) + str(number_pass) + str(symbol_pass)
password = letter_pass + number_pass + symbol_pass
print(f"Newly generated password is {password}")
