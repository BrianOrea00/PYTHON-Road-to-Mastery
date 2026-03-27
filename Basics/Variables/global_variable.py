# Global Variable
# Its a variable that is created outside the function 
# this variable can be used inside and outside the function
# example1
x = "Mastery"
def myfunc1():
    print("Road to "+ x)
myfunc1()

# we can also create variable with same name inside the function then this will be local
# meaning that local can be used inside the function only
# then the global can be used as it is
# example2
y = "Mastery"
def myfunc2():
    print("Road to "+ y)
myfunc2()
print(y + " is the key to success!")

# the next one is to create a global variable inside the function
# normally when we create a variable inside the function that variable is local right?
# but we can use the keyword "global" to make it global variable
# example3
def myfunc3():
    global z
    z = "tricky"
myfunc3()   
print("this one is kinda " + z)

# another one in here we can rewrite the value of the global variable 
# by using the keyword "global" inside the function
# example4
a = "Hotdog"
def myfunc4():
    global a
    a = "Adobo"
myfunc4()
print("My fav Food is "+ a)

