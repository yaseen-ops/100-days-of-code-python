def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide any inputs"  # return statement ends the function
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_name = format_name(input("Enter your first name : "), input("Enter your last name : "))
print(formatted_name)
