variable = 5


# def test_variable():
#     print(variable)
#
#
# test_variable() # This will print 5, as top variable is a global variable where you can call it anywhere

# def test_variable():
#     variable = 4
#     print(variable)
#
#
# test_variable()  # This will print 4, as we defined a local variable for fun test_variable


# def test_variable():
#     #variable += 2  # This is will not work as there isn't any local variable to modify.
#     global variable  # we have mention global to modify global variable
#     variable += 2  #  But this actually we are modifying the global variable
#     print(variable)
#
#
# # Both the output of below statements will print same answer, as the global variable as well modified
# test_variable()
# print(variable)


def test_variable():
    return variable + 3


# Now we haven't modified the global variable and made use of global variable for increment
print(test_variable())
print(variable)
