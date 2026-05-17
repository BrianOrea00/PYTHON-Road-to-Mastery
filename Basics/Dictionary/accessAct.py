# AI generated problem

# 1. Create dictionary with:
# brand, model, year
# 2. Print the dictionary
# 3. Print value of "model"
# 4. Print all keys in the dictionary
# 5. Print all values in the dictionary
# 6. Use get() method to access "brand"
# 7. Check if "year" key exists in dictionary
# 8. Explain (comment):
# what keys() method does
# 9. Explain (comment):
# what values() method does
# 10. Explain (comment):
# difference between get() and square brackets []

laptop = {
    "brand" : "SAMSUNG",
    "model" : "RC510",
    "year" : 2011
}

print(laptop)

print(laptop["model"])

key = laptop.keys()
print(key)

value = laptop.values()
print(value)

getBrand = laptop.get("brand")
print(get)

if "year" in laptop:
    print("Yes, the key \"year\" exists")

# The keys() method returns a view object containing a list of all the keys present in the dictionary

# The values() method returns a view object containing a list of all the values stored in the dictionary

# While both retrieve a value, square brackets [] raise a KeyError if the key does not exist, whereas the get() method safely returns None or a specified default value
