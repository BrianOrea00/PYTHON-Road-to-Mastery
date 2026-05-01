# Tuples
# tuples are used to store items in a single variable
# tuple is one of 4 built in data types in python used to store collections of data the other are List, Set, and Dictionary all different qualities and usage
# A tuple is a collection which ordered and unchangeable
# tuples are written with round brackets
thistuple1 = ("apple", "banana", "cherry")
print(thistuple1)

# Tuple items
# tuple items are ordered, unchangeable, and allows duplicate values
# tuple items are indexed the first has index [0] then [1] and so on
#
# Ordered
# when we say that tuples are ordered it means that the items have a defined order and that order will not change

# Unchangeable
# tuples are unchangeable meaning that we cannot change add or remove items after the tuple has been created

# Allows duplicate
# since tuple are indexed they can have items with the same value
thistuple2 = ("a", "b", "c", "a")
print(thistuple2)

# Tuple length
# to determine how many items a tuple has use the len() function
print(len(thistuple1))

# Create tuple with one item
# to create a tuple with only on item we have to add a comma after the item otherwise python will not recognize is as a tuple
thistuple3 = ("one",)
print(type(thistuple3))

thistuple4 = ("one")
print(type(thistuple4))

# Tuple items - data types
# tuple items can be of any data types
# we have here str, int and boolean types
thistuple5 = ("a", "b", "c")
thistuple6 = (1, 2, 3)
thistuple7 = (True, False, True)

print(thistuple5)
print(thistuple6)
print(thistuple7)
# a tuple can contain different data types
thistuple8 = ("hi", 69, True)
print(thistuple8)

# Tuple() Constructor
# it is also possible to use the tuple() constructor to make a tuple
thistuple9 = tuple(("yes", "the", "best"))
print(type(thistuple9))
