import art


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


def calculator():
    """
        Used to calculate numbers with different arithmetic operators
    """
    print(art.calc_logo)
    num1 = float(input("Enter the first number : "))  # Changes int to float.
    for symbol in operations:
        print(symbol + "   ", end="")

    should_continue = True
    while should_continue:
        operation_symbol = input("\nPick an operation from the above line : ")
        num2 = float(input("Enter the next number : "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        # Instead of exiting the calculator, let's just restart it from beginning.
        # To restart from the beginning we have to make this code as function to call again from initial spot.
        wish_continue = input("Type 'y' to continue or type 'n' to start a new calculation : ")
        if wish_continue == "y":
            num1 = result
        else:
            should_continue = False
            calculator()  # Recursive function, calling the function within the same function


calculator()
