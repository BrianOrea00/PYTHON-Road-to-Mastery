# Access Set items
# Access items
# we cannot access items in a set by referring to an index or a key
# but we can loop through the set items using a "for" loop or ask if a specified value us present in a set using the "in" keyword
thisset = {"a", "b", "c"}
for x in thisset:
    print(x)

print("b" in thisset)

print("b" not in thisset)

# Change items
# Once a set is created we cannot change its items but we can add new items
