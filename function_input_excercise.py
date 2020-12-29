import math

height = int(input("Enter the height of the wall : "))
width = int(input("Enter the width of the wall : "))
cover = 5


def number_of_cans(wall_height, wall_width, coverage):
    cans_required = int(math.ceil(wall_height * wall_width) / coverage)
    print(f"You need {cans_required} cans of paint")


number_of_cans(wall_height=height, wall_width=width, coverage=cover)
