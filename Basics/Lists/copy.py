# Copy List
# we cannot copy a list by simply by typing list2 = list1 because list2 will only be a reference to list1 and changes made in list1 will automatically also be made in list2

# Use the copy() method
# we can use the built in list method copy() to copy a list
thislist1 = ["Coffee", "Sugar", "Creamer"]
mylist1 = thislist1.copy()
print(mylist1)

# Use the list() method
# another way to make a copy is to use the built in method list()
thislist2 = ["Bear Brand", "Alaska", "Birch tree"]
mylist2 = list(thislist2)
print(mylist2)

# Use the slice operator
# we can also make a copy of a list by using the : (slice) operator
thislist3 = ["Claude", "Deepseek", "Grok"]
mylist3 = thislist3[:]
print(mylist3)
