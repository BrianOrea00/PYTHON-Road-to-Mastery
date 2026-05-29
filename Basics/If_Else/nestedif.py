# Nested If
# Nested If Statements
# we can have if statements inside if statements
# this is called nested if statements
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20")
    else:
        print("but not above 20")

# How Nested If Works
# each level of nesting creates a deeper level of deecision making
# the code evaluates from the outermost condition inward
age = 25
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need license")
else:
    print("You are too young to drive")

# Multiple Levels of Nesting
# we can nest as many levels deep as needed but keep that in mind that too many levels can make codee harder to read
score = 85
attendance = 90
submitted = True
if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")

# Nested If vs Logical Operators
# sometimes nested if statements can be simplified using logical operators like "and"
# the choice depends on our logic
# this is nested if
temperature = 25
is_sunny = True
if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")

# could also be written in "and"
if temperature > 20 and is_sunny:
    print("Perfect beach weather!")


