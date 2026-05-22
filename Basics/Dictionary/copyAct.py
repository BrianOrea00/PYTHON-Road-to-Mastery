# AI generated problem

student = {
    "name": "Brian",
    "age": 23
}
# 1. Create copy using copy()
# 2. Create another copy using dict()
# 3. Modify copied dictionary
# and show original unchanged
# 4. Do:
a = {"x": 1}
b = a
# modify b and print both
# 5. Explain (comment):
# difference between b = a
# and b = a.copy()
# 6. Create copy and remove one key
# from copied dictionary only
# 7. Show original dictionary unchanged
# 8. Explain (comment):
# why copying dictionaries is important
# 9. Predict:
# how many dictionaries exist here?
a = {"x": 1}
b = a
# 10. Explain (comment):
# why direct assignment can be dangerous

studentCopy = student.copy()
print(studentCopy)

anotherCopy = dict(student)
print(anotherCopy)

studentCopy["course"] = "BSCS"
print("Original:", student)
print("Modified Copy:", studentCopy)

b["x"] = 100
print(a)
print(b)

# b = a creates a reference to the same dictionary while b = a.copy() creates a brand new independent duplicate in memory

studentCopy.pop("course")
print("Copy", studentCopy)
print("Original", student)

# Copying dictionaries is important because it allows you to manipulate and mutate data without accidentally altering or ruining the original source data

# There is exactly 1 dictionary object here as both variables a and b are pointing to the same address in memory

# Direct assignment is dangerous because modifying the new variable inadvertently changes the original data often leading to unintended side effects and bugs
