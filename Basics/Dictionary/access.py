# Access Dictionary Items
# Accessing Items
# we can access the items of a dictionary by referring to its key name inside square brackets
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
}
x = thisdict["model"]
print(x)
# there is also a method called get() that will give us same result
x = thisdict.get("year")
print(x)

# Get Keys
# the keys() method will return a list of all keys in the dictionary
x = thisdict.keys()
print(x)
# the list of the keys is a view of the dictionary meaning that any changes done to the dictionary will be reflected in the keys list
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
}
x = car.keys()
print(x)
car["color"] = "white"
print(x)

# Get Values
# the values() method will return a list of all the values in the dictionary
x = thisdict.values()
print(x)
# the list of the values is a view of the dictionary meaning that any changes done to the dictionary will be reflected in the values list
x = car.values()
print(x)
car["year"] = "2020"
print(x)

# Get Items
# the items() method will return each items in a dictionary as tuples in a list
x = thisdict.items()
print(x)
# the returrned list is a view of the items of the dictionary meaning that any changes done to the dictionary will be reflected in the items list
x = car.items()
print(x)
car["year"] = "2026"
print(x)

# Check if Key Existed
# to determine if a specified key is present in a dictionary use the in keyword
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


