# AI generated problem

# 1. Create a frozenset with 3 fruits
# 2. Print the frozenset
# 3. Check if "apple" exists
# 4. Loop through frozenset
# 5. Fix this error:
# fs.add("orange")
# 6. Create 2 frozensets
# and use union()
# 7. Explain (comment):
# difference between set and frozenset
# 8. Explain (comment):
# why frozenset is immutable
# 9. Explain (comment):
# why frozenset can be used inside another set
# 10. Predict:
# what happens if you try:
# fs.remove("apple")

fruits = frozenset({"apple", "banana", "cherry"})

print(fruits)

print("apple" in fruits)

for x in fruits:
    print(x)

fs = set(fruits)
fs.add("orange")
print(fs)
fruits = frozenset(fs)
print(fruits)

fs1 = frozenset({1, 2, 3})
fs2 = frozenset({4, 5, 6})
print(fs1 | fs2)

# set is a mutable collection that allows us to add or remove elements after creation
# while a frozenset is an immutable version whose elements cannot be changed once defined

# frozenset is designed to be immutable so that its data remains static and safe from accidental modification, ensuring its contents are fixed for the entirety of its lifecycle

# frozenset is immutable it is hashable which satisfies the python requirements that all elements inside a standard set must have a permanent unchanging hash value

# it will raise an AttributError because the frozenset object does not possess a remove() method
