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
num2 = int(input("Enter the second number : "))

for symbol in operations:
    print(symbol + "   ", end="")

operation_symbol = input("\nPick an operation from the above line : ")

calculation_function = operations[operation_symbol]
result = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {result}")
