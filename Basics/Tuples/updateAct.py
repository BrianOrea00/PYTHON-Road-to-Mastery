# AI generated problem

t = ("apple", "banana", "cherry")

# 1. Change "banana" to "mango"
# (use correct method)
# 2. Add "orange" to the tuple
# 3. Remove "apple" from the tuple
# 4. Create a new tuple with an extra item "grape"
# without modifying the original tuple
# 5. Show that original tuple is unchanged (print both)
# 6. Delete the entire tuple
# 7. Fix this error:
# t[0] = "kiwi"
# 8. Fix this:
# t.append("melon")
# 9. Explain (comment):
# why tuples cannot be changed
# 10. Explain (comment):
# what actually happens when we "update" a tuple

l = list(t)
l[1] = "mango"
t = tuple(l)
print(t)

l = list(t)
l.append("orange")
t = tuple(l)
print(t)

l = list(t)
l.remove("apple")
t = tuple(l)
print(t)

# need original tuple
original = ("apple", "banana", "cherry")
c = list(original)
c.append("grape")
cm = tuple(c)
print("Original", original)
print("Modified", cm)

del t
# i will re create the tuple
t = ("apple", "banana", "cherry")

l = list(t)
l[0] = "kiwi"
t = tuple(l)
print(t)

l = list(t)
l.append("melon")
t = tuple(l)
print(t)

# tuples are immutable by design meaning their memory structure is fixed upon creation to ensure data integrity and allow for faster processing and hashability

# when we "update" a tuple we are actually converting it to a list modifying the list and then creating an entirely new tuple object to replace the old one
