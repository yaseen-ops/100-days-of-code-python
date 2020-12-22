age = input("What is your current age? ")

# life_end = 90
# days_oneyear = 365
# weeks_oneyear = 52
# months_oneyear = 12
# life_num_days = days_oneyear * life_end
# life_num_weeks = weeks_oneyear * life_end
# life_num_months = months_oneyear * life_end
#
# age_num_days = days_oneyear * int(age)
# age_num_weeks = weeks_oneyear * int(age)
# age_num_months = months_oneyear * int(age)
#
# left_days = life_num_days - age_num_days
# left_weeks = life_num_weeks - age_num_weeks
# left_months = life_num_months - age_num_months
#
# print(f"Number of days left in your Life is: {left_days}")
# print(f"Number of weeks left in your Life is: {left_weeks}")
# print(f"Number of months left in your Life is: {left_months}")


# But you can do it in a simple way like below hahaha
years_left = 90 - int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
age_message = f"You have left {years_left} years, {months_left} months, {weeks_left} weeks and {days_left} days"
print(age_message)
