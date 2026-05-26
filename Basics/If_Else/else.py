# Else Statement
# The Else Keyword
# the else keyword catches anything which isn't caught by the preceding conditions
# the else statement is executed when the if condition evaluate to False
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Else without Elif
# we can also have an else without the elif
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# How Else Works
# the else statement provides a default actiion when none of the previous conditions are True
# think of it as a "catch-all" for any scenario not covered by your if and elif statements
# Note: The else statement must come last we cannot have an elif after an else
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Complete If-Elif-Else Chain
# we can combine if, elif, and else to create a comprehensive decision-making structure
temperature = 22
if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside!")

# Else as Fallback
# the else statement act as a fallback that executes when none of the preceding conditions are True
# this makes it useful for error handling, validation, and providing default values
username = "Brian"
if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty")
