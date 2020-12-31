dictionary = {
    "greet": "Hello",
    "day": "Morning",
    "name": "Dhoni",
    12: "test"
}
print(dictionary)
print(dictionary["greet"], dictionary["name"])
print(dictionary[12])

# Either it creates a new entry in dictionary or updates the existing one.
dictionary["sport"] = "Cricket"

print(dictionary)

# Either creates an empty dictionary or deletes the exiting dictionary.
# dictionary = {}

for key in dictionary:
    print(f"{key} : ", end="")
    print(dictionary[key])
