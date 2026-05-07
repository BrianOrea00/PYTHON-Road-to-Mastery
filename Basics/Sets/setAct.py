# AI generated problem

# 1. Create a set with 3 fruits
# 2. Print the set
# 3. Create a set with duplicate values
# and observe output
# 4. Print length of set
# 5. Create a set with mixed data types
# 6. Check type of set
# 7. Create empty set correctly
# 8. Check if "apple" exists in set
# 9. Explain (comment):
# why sets do not allow duplicates
# 10. Explain (comment):
# why sets cannot use indexing

fruits = {"mango", "grapes", "apple"}

print(fruits)

dupSet = {1, 1, 1, 2, 3}
print(dupSet)

print(len(fruits))

mixSet = {"a", 99, True}
print(mixSet)

print(type(fruits))

empSet = set()

if "apple" in fruits:
    print("exists")

# sets use hashing to assign each item a unique position in memory so attempting to add a duplicate simply points to an existing entry rather than creating a new one

# sets are unordered collections where the internal position of an element in determined by its hash value and can shift during resizing making a fixed numerical index unreliable
