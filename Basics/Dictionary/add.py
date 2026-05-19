# Add Dictionary Items
# Adding Items
# adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["color"] = "red"
print(thisdict)

# Update Dictionary
# the update() method will update the dictionary with the items frrom a given argument if the items does not exist the item will be added
# the argument must be a dictionary or an iterable object with key:value pairs
thisdict.update({"color": "black"})
print(thisdict)
