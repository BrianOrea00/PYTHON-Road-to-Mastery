# AI generated problem

# 1. Create a function using *args
# and print the whole tuple
# 2. Call it with three values
# 3. Print the first value from *args
# 4. Explain (comment):
# what type of object *args becomes
# 5. Create a function using **kwargs
# and print the whole dictionary
# 6. Call it with:
# fname="Brian"
# age=23
# 7. Print only age
# 8. Explain (comment):
# what type of object **kwargs becomes
# 9. Explain (comment):
# difference between *args and **kwargs
# 10. Predict:
def test(*x):
    print(x[2])
# test(1, 2, 3, 4)
# What will be printed?

def myFunc(*args):
    print(args)
    
myFunc("Emil", "Tobias", "Linus")

def myFunc(*args):
    print(args[0])
myFunc(100, 200, 300)

# *args becomes a tuple containing all positional arguments passed to the function

def myFunc(**kwargs):
    print(kwargs)
    print(kwargs["age"])

myFunc(fname="Brian", age=23)


# **kwargs becomes a dictionary containing all keyword arguments passed to the function

# *args captures variable-length positional arguments as a tuple, while **kwargs captures variable-length keyword arguments as a dictionary.

# it will print 3 because we can index the tuple x and access the third element which is 3.