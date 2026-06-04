# For Loop
# a for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
# this is less like the for keyword in other programming languages and works more like an iterator method as found in other object-oriented programming languages
# with the for loop we can execute a set of statements once for each item in a list, tuple, set etc
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# the for loop does not require an indexing variable to set beforehand

# Looping Through a String
# even strings are iterable object they contain a sequence of characters
for x in "banana":
    print(x)

# The break Statement
# with the break statement we can stop the loop before it has looped through all the items
# exit the loop when x is "banana"
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
# exit the loop when x is "banana", but this time the break comes before the print
for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue Statement
# with the continue statement we can stop the current iteration of the loop and continue with the next
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
# to loop through a set of code a specified number of times we can use the range() function
# the range() function returns a sequence  of numbers, starting from 0 by default and increments by 1(by default) and ends at a specified number
for x in range(6):
    print(x)
# Note that range(6) is not the values of 0 to 6 but the values of 0 to 5
# the range() function default to 0 as starting value however it is possible to specify the starting value by adding a parameter: range(2, 6) which means values from 2 to 6(but not including 6)
for x in range(2, 6):
    print(x)
# The range() function defaults to incremennt the sequence by 1 however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
for x in range(2, 30, 3):
    print(x)

# Else in For Loop.
# the else keyword in a for loop specifies a block of code to be executed when the loop is finished
for x in range(6):
    print(x)
else:
    print("Finished")
# Note: The else block will NOT be executed if the loop is stopped by a break statement
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

# Nested Loops
# a nested loop is a loop inside a loop
# the "inner loop" will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# The pass Statement
# for loops cannot be empty but if we for some reason have a for loop with no content put in the pass statement to avoid getting an error
for x in [0, 1, 2]:
    pass
