# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights : ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    # print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total Height = {total_height}")

total_students = 0
for student in student_heights:
    total_students += 1
print(f"Total Students = {total_students}")

######## OR ##########
# total_height = sum(student_heights)
# total_students = len(student_heights)

average_height = round(total_height / total_students)
print(f"Average height of all the students : {average_height}")
