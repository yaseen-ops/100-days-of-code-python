import random

name_string = input("Enter the set of names separated by comma \n")
names = name_string.split(",")

length = (len(names))

# opening_batsman = names[random.randint(0, length - 1)]
############### OR #############
# random_choice = random.randint(0, length - 1)
# opening_batsman = names[random_choice]
############### OR #############
opening_batsman = random.choice(names)
print("Opening Batsman for today's match is " + opening_batsman)
