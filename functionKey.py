def greet(name, age):
    print(f"Hello {name}, ", end="")
    print(f"Your age is {age}")


# greet(31, "Yasin")  # This one prints name as 31 and ages as "Yasin", but it is incorrect, we can use keywords
# greet(age=31, name="Yasin")   # Using Keyword where the value of the parameter doesn't change.
greet(name="Yasin", age=31)