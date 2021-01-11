import random
import subprocess

from HigherLowerGameData import data
from art import higherlower, vs

score = 0


def format_account(account):
    """Format the data and return in to a printable format"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, from {country}"


def check_answer(guess, a_follower_count, b_follower_count):
    """Take the user guess & follower count and return if they got it right"""
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"


print(higherlower)
account_b = random.choice(data)  # its like b = randomint, a = b & again b = randint , LOGIC
game_should_continue = True
while game_should_continue:
    # account_a = random.choice(data)
    # account_b = random.choice(data)
    account_a = account_b
    account_b = random.choice(data)
    # if account_a == account_b:
    while account_a == account_b:  # Better to have while run again & again until both doesn't have same data
        account_b = random.choice(data)

    print(f"Compare A : {format_account(account_a)}")
    print(vs)
    print(f"Against B : {format_account(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # subprocess.run(["clear"])  # Uncomment this line if you run in bash for clearing the screen
    print(higherlower)
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right!, Current score : {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong, Final score : {score}")
