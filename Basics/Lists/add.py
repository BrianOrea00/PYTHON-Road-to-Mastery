# Add List
# Append items
# to add an item to the end of the list use the append() method
thislist = ["Facebook", "Messenger", "Instagram"]
thislist.append("Threads")
print(thislist)

# Insert items
# to insert a list item to a specified index use insert() method
thislist.insert(0, "WhatsApp")
print(thislist)

# Extend List
# to append elements from another list to the current list use the extend() method
thislist2 = ["Meta Horizon", "Meta View"]
thislist.extend(thislist2)
print(thislist)
# the new elements will be added at the end of the list

# Add any iterable
# the extend() method does not have to append list we can add any iterable object(tuple, sets, dictionaries, etc)
thistuple =("Meta Quest", "Meta AI")
thislist.extend(thistuple)
print(thislist)
