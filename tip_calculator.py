print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? US$"))
percentage = float(input("What percentage would you like to give? "))
people = int(input("How many people will split the bill? "))

value_per_person = (bill + (percentage/100) * bill) / people
print("The value per person will be: " + "%.2f" %value_per_person)
