# AI generated problem

student = {
    "name": "Brian",
    "age": 23,
    "course": "BSCS"
}

# 1. Change age to 24
# 2. Change course to "Computer Science"
# 3. Add new key:
# "year" = 2026
# 4. Use update() to change name
# 5. Use update() to add:
# "school" = "XYZ University"
# 6. Print all keys
# 7. Print all values
# 8. Explain (comment):
# what happens when assigning to an existing key
# 9. Explain (comment):
# difference between update() and direct assignment
# 10. Explain (comment):
# why dictionaries are considered mutable

student["age"] = 24
print(student)

student["course"] = "Computer Science"
print(student)

student["year"] = 2026
print(student)

student.update({"name" : "Brian Orea"})
print(student)

student.update({"school" : "XYZ University"})
print(student)

print(student.keys())

print(student.values())

# assigning a value to an existing key overwrites its current value with the new one

# direct assignment modifies or adds a single key-value pair whereas the update() method can modify or merge multiple
# key-value pairs at once using another dictionary or iterable

# dictionaries are considered mutable because we can change, add, or remove their elements after the dictionary has been created without changing its memory identity
