# Join List
# Join Two Lists
# these are several ways to join or concatenate two or more list in python
# one of the easiest ways are by using the "+" operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# another way to join is by appending all the items from list2 into list1 one by one
for x in list2:
    list1.append(x)

print(list1)

# Or we can use the extend() method where the purpose is to add elements from one list to another list
list4 = ["q", "w", "e", "r"]
list5 = [9, 8, 7, 6]
list4.extend(list5)
print(list4)
