# Remove Set items
# Remove Item
# To remove an item in a set use the remove() or the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# Note: if the item to remove does not exist remove() will raise an error
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# Note: if the item to remove does not exist discard() will not raise an error
# we can also use the pop() method to remove an item but this method will remove a random item
# so we cannot be sure what item that gets removed
# the return value of the pop() method is the removed items
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# Note: sets are unordered so when using the pop() method we do not know which item that gets removed

# the clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# the del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset

