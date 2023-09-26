'''In this file, we'll see functions with infinite number of arguments.
In the case below, we are defining a function that will print people's names, BUT we DON'T know before how many
people we are talking about, it may be 2 or it may be 50 people, or maybe 5.000!
So, by using the * (asterisk) before the variable (argument) name, we are telling python that this variable will be
an array, and the function's argument will be this array. So the functino reads this array and process it inside itself.
'''

def print_people_names(*people):
    for person in people:
        print("This person's name is", person)

print_people_names("Matheus", "José", "Maria", "Carolina", "Mariana", "Nicole", "Mário", "Guilherme", "Hugo")

# As the function's argument is a list AND in Python a list is an array that accepts any data types, we can pass
# numbers in that list that will be displayed by our function
print("\nBelow, as a test, we'll be using print_people_names but passing an int as an item in the list!")
print_people_names("Josefina", "Thiago", "Gabriel", "César", 25, 65, 4092)
