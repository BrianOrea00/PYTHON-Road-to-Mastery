# List
# Lists are used to store multiple items in a single variable
# Lists are one of 4 built in data types in python used to store collections of data the other 3 are Tuple, Set, and Dictionary all with different qualities and usage
# Lists are created using square brackets
thisislist1= ["Akali", "Thresh", "Leona"]
print(thisislist1)

# List Items
# list items are ordered, changeable, and allow duplicate values
# list items are indexed the first item has [0] the second item has index [1] and so on

# Ordered
# when we say the list is ordered it means that the items have a defined order amd that order will not change
# if we add new items to a list the new item will be placed at the end of the list

# Note: There are some list methods that will change the order, but in general: the order of the items will not change

# Changeable
#  the list is changeable meaning we can change, add, and remove items in a list after it has been created

# Allow duplicates
# since list are indexed lists can have items with the same value
thisislist2 = ["Naafiri", "Dr. Mundo", "Samira", "Naafiri"]
print(thisislist2)

# List lenght
# to determine how many items in a list use the len() function
print(len(thisislist1))

# List Items - Data Types
# list item can be of any data types
list1 = ["A", "B", "C"]
list2 = [1, 2, 3]
list3 = [True, False, True]
print(list1)
print(list2)
print(list3)
# a list can contain different data types
list4 = ["abc", 34, True, 40, "male"]
print(list4)

# type()
# from pythons perspective list are defined as objects with the data type 'list'
print(type(thisislist2))

# list() Constructor
# it is also possible to use the list() constructor when creating a new list
thisislist3 = list(("C", "C++", "C#"))
print(thisislist3)
