def format_name(f_name, l_name):
    # f_name = f_name.lower()
    # l_name = l_name.lower()
    # print(f_name.title(), l_name.title())  # Title case converts first letter as capital and remaining as small
    # return f_name.title(), l_name.title()
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_name = format_name(f_name="mOHammed", l_name="yaSin")
print(formatted_name)
