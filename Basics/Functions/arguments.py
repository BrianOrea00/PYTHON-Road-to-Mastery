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
