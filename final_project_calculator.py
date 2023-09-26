# By importing 're', we are importing the library to work with regex in Python
import re

print("My Calculator in Python")
print("Type 'quit' to exit.\n")

previous_result = 0
run = True

def perform_Math_Operations():
    #says that our run variable is the variable OUTSIDE this function, the run defined before, otherwise we can't access it from within the function
    global run
    global previous_result
    equation = input("Enter your equation: ")
    if equation == "quit":
        run = False
    else:
        #Performing regex to avoid misuse of typing in the input by the user
        equation = re.sub('[a-zA-Z,.:()+" "]', '', equation)
        previous_result = eval(equation)
        print("Your equation:", previous_result)

while run:
    perform_Math_Operations()