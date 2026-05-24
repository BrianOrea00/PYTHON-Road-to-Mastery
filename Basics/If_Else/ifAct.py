# AI generated problem

a = 10
b = 20

# 1. Print:
# "b is greater"
# if b > a
# 2. Print:
# "a is positive"
# if a > 0
# 3. Create boolean variable:
# is_admin = True
# then use it in if statement
# 4. Create:
# name = ""
# use if statement to test it
# 5. Put 2 print statements
# inside one if block
# 6. Explain (comment):
# what indentation does
# 7. Explain (comment):
# what happens if condition is False
# 8. Explain (comment):
# why boolean variables can be used directly
# 9. Predict:
# if 0:
#     print("Hello")
# will it print?
# 10. Predict:
# if "False":
#     print("Hi")
# will it print?

if b > a:
    print("b is greater than a")

if a > 0:
    print("a is positive")

is_admin = True
if is_admin:
    print("Welcome to admin page")

name = ""
if name:
    print("Hi there my name is", name)

is_student = True
if is_student:
    print("Welcome back to School")
    print("Are you ready to learn?")

# Indentation defines the structure and scope of code blocks, indicating which statements belong to a specific condition, loop, or function

# If a condition is False, the code block indented beneath it is skipped, and the program moves to the next executable line outside that block

# Boolean variables can be used directly because they already evaluate to either True or False, which is exactly what an if statement requires to make a decision

# It will not print, because the integer 0 is considered "falsy" in Python and evaluates to False

# It will print, because "False" is a non-empty string, and all non-empty strings are considered "truthy" in Python
