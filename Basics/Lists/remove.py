# Remove List
# Remove specified item
# the remove() method removes the specified item
thislist1= ["League of Legends", "VALORANT", "Teamfight Tactics"]
thislist1.remove("Teamfight Tactics")
print(thislist1)

# if there are more than one item with specified value the remove() method removes the first occurence
thislist2 = ["League of Legends", "VALORANT", "Teamfight Tactics", "Teamfight Tactics", "Legends of Runeterra", "League of Legends: Wild Rift"]
thislist2.remove("Teamfight Tactics")
print(thislist2)

# Remove specified index
# the pop() method removes the specified index
thislist2.pop(2)
print(thislist2)
# if we do not specify the index the pop() method removes the last item
thislist2.pop()
print(thislist2)

# the del keyword also removes the specified index
del thislist2[2]
print(thislist2)

# del keyword can also delete the list completely
del thislist2

# Clear the list
# the clear() method empties the list
# the list remains but it has no content
thislist1.clear()
print(thislist1)
