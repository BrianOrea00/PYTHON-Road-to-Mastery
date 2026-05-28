# Logical Operators
# Logical operators are used to combine conditional statements
# Python provides three logical operators
# and - returns True if both statements are true
# or - returns True if at least one statement is true
# not - reverses the result, returns True if the result is false

# the and operator
# the and keyword is a logical operator and is used to combine conditional statements
# both conditions must be true for the entire expression to be true
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true")

# the or operator
# the or keyword is a logical operator and is used to combine conditional statements
# at least one condition must be true for the entire expression to be true
if a > b or a > c:
    print("At least one condition is true")

# the not operator
# the not keyword is a logical operator and is used to reverse the result of the conditional statement
if not a > b:
    print("a is not greater than b")

# combining multiple operators
# we can combine multiple logical operators in a single expression
# python evaluates not first then and then or
age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applied")

# using parentheses for clarity
# when combining multiple logical operators use parentheses to make our intentions clear and control the order of evaluation
temperature = 25
is_raining = False
is_weekend = True
if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")