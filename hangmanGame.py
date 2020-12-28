import random
import hangman_words
import hangman_art
from os import system, name

print(hangman_art.logo)
# word_list = ["tiger", "elephant", "camel", "lizard"]
word_list = hangman_words.word_list
random_word = random.choice(word_list)

# user_guess = input("Guest a letter : ").lower()
# for letter in range(len(random_word)):
world_length = len(random_word)
empty_list = []
for _ in range(world_length):  # OR for _ in random_word:
    empty_list.append("_")
    # OR
    # empty_list += "_"

    # while empty_list.count('_') > 0:  # If there is no '_' in the list means obviously the user has matched the word.
#     user_guess = input("Guest a letter : ").lower()
#     for position in range(world_length):
#         letter = random_word[position]
#         if letter == user_guess:
#             empty_list[position] = letter
#     print(empty_list)
# print("You Won!")
############## OR ########################
lives = 6
end_game = False
while not end_game:
    user_guess = input("Guest a letter : ").lower()
    if user_guess in empty_list:
        print(f"The letter {user_guess} already guessed")
    for position in range(world_length):
        letter = random_word[position]
        if letter == user_guess:
            empty_list[position] = letter
    print(empty_list)
    if user_guess not in random_word:
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            end_game = True
            print(f"Your Lose!.. The word is {random_word}")
    if "_" not in empty_list:
        end_game = True
        print("You Won!")