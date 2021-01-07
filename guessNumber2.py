import random
import art

# Assigning global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's answer against the guess
def check_answer(guess, answer, turns):  # added turns to reduce turns by 1 during every attempt
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty, Type 'easy' or 'hard': ")
    if level == "easy":
        # turns = EASY_LEVEL_TURNS
        return EASY_LEVEL_TURNS
    else:
        # turns = HARD_LEVEL_TURNS
        return HARD_LEVEL_TURNS


def game():
    print(art.guess_number)
    print("Welcome To The Number Guessing Game")
    print("I am thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    # print("The random number is :", answer)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining to guess the number.")
        guess = int(input("Make a guess : "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses, You Lose!")
            return  # Return is end the end loop
        elif guess != answer:  # This is optional
            print("Guess again. ")


game()
