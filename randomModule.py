import random

# Prints a random integer from 1 to 11 every time we run the code, we can use this for 'Dice' games
random_integer = random.randint(1, 6)
print(random_integer)

random_float = random.random()  # Prints a random float from 0 to 0.9999..
print(random_float)

# If i want to have a random float above 0.999... then i have to just multiple with the number, example
random_float = random_float * 5
print(random_float)

heads_tails = random.randint(0, 1)
if heads_tails == 1:
    print("It\'s a Heads")
else:
    print("Its\'s a Tail")
