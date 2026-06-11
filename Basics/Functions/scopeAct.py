# AI generated problem

# 1. Create a local variable x = 10
# inside a function and print it
# 2. Explain what happens if you
# print x outside the function
# 3. Create a global variable name
# and print it inside a function
# 4. Create a local variable with the
# same name as a global variable
# 5. Show that local and global variables
# are different
# 6. Create a function inside a function
# and access the outer variable
# 7. Use global keyword to create
# a global variable inside a function
# 8. Explain (comment):
# what local scope means
# 9. Explain (comment):
# what global scope means
# 10. Predict:
x = "Outside"
def test():
    x = "Inside"
    print(x)
test()
print(x)
# What will be printed?

def myFunc():
    x = 10
    print(x)
myFunc()

# If you print x outside the function, it will raise a NameError because x is a local variable and is not accessible outside the function.

name = "Global Name"
def printName():
    print(name)
printName()

name = "Global Name"
def localGlobal():
    name = "Local Name"
    print(name)
localGlobal()
print(name)

def outerFunction():
    outerVar = "Outer Variable"
    def innerFunction():
        print(outerVar)
    innerFunction()
outerFunction()

def createGlobal():
    global globalVar
    globalVar = "I am a global variable"
createGlobal()
print(globalVar)

# Local scope means that a variable defined inside a function is only accessible within that function. It cannot be accessed outside the function.

# Global scope means that a variable defined outside of any function is accessible from anywhere in the code, including inside functions.

# The output of the code will be: Inside Outside