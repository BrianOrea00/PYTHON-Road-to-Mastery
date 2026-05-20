# AI generated problem

student = {
    "name": "Brian",
    "age": 23,
    "course": "BSCS"
}

# 1. Remove "age" using pop()
# 2. Store removed value from pop()
# and print it
# 3. Remove last item using popitem()
# 4. Add new key:
# "year" = 2026
# 5. Remove "year" using del
# 6. Clear the dictionary
# 7. Print dictionary after clear()
# 8. Explain (comment):
# difference between pop() and del
# 9. Explain (comment):
# difference between clear() and del
# 10. Predict:
# what happens if pop() uses missing key

student.pop("age")
print(student)

remVal = student.pop("course")
print(remVal)

student.popitem()
print(student)

student["year"] = 2026
print(student)

del student["year"]
print(student)

student.clear()

print(student)

# pop() removes a key and returns its value so we can use it
# while del simply deletes the key-value pair without returning anything

# clear() empties the contents of the dictionary leaving it valid but empty
# whereas del deletes the entire dictionary variable from the memory

# it will raise a KeyError unless a default fallback value is provided as a second argument
