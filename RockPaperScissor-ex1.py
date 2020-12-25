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


def print_choice():
    print("Your choice:")
    print("############")


game_images = [Rock, Paper, Scissor]
computer_choice = random.choice(game_images)
user_choice = input("Enter your choice of Rock, Paper, Scissor : ")
if user_choice == "Rock":
    print_choice()
    print(Rock)
elif user_choice == "Paper":
    print_choice()
    print(Paper)
elif user_choice == "Scissor":
    print_choice()
    print(Scissor)
else:
    print("Please enter Rock or Paper or Scissor")
print("Computer Choice:")
print("################")
print(computer_choice)
