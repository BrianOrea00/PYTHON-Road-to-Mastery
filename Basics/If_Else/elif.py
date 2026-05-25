# Elif Statement
# The Elif keyword
# the elif keyword is python's way of saying "if the previous conditions were not True then try this condition"
# the elif keyword allows us to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True
a = 33
b = 33
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")

# Multiple Elif Statements
# we can have as many elif statements as we need
# python will check each conditions in order and execute the first one that is True
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

# How Elif Works
# when we use elif python evaluates the conditions from top to bottom as soon as it finds a condition that is True it executes that block of code and skips all remaing conditions
# IMPORTANT: only the first true condition will be executed even if multiple conditions are True python stops after executing the first matching block
age = 23
if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teen")
elif age < 65:
    print("You are a adult")
elif age >= 65:
    print("You are a senior")

# When to Use Elif
# use elif when we have multiple exclusive conditions to check
# this is more efficient than using multiple separate if statements because python stops checking once it finds a True condition
day = 6
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
