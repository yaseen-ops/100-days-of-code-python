# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
# height_int = float(height)
# weight_int = int(weight)
# # round makes just round the number from floating
# bmi = round(weight_int / pow(height_int, 2)) # or /height_int * height_int or /height_int ** 2
#
# print("BMI is : " + str(bmi))
print(8 / 3)
print(round(8 / 3))
print(round(8 / 3, 2))  # round the number to two decimal places
print(8 // 3)  # or print(int(8 / 3)) , As usually divided number type will be float

print(type(4 / 2))
print(type(4 // 2))

score = 6
score += 2
print(score)
score = 6
score -= 2
print(score)
score = 6
score *= 2
print(score)
score = 6
score /= 2
print(score)
