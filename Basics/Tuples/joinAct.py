# Ai generated problem
#
# 1. Join two tuples
t1 = ("a", "b")
t2 = ("c", "d")
# create a new tuple with all values
t3 = t1 + t2
print(t3)

# 2. Join three tuples into one
t1 = (1,)
t2 = (2,)
t3 = (3,)
# result should be (1, 2, 3)
t4 = t1 + t2 + t3
print(t4)

# 3. Predict the output (no code change)
t1 = ("x", "y")
t2 = ("z",)
result = t1 + t2
print(result)
# My prediction is ('x', 'y', 'z')

# 4. Fix this error:
t1 = ("a", "b")
t2 = ("c", "d")
# t1.append(t2) this should be like this
t3 = t1 + t2
print(t3)

# 5. Create a tuple that repeats ("hi",) 3 times
t1 = ("hi",)
print(t1 * 3)

# 6. Join tuple with one element correctly
t1 = ("apple", "banana")
# add "orange" using tuple join
# we add new tuple named t2
t2 = ("orange",)
print(t1 + t2)

# 7. Predict:
t = (1, 2)
print(t * 2)
# My prediction is (1, 2, 1, 2)

# 8. Explain (comment):
# difference between + and * in tuples
# the + operator is used for concatenation which merges two or more tuples together
# the * operator is used for multiplication(repetition) which repeats its contents of a single tuple a specific number of times

# 9. Explain (comment):
# why join creates a new tuple
# because tuples are immutable meaning the contents cannot be changed or expanded in place after they are created
# so if we cannot modify the original memory block then we must allocate a new space in memory to store the combined elements

# 10. Fix this:
t1 = ("a", "b")
t2 = ("c", "d")
# store result in t1 (properly)
t1 = t1 + t2
print(t1)
