# AI generated problem

# 1. Print numbers 1 to 5 using while
# 2. Print numbers 5 to 1 using while
# 3. Print even numbers from 2 to 10
# 4. Use break:
# stop when number reaches 4
# 5. Use continue:
# skip number 3
# 6. Use while else:
# print "Finished" after loop ends
# 7. Explain (comment):
# what a while loop does
# 8. Explain (comment):
# what break does
# 9. Explain (comment):
# what continue does
# 10. Explain (comment):
# what happens if we forget to update the loop variable

i = 1
while i <= 5:
    print(i)
    i += 1

i = 5
while i >= 1:
    print(i)
    i -= 1  
    
i = 2
while i <= 10:
    print(i)
    i += 2
    
i = 1
while i <= 5:
    print(i)
    if i == 4:
        break
    i += 1
    
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
    
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Finished")
    
# A while loop is a control flow statement that allows code to be executed repeatedly based on a given boolean condition. The loop will continue to execute as long as the condition is true.

# The break statement is used to exit a loop prematurely, even if the loop's condition is still true. When a break statement is encountered, the loop will immediately terminate and control will be passed to the next statement after the loop.

# The continue statement is used to skip the current iteration of a loop and move on to the next iteration. When a continue statement is encountered, the rest of the code inside the loop for that iteration will be skipped, and the loop will proceed with the next iteration.

# If we forget to update the loop variable, the condition for the while loop will never become false, resulting in an infinite loop. This means that the loop will continue to execute indefinitely, which can cause the program to crash or become unresponsive.