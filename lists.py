states_of_india = ["Tamil Nadu", "Kerala", "Telugana", "Karnatka", "Andhra Pradesh", "Maharastra", "Punjab"]

states_of_india.append("Haryana")
print(states_of_india)

states_of_india.extend(["Assam", "Manipur"])
print(states_of_india)

print(states_of_india[0])
print(states_of_india[1])
print(states_of_india[-1])
print(states_of_india[-3])
print(states_of_india.index("Kerala"))

states_of_india.insert(5, "Goa")  # insert(position, value)
print(states_of_india)

states_of_india.remove("Haryana")
print(states_of_india)
print(states_of_india.count("Kerala"))
states_of_india.sort()
print(states_of_india)
states_of_india.reverse()
print(states_of_india)
states_of_india.pop()  # Removes the last item by default
print(states_of_india)
states_of_india.pop(3)
print(states_of_india)
