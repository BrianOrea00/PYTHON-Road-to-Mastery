# Arguments
# information can be passed into functions as arguments
# arguments are specified after the function name inside the parenthesis we can add as many arguments as we want just separate them with comma
# this function with one argument (fname) when the function is called we pass along a first name which is used inside the function to print the full name
def myFunc(fname):
    print(fname + " Refsnes")
myFunc("Emil")
myFunc("Tobias")
myFunc("Linus")

# Parameters  vs Arguments
# the term parameter and argument can be used for same thing
# information that are passed into a function

# from a functions perspective 
# a parameter is the variable listed inside the parenthesis in the function definition
# an argument is the actual value that is sent to the function when it is called
def myFunc(name): # name is a parameter
    print("Hello",name)
myFunc("Brian") # "Brian" is an argument

# Number of Arguments
# by default a function must be called with the correct number of arguments
# if the function expects 2 arguments we must call it with exactly 2 arguments
def myFunc(fname, lname):
    print(fname + " " + lname)
myFunc("Brian", "Orea")
# if we try to call the function with the wrong number of arguments
# we will get an error
# def myFunc(fname, lname):
#   print(fname + " " + lname)
# myFunc("Brian")

# Default Parameter Values
# we can assign default values to parameters if the function is called without an argument
# it uses the default value
def myFunc(name = "Friend"):
    print("Hello", name)
myFunc("Emil")
myFunc("Tobias")
myFunc()
myFunc("Linus")
# default value for country parameter
def myFunc(country = "Norway"):
    print("Im from", country)
myFunc("Sweden")
myFunc("India")
myFunc()
myFunc("Brazil")

# Keyword Arguments
# we can send arguments with the ket = value syntax
def myFunc(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
myFunc(animal = "Dog", name = "Buddy")
# this way with Keyword arguments the order of the arguments does not matter
myFunc(name = "Buddy", animal = "Dog")
# the phrase Keyword Arguments is often shortened to kwargs in python documentation

# Positional Arguments
# when we call a function with arguments without using keywords they are called positional arguments
# positional arguments must be in the correct order
def myFunc(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
myFunc("Dog", "Buddy")
# the order matters with positional arguments
myFunc("Buddy", "Dog")

# Mixing Positional and Keyword Arguments
# we can mix positional and keyword arguments in a function call
# however positional arguments must come before keyword arguments
def myFunc(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)
myFunc("Dog", name = "Buddy", age = 5)

# Passing Different Data Types
# we can send any data type as an argument to a function(string, number, list, dict, etc.)
# the data type will be preserved inside the function
# sending a list as an argument
def myFunc(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits = ["apple", "banana", "cherry"]
myFunc(my_fruits)
# sending a dictionary as an argument
def myFunc(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
my_person = {"name":"Emil", "age":"25"}
myFunc(my_person)

# Return Values
# functions can return values using the return statement
def myFunc(x, y):
    return x + y
result = myFunc(5, 8)
print(result)

# Returning Different Data Types
# functions can return any data type including list, tuple, dictionary and more
# function that returns a list
def myFunc():
    return ["apple", "banana", "cherry"]
fruits = myFunc()
print(fruits[0])
print(fruits[1])
print(fruits[2])
# function that returns a tuple
def myFunc():
    return (10,20)
x, y = myFunc()
print("x:", x)
print("y:", y)

# Positional-Only Arguments
# we can specify that a function can have only positional arguments
# to specify positional-only arguments add ,/ after the arguments
def myFunc(name, /):
    print("Hello", name)
myFunc("Emil")
# without the ,/ we are actually allowed to use keyword arguments even if the function expects positional arguments
def myFunc(name):
    print("Hello", name)
myFunc(name = "Chicken")
# with ,/ we will get an error if we try to use keyword arguments
# def myFunc(name, /):
#   print("Hello", name)
# myFunc(name = "Emil")

# Keyword-Only Arguments
# to specify that a function can have only keyword arguments add *, before the arguments
def myFunc(*, name):
    print("Hello", name)
myFunc(name = "Emil")
# without *, we are allowed to use positional arguments even if the function expects keyword arguments
def myFunc(name):
    print("Hello", name)
myFunc("Emil")
# with *, we will get an error if we try to use positional arguments
# def myFunc(*, name):
#   print("Hello", name)
# myFunc("Emil")

# Combining Positional-Only and Keyword-Only
# we can combine both argument types in the same function
# arguments before / are positional-only and arguments are after * are keyword-only
def myFunc(a, b, /, *, c, d):
    return a + b + c + d

result = myFunc(5, 10, c = 15, d = 20)
print(result)
