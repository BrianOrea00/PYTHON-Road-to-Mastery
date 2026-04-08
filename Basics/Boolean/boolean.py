# Boolean
# represents one of two values: True and False.
# in programming we often need to know of an expression is true or false.
# we can evaluate any expression in python and get one of two answers.
# when we compare two values the expression is evaluated and python returns the boolean answer.
# example1
print(10 > 9)
print(10 == 10)
print(10 < 9)

# when we run a condition in an if statement python returns true or false.
# example2
a = 66
b = 34

if b > a:
    print("A is less than B")
else:
    print("A is greater than B")

# evaluate values and variables
# the bool() function allows us to evaluate any value and give us true or false in return.
# example3
print(bool("Heloo World"))
print(bool(99))
# or we can also this.
c = "Text"
d = 66
print(bool(c))
print(bool(d))

# most values are true
# almost any value is evaluated to true if it has some sort of content.
# any string is true except empty string.
# any number is true except 0.
# any list,tuple,set, and dict are true except empty  ones.
# example4
print(bool("string"))
print(bool(11))
print(bool(["Hotdog","Adobo","Bulalo"]))

# some values are false
# there are not many values that evaluate to false except empty values such as (),[],{},"", and 0 and the value None and of course the value false evaluates false.
# example5
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# one more value or object in this case evaluates to false and that us if we have an object that is made from a class with a __len__ function that returns 0 or false.
# example6
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

# functions can return a boolean
# we can create fuunctions that returns a boolean value.
# example7
def myfunc():
    return True
print(myfunc())

# we can execute code based on the boolean answer of a function.
# example8
def myfunc2():
    return True

if myfunc2():
    print("Yes")
else:
    print("No")

# python also has many built in functions that return a boolean value like the isinstance() function which can be used to determine if an object is of a certain data type.
# example9
e = 200
print(isinstance(e, int))
