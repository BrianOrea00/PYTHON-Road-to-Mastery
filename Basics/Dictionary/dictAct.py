# AI generated problem

# 1. Create dictionary with:
# name, age, course
# 2. Print dictionary
# 3. Print value of "name"
# 4. Print number of key-value pairs
# 5. Create dictionary with mixed data types
# 6. Create dictionary using dict()
# 7. Create dictionary with duplicate key
# and observe output
# 8. Explain (comment):
# what key-value pair means
# 9. Explain (comment):
# why duplicate keys are not allowed
# 10. Explain (comment):
# difference between list and dictionary

student = {
    "name": "Brian",
    "age": "23",
    "course": "Computer Science"
}

print(student)

print(student["name"])

print(len(student))

mixDict = {
    "name" : "Brian",
    "age" : 23,
    "is_student" : True,
    "subjects" : ["NLP", "Thesis", "CS electives"]
}
print(mixDict)

thisdict = dict(redFruit = "Apple", greenFruit = "Kiwi", yellowFruit = "Banana")
print(thisdict)

dupDict = {
    "redFruit": "Apple",
    "greenFruit": "Kiwi",
    "yellowFruit": "Banana",
    "redFruit": "Strawberry"
}
print(dupDict)

# In a dictionary, a key-value pair is a set of two associated elements: a key (which is unique) and a value.
# The key is used to access the value in the dictionary.

# Duplicate keys are not allowed in a dictionary because each key must uniquely identify its value.
# If a duplicate key is added, the original key-value pair is overwritten by the new one.

# a list stores items accessed by numerical index,
# while a dictionary stores data as key-value pairs accessed by keys