# Ai generated problem

s1 = {"a", "b", "c"}
s2 = {"c", "d", "e"}

# 1. Join sets using union()
# 2. Join sets using update()
# 3. Join sets using |
# 4. Find common values
# 5. Find values only in s1
# 6. Find values not shared
# 7. Explain (comment):
# difference between union() and update()
# 8. Explain (comment):
# what intersection means in sets
# 9. Predict:
# what happens to duplicates during join
# 10. Explain (comment):
# why sets are useful for comparisons

set3 = s1.union(s2)
print(set3)

s1.update(s2)
print(s1)

set3 = s1 | s2
print(set3)

set3 = s1.intersection(s2)
print(set3)

set3 = s1.difference(s2)
print(set3)

set3 = s1.symmetric_difference(s2)
print(set3)

# the union() creates new set with all elements while update() modifies the original set in place

# intersection identifies only the elements that are present in both sets simultaneously

# duplicates are automatically removed because sets only store unique values

# sets are useful for comparisons because they provide highly efficient mathematical operations for finding unique or shared items
