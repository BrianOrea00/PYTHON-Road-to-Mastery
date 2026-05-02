# Access Tuple
# we can access tuple items by referring to the index number inside square brackets
thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[1])

# Negative Indexing
# negative indexing means start from the end
print(thistuple1[-1])

# Range of Indexes
# we can specify a range of indexes by specifying where to start and where to end the range
# when specifying a range the return value will be a new tuple with the specified items
thistuple2 = ("a", "b", "c", "d", "e", "f", "g")
print(thistuple2[2:5])
# by leaving out the start value the range will start at the first
print(thistuple2[:4])
# by leaving out the end value the range will go on to the end of the tuple
print(thistuple2[2:])

# Range of Negative Indexes
# specify negative indexes if we want to start the search from the end of the tuple
print(thistuple2[-4:-1])

# Check if items Existed
# to determine if a specified item is present in a tuple use the "in" keyword
if "apple" in thistuple1:
    print("Yes, apple is present")


