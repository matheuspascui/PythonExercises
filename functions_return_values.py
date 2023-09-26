'''
In this file, we'll explore the return values for functions. If we only call our function, nothing will be displayed on 
screen, but the returning was done. Example:
add_numbers(1,2)

Only typing this, nothing will be displayed on screen, BUT the function returned its value, in this case, 3 (by
adding 1 and 2 and RETURNING it).

BUT, if we create a variable and assign the returning value of the function as the value of the variable, printing
the variable, then we can actuallt see what has been done.
'''

def add_numbers(num1, num2):
    return num1 + num2

# Assigning the variable's value to the returning value of the function
sum1 = add_numbers(3,5)

# Printing the variable to see the returning value
print("Below, we'll print the variable sum1 that hold the returning value of add_numbers function")
print(sum1)

sum2 = add_numbers(3,23)
print(sum2)
