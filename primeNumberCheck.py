# def prime_checker(number):
#     if number in [1, 2, 3, 5, 7]:
#         print(f"{number} is a prime number")
#     elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
#         print(f"{number} is not a prime number")
#     else:
#         print(f"{number} is a prime number")
#
# user_number = int(input("Enter a number : "))
# prime_checker(user_number)
#### OR ######
def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


user_number = int(input("Enter a number : "))
prime_checker(user_number)
