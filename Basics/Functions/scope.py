# Scope
# a variable is only available from inside the region it is created
# this is called scope
# Local Scope
# a variable created inside the function belongs to the local scope of that function
# and can only be used inside that function
def myFunc():
    x = 300
    print(x)
myFunc()

# Function inside Function
# as explained in the example above the variable x is not available outside the function
# but its available for any function inside the function
def myFunc():
    x = 300
    def myinnerFunc():
        print(x)
    myinnerFunc()
myFunc()

# Global Scope
# a variable created in the main body of the code is a global variable and belongs to the global scope
# global variable are available from withon the scope, global and local
x = 400
def myFunc():
    print(x)
myFunc()
print(x)

# Naming Variables
# if we operate with the same variable name inside and outside fo a function
# python will treat them as two separate variables
# one available in the global scope and one available in the local scope
x = 10
def myFunc():
    x = 11
    print(x)
myFunc()
print(x)

# Global Keyword
# if we need to create a global variable but are stuck in the local scope we can use the global keyword
# the global keyword makes the variable global
def myFunc():
    global x
    x = 99
myFunc()
print(x)
# also use the global keyword if we want to make a change to a global variable inside a function
x = 300
def myFunc():
    global x
    x = 200
myFunc()
print(x)

# Nonlocal Keyword
# the nonlocal keyword is used to work with variables inside nested functions
# the nonlocal keyword makes the variable belongs to the outer function
def myFunc():
    x = "Jane"
    def myFunc2():
        nonlocal x
        x = "Hello"
    myFunc2()
    return x
print(myFunc())

# The LEGB Rule
# python follows the LEGB rule when looking up variable names, and searches for them in this order
# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace
x = "Global"
def outer():
    x = "Enclosing"
    def inner():
        x = "Local"
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()
print("Global:", x)
