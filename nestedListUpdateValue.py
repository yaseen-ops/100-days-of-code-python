row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

# row1 = ["r1c1", "r1c2", "r1c3"]
# row2 = ["r2c1", "r2c2", "r2c3"]
# row3 = ["r3c1", "r3c2", "r3c3"]

mapping = [row1, row2, row3]
position = input("Enter the position : ")
value1 = int(position[0])
value2 = int(position[1])
mapping[value1 - 1][value2 - 1] = "💲"  # row/column
# mapping[value2-1][value1-1] = "💲"  # column/row
print(f"{row1}\n{row2}\n{row3}")
