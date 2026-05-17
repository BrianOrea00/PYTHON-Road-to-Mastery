# Dictionary
# dictionaries are used to store data values in key:value pairs
# a dictionary is a collection which is ordered, changeable and does not allow duplicates
# dictionaries are written with curly brackets, and have keys and values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dictionary Items
# dictionary items are ordered pairs of keys and values
# you can access the items of a dictionary by referring to its key name
print(thisdict["brand"])

# Ordered or Unordered
# when we say that dictionaries are ordered it means that the items have a defined order and that order will not change
# unordered means that the items do not have a defined order we cannot refer to an item by using an index

# Changeable
# dictionaries are changeable meaning that we can change, add, remove items after the dictionary has been created

# Duplicates not allowed
# dictionaries cannot have two items with the same key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

# Dictionary Length
# to determine how many items a dictionary has, use the len() function
print(len(thisdict))

# Dictionary Items - Data types
# the values in dictionary items can be of any data type
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "electric": False,
    "colors": ["red", "white", "blue"]
}
print(thisdict)

# Type()
# from python perspective dictionaries are defined as objects with the data type "dict"
print(type(thisdict))

# the dict() constructor
# it is also possible to create a dictionary using the dict() constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)