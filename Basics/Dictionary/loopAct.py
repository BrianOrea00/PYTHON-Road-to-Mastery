# AI generated problem

student = {
    "name": "Brian",
    "age": 23,
    "course": "BSCS"
}

# 1. Print all keys using loop
# 2. Print all values using values()
# 3. Print all key-value pairs using items()
# 4. Print:
# "name : Brian"
# 5. Count number of keys using loop
# (not len)
# 6. Check if "age" exists
# 7. Explain (comment):
# what items() returns
# 8. Explain (comment):
# difference between keys() and values()
# 9. Explain (comment):
# why looping directly over dictionary returns keys
# 10. Predict:
# what does this print?
# for x in student:
#     print(student[x])

for x in student:
    print(x)

for x in student.values():
    print(x)

for x, y in student.items():
    print(x, y)

for key, value in student.items():
    print(key, ":", value)

count = 0
for x in student:
    count += 1
print(count)

print("age" in student)

# The items() method returns a view object containing tuples of every key-value pair in the dictionary, allowing you to access both the label and its data simultaneously

# The keys() method returns a list like view of all the identifiers (names) in the dictionary
# whereas values() returns only the actual data (entries) associated with those identifiers

# Python is designed to prioritize the keys when looping directly over a dictionary because keys are the unique identifiers used to navigate the structure making them the most logical default for iteration

# It will print the values associated with each key in the student dictionary
