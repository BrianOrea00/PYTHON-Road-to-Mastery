# Add Set Items
# Add Items
# Note: Once a set is created we cannot change its items but we can add new items
# To add one item to a set use the add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("dates")
print(thisset)

# Add Sets
# to add items from another set into the current set use the update() method
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add any Iterable
# the object in the update() method does not have to be a set it can be any iterable object like tuples, list, dictionaries etc
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
