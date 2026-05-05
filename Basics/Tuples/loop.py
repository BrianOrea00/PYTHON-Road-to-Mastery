# Loop Tuple
# Loop through a Tuple
# we can loop through the tuple items by using a "for" loop
thistuple1 = ("apple", "banana", "cherry")
for x in thistuple1:
    print(x)

# Loop through the index Numbers
# we can loop through the tuple items by referring to their index number
# use the range() and len() functions to create a suitable iterable
for i in range(len(thistuple1)):
    print(thistuple1[i])

# Using a While Loop
# we can loop through the tuple items by using a while loop
# use the len() function to determine the length of the tuple then start at 0 and loop our way through the tuple items by referring to their indexes
# remember to increase the index by 1 after each iteration
i = 0
while i < len(thistuple1):
    print(thistuple1[i])
    i += 1
