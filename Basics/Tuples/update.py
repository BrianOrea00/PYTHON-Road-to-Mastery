# Update Tuples
# tuples are unchangeable meaning that we cannot change, add, or remove items once the tuple is created
# but there are some wworkaround
# we can convert the tuple into a list, change the list, and convert the list back into a tuple
thistuple1 = ("a", "b", "d")
thislist1 = list(thistuple1)
thislist1[2] = "c"
thistuple1 = tuple(thislist1)
print(type(thistuple1))
print(thistuple1)

# Add Items
# since tuples are immutable they do not have built in append() method but there are other ways to add to a tuple
# 1. Convert into a list just like the wworkaround for channging a tuple we can convert it into a list, add our item/s and convert it back into a tuple
thislist2 = list(thistuple1)
thislist2.append("d")
thistuple1 = tuple(thislist2)
print(thistuple1)

# 2. Add tuple to a tuple we aree allowed to add tuples to tuples so if we want to add one item/s create a new tuple with the item/s
thistuple2 = ("e",)
thistuple1 += thistuple2
print(thistuple1)

# Remove Items
# just like earlier convert ihe tuple into list then remove() and convert it back into tuple
thislist3 = list(thistuple1)
thislist3.remove("a")
thistuple1 = tuple(thislist3)
print(thistuple1)
# or we can delete the tuple completely
# the del keyword can delete it completely
del thistuple1
# print(thistuple1) this will raise an error because the tuple no longer exist
