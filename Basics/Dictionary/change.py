# Change Dictionary Items
# Change Values
# we can change the value of a specific item by reffering to its key name
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
}
thisdict["year"] = "2020"
print(thisdict)

# Update Dictionary
# the Update() method will update the dictionary with the items from the given argument
# the argument must be a dictionary or an iterable object with key:value pairs
thisdict.update({"year":"2026"})
print(thisdict)
