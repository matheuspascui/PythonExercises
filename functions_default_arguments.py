''' The difference between writing print("My name is" + name + "and my age is" + age) and
print("My name is", name, "and my age is", age) is that in the 2nd print, the function print is printing 4 differente things, like
if instead of writing 4 separate print(), we used only 1 but passed 4 types of things to print on screen.
The 1st print is concatenating strings and won't work because we can have age as an int and not a string, so it will throw a conversion
error, because we tried to concatenate a string and an integer without converting the int.
'''

''' In other cases, where we must have values by default on the functions, we can achieve this by using default values for the functions.
It means that within the parentheses we set default values for the parameters.
'''

def another_printing(name, age):
    print("My name is", name, " and my age is" , age)

another_printing("Matheus", 24)

def printing_v2(name = "Name", age = "21"):
    print("My name is", name, "and my age is", age)

printing_v2()
printing_v2("Carolina", 23)
