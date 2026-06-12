# Decorators
# decorators lets us add extra behavior to a function without changing the functions code
# a decorator is a function that takes another function as input and returns a new function

# Basic Decorator
# define the decorator first then apply it with @decorator_name above the function
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myFunc():
    return "Hello Sally"
print(myFunc())
# by placing @changecase directly above the function definition the function myFunc is being "decorated" with the changecase function
# the function changecase is th decorator
# the function myFunc is the function that gets decorated

# Multiple decorator Calls
# a decorator can be multiple times just place the decorator above the function we want to decorate
def changecase(func):
    def myinner():
        return 
