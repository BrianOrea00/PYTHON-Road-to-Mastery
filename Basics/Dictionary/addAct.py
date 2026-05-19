# AI generated problem

student = {
    "name": "Brian"
}

# 1. Add:
# "age" = 23
# 2. Add:
# "course" = "BSCS"
# 3. Use update() to add:
# "year" = 2026
# 4. Use update() to add multiple:
# "school" and "section"
# 5. Print all keys
# 6. Print all values
# 7. Check if "course" exists
# 8. Explain (comment):
# what happens if added key already exists
# 9. Explain (comment):
# difference between adding and updating
# 10. Explain (comment):
# why dictionaries cannot have duplicate keys

student["age"] = 23
print(student)

student["course"] = "BSCS"
print(student)

student.update({"year": 2026})
print(student)

student.update({"school": "CMI", "section": "A"})
print(student)

print(student.keys())

print(student.values())

print("course" in student)

# it will overwrite the existing keys value with the new value we provided

# adding inserts a brand new key-value pair into the dictionary whereas updating modifies the value of a key that is already present

# dictionaries rely on unique keys to function as a lookup map
# if duplicate keys were allowed the computer wouldnt know which specific value to retrieve when we call that key
