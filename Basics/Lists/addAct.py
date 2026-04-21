# List Add Activity

fruits = ["apple", "banana", "cherry"]

# 1. Add "orange" at the end using append()
# 2. Add "mango" at index 1
# 3. Add ["grape", "melon"] using extend()
# 4. Add a list ["kiwi", "lemon"] using append()
# (observe what happens)
# 5. Insert "pineapple" at the beginning
# 6. Insert "pear" at the end using insert()
# 7. Create a second list:
more = ["x", "y"]
# Add it to fruits using extend()
# 8. Explain (comment):
# difference between append() and extend()
# 9. Explain (comment):
# what happens when you append a list
# 10. Explain (comment):
# why extend() is used for multiple items

fruits.append("orange")
print(fruits)

fruits.insert(1, "mango")
print(fruits)

fruits2 = ["grape", "melon"]
fruits.extend(fruits2)
print(fruits)

fruits.append(["kiwi", "lemon"])
print(fruits)

fruits.insert(0, "pineapple")
print(fruits)

fruits.insert(len(fruits), "pear")
print(fruits)

fruits.extend(more)
print(fruits)

# I think the difference are in append adds one item to the list while in extend add each elements from another iterable into the list

# Just like in #4 I observe that when we append it adds the entire list inside the list

# extend is used to add multiple elements individually into the list
