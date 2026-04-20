# Change List
# to change the value of a specific item refer to the index number
thislist1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
thislist1[1] = "b"
print(thislist1)

# Change a Range of Item Values
# to change the value of items within a specified range define a list with the new values and refer to the range of the index numbers where we want to insert the new values
thislist1[2:5] = ["c", "d", "e"]
print(thislist1)
# if we insert more items than we replace the new items will be inserted where we specified and the remaining items will move accordingly
thislist1[6:7] = ["g", "h"]
print(thislist1)
# Note: The length of the list will change when the number of items inserted does not match the number of items replaced
# if we insert less item than we replace the new items will be inserted where we specified and the remaining items will move accordingly
thislist1[6:8] = ["G"]
print(thislist1)

# Insert items
# to insert a new list item without replacing any of the values we cna use the insert() method
# the insert() method inserts an item at the specified index
thislist1.insert(7, "New")
print(thislist1)
