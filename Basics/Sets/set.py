# Sets
# sets are used to store multiple items in a single variable
# Set is one of 4 built in data types in python used to store collections of data the other 3 are List, Tuple, and Dictionary all with diferent qualities and usage
# a set is a collection which is unordered, unchangeable, and unidexed
# Note: Set items are unchangeable but we can remove items and add new items
# Sets are written with curly brackets
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Note: Sets are unordered so we cannot sure in which order the items will appear

# Set items
# set items are unordered, unchangeable, and do not allow duplicate value

# Unordered
# unordered means that the items in a set do not have a defined order
# set items can appear in a diferent order every time we use them and cannot be referred to by index or key

# Unchangeable
# set items are unchangeable meaning that we cannot change the items after the set has been created

# Duplicates Not Allowed
# sets cannot have two items with the same value
thisset2 = {"apple", "apple", "banana", "cherry"}
print(thisset2)
# Note: The values True and 1 are considered the same value in sets and are treated as duplicates
thisset3 = {"apple", True, 1, 2}
print(thisset3)
# Note: The values False and 0 are considered the same value in sets and are treated as duplicates
thisset4 = {"banana", False, 0, 333}
print(thisset4)

# Get the Length of a Set
# to determine how many items a set has use the len() function
print(len(thisset))

# Set items - Data types
# set items can be of any data types
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {True, False}
print(type(set1))
print(type(set2))
print(type(set3))
# a set can contain diferent data types
set4 = {"a", 1, True}
print(set4)

# The set() Constructor
# it is also possible to use the set() constructor to make a set
thisset5 = set(("apple", "banana", "cherry"))
print(thisset5)
