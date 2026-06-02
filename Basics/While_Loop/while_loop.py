# While Loop
# Python Loops
# python has two primitive loop commands
# while loops
# for loops
# the wile loop executes a set of statements as long as a condition is true
i = 1
while i < 6:
    print(i)
    i += 1
# Note: remember to increment i, or else the loop will continue forever
# the while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1
# the break statement
# the break statement can be used to stop a while loop even if the while condition is true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# the continue statement
# the continue statement can be used to stop the current iteration of the loop, and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# the else statement
# with the else statement we can run a block of code oncce when the condition no longer is true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# Note: the else block will NOT be executed if the loop is stopped by a break statement