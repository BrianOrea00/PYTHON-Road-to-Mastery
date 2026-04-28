# Sort List
# Sort List Alpanumerically
# list object have a sort() method that will sort the list alpanumerically - ascending by default
# example
thislist1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist1.sort()
print(thislist1)

# sort list numerically
thislist2 = [100, 50, 65, 82, 23]
thislist2.sort()
print(thislist2)

# Sort Descending
# to sort descending use the argument "reverse = True"
# example
thislist1.sort(reverse = True)
print(thislist1)

# sort descending numerically
thislist2.sort(reverse = True)
print(thislist2)

# Customize Sort Function
# we can also customize our own function by using the keyword argument "key = function"
# the function will return a number that will be used to sort the list (the lowest number first)
# example
# sort the list based on how close the number is to 50
def myfuc(n):
    return abs(n - 50)

thislist2.sort(key =  myfuc)
print(thislist2)

# Case Insensitive Sort
# the default the sort() method is case sensitive resulting in all capital letters being sorted before lower case letters
thislist3 = ["hotsilog", "masilog", "Bangsilog", "Tapsilog"]
thislist3.sort()
print(thislist3)

# luckily we can use built in functions as key functions when sorting a list
# so is we want a case insensitive sort function use "str.lower" as a key function
thislist3.sort(key = str.lower)
print(thislist3)

# Reserve Order
# what if we want to reverse the order of a list regardless of the alphabet
# the reverse() method reverses the current sorting order of the elements
thislist4 = ["a", "b", "c", "d"]
thislist4.reverse()
print(thislist4)
