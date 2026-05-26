# AI generated problem

x = 10
y = 20

# 1. Print:
# "y is bigger"
# if y > x
# 2. Print:
# "Equal"
# if x == y
# otherwise print:
# "Not Equal"
# 3. Print:
# "Positive"
# if x > 0
# 4. Print:
# "Even"
# if x is divisible by 2
# otherwise print:
# "Odd"
# 5. Use elif:
# if x > 20 -> print "Large"
# elif x > 5 -> print "Medium"
# else -> print "Small"
# 6. Use and operator
# 7. Use or operator
# 8. Explain (comment):
# difference between if and elif
# 9. Explain (comment):
# what else does
# 10. Predict:
# what happens if all conditions are False

if y > x:
    print("y is bigger")

if x == y:
    print("Equal")
else:
    print("Not Equal")

if x > 0:
    print("Positive")

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

if x > 20:
    print("Large")
elif x > 5:
    print("Medium")
else:
    print("Small")

age = 23
has_license = True
if age >= 18 and has_license:
    print("You are eligible to drive")
else:
    print("You cannot drive")

is_grid_electricity = True
is_solar = False
if is_grid_electricity or is_solar:
    print("The power is ON.")
else:
    print("Blackout! No power available.")

# The if statement checks the initial condition to start a decision-making block
# while elif (short for else if) allows us to check multiple subsequent conditions only if the previous ones were False

# The else statement captures anything that wasn't caught by the preceding if or elif conditions
# acting as a final catch-all block that runs when all other conditions fail

# If all conditions are False and there is no else block provided
# the entire conditional structure is skipped and the program simply moves on to execute the next line of code
