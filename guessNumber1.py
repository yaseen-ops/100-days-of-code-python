import random
import art


def random_number():
    number = range(1, 101)
    number = random.choice(number)
    return number


def hint(guess_number):
    if guess_number > number:
        comp = guess_number - number
        if guess_number > number + 10:
            print("Too High")
        else:
            print("High")
    elif guess_number < number:
        comp = number - guess_number
        if number > guess_number + 10:
            print("Too Low")
        else:
            print("Low")


# def game_over():
#     if guess_number == number:
#         print("You Won The Game!")
#         is_game_over = True
#     elif rem_attempts == 0:
#         print("You Lose The Game!")
#         is_game_over = True

print(art.guess_number)
print("Welcome To The Number Guessing Game\n")
print("I am thinking of a number between 1 and 100")
number = random_number()
user_level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
attempts = 0
is_game_over = False
while not is_game_over:
    if user_level == "easy":
        easy_attempts = 10
        rem_attempts = easy_attempts - attempts
        # print(f"You have {rem_attempts} remaining to guess the number")
        # guess_number = int(input("Guess The Number : "))
        # hint(guess_number)
    else:
        hard_attempts = 5
        rem_attempts = hard_attempts - attempts
        # print(f"You have {rem_attempts} remaining to guess the number")
        # guess_number = int(input("Guess The Number : "))
        # hint(guess_number)
    # guess_number = ""
    if rem_attempts > 0:
        print(f"You have {rem_attempts} remaining to guess the number")
        guess_number = int(input("Guess The Number : "))
        hint(guess_number)
        if guess_number == number:
            # print("You Won The Game!")
            print(art.game_won)
            is_game_over = True
    elif rem_attempts == 0:
        # print("You Lose The Game!")
        print(art.game_lose)
        is_game_over = True
    # else:
    #     guess_number = int(input("Guess The Number : "))
    #     hint(guess_number)
    attempts += 1


# This code is written by me, for better experience check guessNumber2.py
