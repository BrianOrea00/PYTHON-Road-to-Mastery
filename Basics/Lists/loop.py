# Loop List
# loop through a list
# we can loop through the list items by using a "for" loop
thisist = ["Apple", "Banana", "Cherry"]
for x in thisist:
    print(x)

# Loop through the index numbers
# we can also loop through the list items by referring to their index numbers
# use the range() and len() functions to create a suitable iterable
for y in range(len(thisist)):
    print(thisist[y])
# the iterable created in here is [0, 1, 2]

# Using a While loop
# we can loop through the list items by using "while" loop
# use the len() function to determine the length if the list then start at 0 and loop through the list items by referring to their indexes
# remember to increase the index by 1 after each iteration
z = 0
while z < len(thisist):
    print(thisist[z])
    z = z + 1

# Looping using list comprehension
# this offers the shortest syntax for Looping through list
[print(a) for a in thisist]
