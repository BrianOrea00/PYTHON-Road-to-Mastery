# AI generated problem

age = 20
has_id = True

# 1. Use nested if:
# if age >= 18
# then check has_id
# 2. Print:
# "Adult with ID"
# 3. Add else:
# print "No ID"
# 4. Add outer else:
# print "Minor"
# 5. Create:
# score = 95
# use nested if:
# if score >= 75
# then check if score >= 90
# 6. Explain (comment):
# what nested if means
# 7. Explain (comment):
# why indentation matters in nested if
# 8. Explain (comment):
# when nested if is useful
# 9. Predict:
x = 15
# if x > 10:
#     print("A")
#     if x > 20:
#         print("B")
# what prints?
# 10. Predict:
x = 30
# if x > 10:
#     print("A")
#     if x > 20:
#         print("B")
# what prints?

if age >= 18:
    if has_id:
        print("Adult with ID")
    else:
        print("No ID")
else:
    print("Minor")

score = 95
if score >= 75:
    print("Passed")
    if score >= 90:
        print("Passed with Honors")

# a nested if statement is an if statement that is placed inside the body of another if statement

# indentation is crucial because it defines the structure and scope
# telling the program which inner condition belong to which outer condition

# it is useful when we need to check a secondary condition only after the primary condition has already been met

# it will print "A"

# it will print both "A" and "B" because both are True
