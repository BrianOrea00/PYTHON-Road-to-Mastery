# Loop Dictionary
# Loop through a dictionary
# we can loop through a dictionary by using "for" loop
# when looping through a dictionary the return value are the keys of the dictionary but there are methods to return the value as well
# print all key names in the dictionary one by one
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)

# print all values in the dictionary one by one
for x in thisdict:
    print(thisdict[x])

# we can also use the values() method to return values of a dictionary
for x in thisdict.values():
    print(x)

# we can use the keys() method to return the key of a dictionary
for x in thisdict.keys():
    print(x)

# loop through both keys and values by using the items() method
for x, y in thisdict.items():
    print(x, y)
