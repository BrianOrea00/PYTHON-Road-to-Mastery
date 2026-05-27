# Shorthand If
# Short Hand If
# if we have only one statement to execute we can put it on the same line as the if statement
a = 5
b = 3
if a > b: print("a is greater than b")
# Note: We still need the colon : after the condition

# Short Hand If ... Else
# if we have one statement for if and one for else we can put them on the same line using a conditional expression
a = 2
b = 330
print("A") if a > b else print("B")
# this is called a conditional expression (sometimes known as a "ternary operator")

# Assign a Value With If ... Else
# we can also use a one line if / else to choose a value and assign it to a variable
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# Multiple Conditions on One Line
# we can chain conditional expressions but keep it short so it stays readable
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# When to Use Shorthand If
# Shorthand if statements and ternary operators should be used when

#   The condition and actions are simple
#   It improves code readability
#   You want to make a quick assignment based on a condition

