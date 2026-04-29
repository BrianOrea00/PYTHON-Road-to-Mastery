# List Copy Activity

fruits = ["apple", "banana", "cherry"]

# 1. Create a copy using copy()
# 2. Create another copy using list()
# 3. Create another copy using slicing
# 4. Modify the copied list (add one item)
# and print both original and copy
# 5. Do this:
a = ["x", "y"]
b = a
# Modify b and print both a and b
# (observe what happens)
# 6. Explain (comment):
# difference between b = a and b = a.copy()
# 7. Create a copy and remove one item from the copy only
# 8. Show that original list is unchanged
# 9. Explain (comment):
# why copying is important
# 10. Predict:
# if you do b = a, how many lists exist?

copy1 = fruits.copy()
print(copy1)

copy2 = list(fruits)
print(copy2)

copy3 = fruits[:]
print(copy3)

copy4 = fruits.copy()
copy4.append("mango")
print("original", fruits)
print("modified copy", copy4)

b.append("z")
print(a, b)

# b = a this both refer to the same list (same object)
# b = a.copy() this creates a new independent list

copy7 = fruits.copy()
copy7.remove("cherry")
print("Modified Copy", copy7)

print("Original", fruits)

# copying is important to avoid modifying the original list when changes are made to another variable
#
# in my prediction we will have 1 list because its same we just rename it
