# AI generated problem

students = {
    "student1": {
        "name": "Brian",
        "age": 23
    },

    "student2": {
        "name": "Alice",
        "age": 21
    }
}

# 1. Print student1 name
# 2. Print student2 age
# 3. Add:
# "course" = "BSCS"
# to student1
# 4. Change student2 age to 22
# 5. Loop through outer dictionary keys
# 6. Loop through all nested key-value pairs
# 7. Explain (comment):
# what nested dictionary means
# 8. Explain (comment):
# why nested dictionaries are useful
# 9. Predict:
# what does this print?
# print(students["student1"]["age"])
# 10. Explain (comment):
# difference between normal and nested dictionary

print(students["student1"]["name"])

print(students["student2"]["age"])

students["student1"]["course"] = "BSCS"
print(students)

students["student2"]["age"] = 22
print(students)

for x in students.keys():
    print(x)

for y, obj in students.items():
    print(y)
    for z in obj:
        print(z, ':', obj[z])

# a nested dictionary is a dictionary that contains other dictionaries as its values

# they are useful for organizing and storing complex, hierarchical data in a structured easy to read format

# a normal dictionary maps simple keys to single values
# while a nested dictionary maps keys to entire dictionaries for multi layered data
