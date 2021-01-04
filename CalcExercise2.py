# Addition
def add(n1, n2):
    return n1 + n2


# Subtraction
def subtract(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    return n1 * n2


# Division
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Enter the first number : "))
for symbol in operations:
    print(symbol + "   ", end="")

operation_symbol = input("\nPick an operation from the above line : ")
num2 = int(input("Enter the second number : "))

calculation_function = operations[operation_symbol]
first_result = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {first_result}")

should_continue = True
while should_continue:
    wish_continue = input("Type 'y' to continue or type 'n' to exit : ")
    if wish_continue == "y":
        operation_symbol = input("Pick another operation : ")
        num3 = int(input("Enter another number : "))
        calculation_function = operations[operation_symbol]
        second_result = calculation_function(first_result, num3)
        print(f"{first_result} {operation_symbol} {num3} = {second_result}")
        first_result = second_result
    else:
        should_continue = False

# Check CalcExercise3.py for better coding.
