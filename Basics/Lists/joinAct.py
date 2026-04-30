# List Join Activity

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# 1. Join using +
# 2. Join using extend()
# 3. Join using loop + append()
# 4. Print all results
# 5. Explain (comment):
# difference between + and extend()
# 6. Explain (comment):
# which method creates a new list
# 7. Explain (comment):
# which method changes the original list
# 8. Predict:
# what happens if you use append(list2)
# 9. Fix this mistake:
# list1.append(list2)
# (make it properly join instead)
# 10. Explain (comment):
# why extend() is usually preferred

list3 = list1 + list2

list1copy = list1.copy()
list1copy.extend(list2)

list1loop = list1.copy()
for x in list2:
    list1loop.append(x)

print(list3)
print(list1copy)
print(list1loop)

# the "+" creates a new list by combining the elements of the operands it does not modify the original list
# the "extend()" adds elements from a iterable like another list to the end of the current list

# the "+" creates new list

# the "extend()" changes the original list

# append(list2) adds the entire list as a single element (nested list)

list1add = list1.copy()
list1fix = list1add + list2
print(list1fix)

# extend() is often preferred because it modifies the list in place without creating a new list
