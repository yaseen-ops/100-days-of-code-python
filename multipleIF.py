height = int(input("Enter your height in cm : "))

if height >= 120:
    print("You can ride a rollercoaster")
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Child tickets are $7")
    else:
        bill = 12
        print("Child tickets are $12")
    wants_photo = input("Do you want to take photo : Y or N - ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Your are not allowed to ride")
