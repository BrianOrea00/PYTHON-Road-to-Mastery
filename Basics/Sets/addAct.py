# AI generated problem

s = {"apple", "banana"}

# 1. Add "orange"
# 2. Add multiple items:
# "grape", "mango"
# 3. Try adding duplicate "apple"
# and observe output
# 4. Create empty set
# then add "hello"
# 5. Use update() with tuple:
# ("x", "y")
# 6. Fix this:
# s.add(["a", "b"])
# 7. Explain (comment):
# difference between add() and update()
# 8. Explain (comment):
# why duplicate values are ignored

s.add("orange")
print(s)

s.update(["grape", "mango"])
print(s)

s.add("apple")
print(s)
# the output is 1 apple only

s = set()
s.add("hello")
print(s)

updTuple = ("x", "y")
s.update(updTuple)
print(s)

s.update(["a", "b"])
print(s)

# add() this method adds only one item in the set
# update() this method can add multiple items and add any iterable object in the set

# sets use hashing to assign each item a unique position in memory so attempting to add a duplicate simply points to an existing entry rather than creating a new one
