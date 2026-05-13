# Join Sets
# there are several ways to join two or more sets in python
# the union() and update() methods join all items from both sets
# the intersection() mthods keeps only the duplicates
# the difference() method keeps the items from the first set that are not in the other set/s
# the symmetrical_difference() method keeps all items except the duplicates

# Union
# the union() method returns a new set with all items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# we can use the | operator instead of the union() method and we will get the same result
set4 = set1 | set2
print(set4)

# Join multiple sets
# all the joining methods and operators can be used to join multiple sets
# when using a method just add more sets in the parentheses separated by commas
set5 = {"Brian", "Orea"}
set6 = {"apple", "banana", "cherry"}
myset = set1.union(set2, set5, set6)
print(myset)
# when using the | operator separate the sets with more | operators
myset = set1 | set2 | set5 | set6
print(myset)

# join a set and a tuple
# the union() method allows us to join a set with other data types like lists or tuples
# the result will be a set
x = {"a", "b", "c"}
y =(1, 2, 3)
z = x.union(y)
print(z)
# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method

# Update
# the update() method inserts all items from one set into another
# the update() changes the original set and does not return a new set
set1 = {"A" ,"B" ,"C"}
set2 = {4, 5, 6}
set1.update(set2)
print(set1)
# Note: Both union() and update() will exclude any duplicate items

# intersection
# keeps only the duplicates
# the intersection() method will return a new set that only contains the items that are present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
# You can use the & operator instead of the intersection() method, and you will get the same result
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)
# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method
# the intersection_update() method will also keep only the duplicates but it will change the original set instead of returning a new set
set1.intersection_update(set2)
print(set1)
# the value True and 1 are considered the same value the same goes to False and 0
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# Difference
# the difference() method will return a new set that will contain only the items from the first set that are not present in the other set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
# we can use the - operator instead of the difference() method and we will get the same result
set3 = set1 - set2
print(set3)
# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method
# the difference_update() method will keep the items from the first set that are not in the other set but it will change the original set instead of returning a new set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
