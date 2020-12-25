import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [Rock, Paper, Scissor]
user_choice = int(input("Enter your choice by typing 0 for Rock, 1 for Paper, 2 for Scissor\n"))
if user_choice >= 3 or user_choice < 0:  # Earlier didn't have an if statement here, after debugging moved here
    print("You typed an invalid number, You lose!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer's Choice : ")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's a draw, Retry")
