# Pass Statement
# The Pass Statement
# if statement cannot be empty but if we for some reason have an if statement with no content put in the pass statement to avoid getting an error
a = 33
b = 200
if a > b:
    pass

# the pass statement is a null operation - nothing happens when it executes. It serves as a placeholder

# Why Use pass?
# the pass statement is useful in several situations
# when you're creating code structure but haven't implemented the logic yet
# when a statement is required syntactically but no action is needed
# as a placeholder for future code during development
# in empty functions or classes that you plan to implement later

# pass in development
# during development you might want to sketch out our program structure before implementing the details
# the pass statement allows us to do this without syntax errors

age = 16
if age < 18:
    pass # TODO: add underage logic later
else:
    print("Access Granted")

# pass vs comments
# a comment is ignored by python but pass is an actual statement that gets executed (thought it does nothing)
# we need pass where python expects a statement not just a comment
# score = 85
# if score > 90:
#   # this is excellent
# this will raise an IndentationError

# this works correctly with pass
score = 85

if score > 90:
    pass # This is excellent
print("Score processed")

# pass with multiple conditions
# we can use pass in any branch of an if-elif-else statement
value = 50
if value < 0:
    print("Negative value")
elif value == 0:
    pass # Zero case - no action needed
else:
    print("Positive")

# pass in other contexts
# while we focus on pass with if statements here its also commonly used with loops, functions, and classes
def calculate_discount(price):
    pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet
