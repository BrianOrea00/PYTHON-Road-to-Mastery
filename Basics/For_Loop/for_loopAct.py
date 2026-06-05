# AI generated problem

fruits = ["apple", "banana", "cherry"]

# 1. Print all fruits using for loop
# 2. Print each character in:
# "python"
# 3. Use break:
# stop when fruit is "banana"
# 4. Use continue:
# skip "banana"
# 5. Use else:
# print "Done"
# 6. Count fruits using loop
# (not len)
# 7. Explain (comment):
# what a for loop does
# 8. Explain (comment):
# difference between for and while
# 9. Explain (comment):
# what break does in a for loop
# 10. Explain (comment):
# what continue does in a for loop

for x in fruits:
    print(x)

for x in "python":
    print(x)

for x in fruits:
    print(x)
    if x == "banana":
        break

for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(3):
    print(x)
else:
    print("Done")

count = 0
for x in fruits:
    count += 1
print(count)

# a for loop repeats a block of code a specific number of times
# typically by iterating over a sequence like a lisst, tuple, or range

# a for loop iterates over a predetermined sequence or range
# whereas a while loop repeats indefinitely as long as a specified condition remains true

# the break statement immediately terminates the loop entirely and jumps to the next code block outside of it

# the continue statement skips the rest of the code in the current iteration and jumps straight to the next turn of the loop
