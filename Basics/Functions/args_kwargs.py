# *args and **kwargs
# by default a function must be called with the correct number of arguments
# however sometimes we want not know how many arguments that will be passed into our function
# *args and **kwargs allow functions to accept a unknown number of arguments

# Arbitrary Arguments, *args
# if we do not know how many arguments will be passed into our fumction add a * before the parameter name
# this way the function will receive a tuple of arguments and can access the items accordingly
def myFunc(*kids):
    print("The youngest child is " + kids[2])
myFunc("Emil", "Tobias", "Linus")
# Arbitrary Arguments are often shortened to *args in Python documentations

# What is *args?
# the *args parameter allows a function to accept any number of positional arguments
# inside the functtion args becomes a tuple containing all the passed arguments
def myFunc(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)
myFunc("Emil", "Tobias", "Linus")

# Using *args with Regular Arguments
# we can combine regular parameters with *args
# Regular parameters must come efore *args
def myFunc(greeting, *names):
    for name in names:
        print(greeting, name)
myFunc("Hello", "Emil", "Tobias", "Linus")

# Practical Example with *args
# args is useful when we want to create flexible function
# a function that calculates the sum of any number of values
def myFunc(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(myFunc(1, 2, 3))
print(myFunc(10, 20, 30, 40))
print(myFunc(5))
# finding the maximum value
def myFunc(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(myFunc(3, 7, 2, 9, 1))

# Arbitrary Keyword Arguments, **kwargs
# if we do not know how many keyword arguments that will be passed into our function add a double ** before the parameter name
# this way the function will receive a dictionary of arguments and can access the items accordingly
def myFunc(**kid):
    print("His last name is " + kid["lname"])
myFunc(fname="Tobias", lname="Refsnes")
# Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentations

# What is **kwargs?
# the **kwargs parameter allows a function to accept any number of keyword arguments
# inside the function kwargs becomes a dictionary containing all the keyword arguments
def myFunc(**myvar):
    print("Type:", type(myvar))
    print("Name", myvar["name"])
    print("Age", myvar["age"])
    print("All Data:", myvar)
myFunc(name="Alice", age=30, city="New York")

# Using **kwargs with Regular Arguments
# we can combine regular parameters with **kwargs
# Regular parameters must come before **kwargs
def myFunc(username, **details):
    print("Username:", username)
    print("Additional Details:")
    for key, value in details.items():
        print(" ", key + ":", value)
myFunc("emil123", age=25, city = "Oslo", profession="Coding")

# Combining *args and **kwargs
# we can use both *args and **kwargs in the same function
# the order of parameters must be: regular parameters, *args, **kwargs
def myFunc(title, *args, **kwargs):
    print("Title:", title)
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)
myFunc("User Info", "Emil", "Tobias", age=25, city="Oslo")

# Unpacking Arguments
# the * and ** operators can also be used when calling functions to unpack(expand a list or dictionary into separate argumets

# Unpacking List with *
# if we have values stored in a list we can use * to unpack them into indivual arguments
def myFunc(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
result = myFunc(*numbers)
print(result)

# Unpacking Dictionary with **
# if we have keyword arguments stored in a dictionary we can use ** to unpack them
def myFunc(fname, lname):
    print("Hello", fname, lname)
person = {"fname": "Emil", "lname": "Refsnes"}
myFunc(**person)