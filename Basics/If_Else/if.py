# If Statement
# Python Conditions and if statements
# python supports the usual logic conditions from mathematics
# > equals: a == b
# > not equals: a != b
# > less than: a < b
# > less than or equal to: a <= b
# > greater than: a > b
# > greater than or equal to: a >= b
# these conditions can be used in several ways most commonly in "if Statements" and loops
# an "if statement" is written by using the "if" keyword
a = 33
b = 200
if b > a:
    print("b is greater than a")

# How If Statements Work
# the if statement evaluates a condition (an expression that results in True or False)
# if the condition is True the code block inside the if statement is executed
# if the condition is False the code block iss skipped
num = 25
if num > 0:
    print("the number is positive")

# Indentation
# python relies on indentation (whitespace at the beginning of a line) to define scope in the code other programming languages often use curly-brackets for this purpose
# a = 33
# b = 200
# if b > a:
# print("b is greater than a") you will get an error

# Note: You can use spaces or tabs for indentation, but you must use the same amount of indentation for all statements within the same code block

# Multiple Statements in If Block
# we can have multiple statements inside an if block all statements must be indented at the same level
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")

# Using Variables in Conditions
# boolean variables can be used directly in if statements without comparison operators
is_logged_in = True
if is_logged_in:
    print("Welcome Back")
# Python can evaluate many types of values as True or False in an if statement
# Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True
# This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string)
