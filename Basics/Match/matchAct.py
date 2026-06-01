# AI generated problem

# 1. Create:
day =2
# Use match to print the day name
# 2. Create:
color = "red"
# Print "Stop" if red
# 3. Add a default case (_)
# 4. Use one case for:
# 6 and 7
# print "Weekend"
# 5. Create:
command = "start"
# handle start and stop
# 6. Explain (comment):
# what match does
# 7. Explain (comment):
# what case _ means
# 8. Explain (comment):
# difference between match and if/elif
# 9. Predict:
status = "open"
# match status:
#     case "open":
#         print("Opened")
#     case _:
#         print("Unknown")
# What prints?
# 10. Predict:
number = 5
# match number:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case _:
#         print("Other")
# What prints?

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

match color:
    case "green":
        print("go")
    case "yellow":
        print("ready")
    case "red":
        print("stop")

    case _:
        print("Traffic light")

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:
        print("Weekend")

match command:
    case "start":
        print("Welcome")
    case "stop":
        print("Please Log in")

# match compares a value against multiple cases
# and executes the block of the first matching case

# the case _ patterns acts as wildcard catch-all that matches any value not previously captured
# functioning similarly to an else statement

# while if/else evaluates conditions based on general boolean logic (true/false expressions)
# match focuses specifically in structural pattern matching and value extraction

# my prediction is it willl print "Opened"

# my prediction is it will print "Other"
