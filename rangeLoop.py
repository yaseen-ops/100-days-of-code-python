even_number = 0
for number in range(0, 101, 2):
    even_number += number
print(f"Total of even number is {even_number}")

### OR ###

# even_number = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         even_number += number
# print(f"Total of even number is {even_number}")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
