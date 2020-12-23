# Reference links
# https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

bill_amount = float(input("Enter your bill amount : $"))
# print(bill_amount)
tips_percent = int(input("Enter % of tips to be give 12 or 15 or 17 : "))
# print(tips_percent)
share_person = int(input("Enter the number of persons sharing : "))
# print (share_person)

bill_with_tip = (bill_amount * (tips_percent / 100) + bill_amount) / share_person
pay_per_person = round(bill_with_tip, 2)
print(f"\nPayment per person is {pay_per_person}")
pay_per_person = "{:.2f}".format(bill_with_tip)  # This format rounds to 2 decimal through actual result doesn't has
print(f"\nPayment per person is {pay_per_person}")
