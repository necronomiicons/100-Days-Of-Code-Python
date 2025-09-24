#TIP CALCULATOR
print("Welcome to the tip calculator!")
print("What was the total bill? $")
total = float(input())

print("How much tip would you like to give? 10, 12, or 15?")
percentage = float(input())
print("How many people to split the bill?")
number_of_people = float(input())

per_person = total / number_of_people
per_person = per_person + (per_person * (percentage/100))
per_person = round(per_person, 2)
print(f"Each person should pay: ${per_person}")