# Function
# Python Function
# a function is a block of code which only runs when it is called
# a function can return data as a result
# a function helps avoiding code repetition

# Creating a Function
# a function is defined using the def keyword followed by a function name and parenthesis
def my_function():
    print("Hello World")
# this creates a function named my_function that prints "Hello World" when called
# the code inside the function must be indented
# python uses indentation to define code block

# Calling a Function
# to call a function write its name followed by parenthesis
def my_function():
    print("Hello World")
my_function()
# we can call the same function multiple times
my_function()
my_function()
my_function()

# Function Names
# function names follow the same rules as variable names in python
#   a function name must start with a letter or underscore
#   a function name can only contain letters, numbers, and underscores
#   function names are case-sensitive (myFunction and myfunction are different)
# sample names
# calculate_sum()
# _private_function()
# my_function2()
# its good practice to use descriptive names that explain what the function does

# Why Use Functions?
# imagine we need to convert temp from fahrenheit to celsius several times in our program
# without functions we would have to write the same calculation code repeatedly
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# with functions - resuable code
def fahrenheit_to_celsiuss(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsiuss(77))
print(fahrenheit_to_celsiuss(95))
print(fahrenheit_to_celsiuss(50))

# Return Values
# function can send data back to the code that called them using the return statement
# when a function reaches a return statement it stops executing and sends the result back
def get_greetings():
    return "Hello there"
message = get_greetings()
print(message)
# we can use the returned value directly
def get_greetings():
    return "Hello there"
print(get_greetings)
# if a function doesnt have a return statement it returns None by default

# The pass Statement
# function definitions cannot be empty if we need to create a function placeholder without any code use the pass statement
def my_func():
    pass
# the pass statement is often used when developing allowing you to define the structure first and implement details later
