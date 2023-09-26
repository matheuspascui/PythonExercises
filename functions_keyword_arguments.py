''' In this type of functions, we use keyword arguments.
'''

def print_without_kwarg(name, age):
    print("My name is", name, "and my age is", age)

print_without_kwarg("Matheus", 24)

'''Now, if we use the new function with default arguments:
'''

def print_df_arguments(name = "Someone", age = 21):
    print("My name is", name, "and my age is", age)

# calling the function WITHOUT arguments to display its default arguments
print_df_arguments()

# calling the function WITH arguments
print_df_arguments("José", 35)

'''BUT, if i only want to modify the age and NOT pass any name argument, the function will display the default OR, if the function is
like the print_without_kwarg, it will throw an error, missing arguments.
To avoid that, we can use KEYWORD ARGUMENTS to pass the arguments that we want, no matter the order we passed them to the function.
'''

def print_with_kwarg(name = "Alguém", age = 30):
    print("My name is", name, "and my age is", age)


# calling the function with its default arguments
print_with_kwarg()

# calling the function with KWARGS
# This way we can let the default argument for name and only change the age parameter
print_with_kwarg(age = 27)

# This way we modify both arguments of the function
print_with_kwarg(age = 45, name = "TESTE")