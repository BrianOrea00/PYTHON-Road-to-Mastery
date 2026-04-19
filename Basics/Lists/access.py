# Access List
# List items are indexed and you can access by referring to the index number
thislist1 = ["Kikyam", "Chicken ball", "Fish ball"]
print(thislist1[1])
# Note: The First item has index 0.

# Negative indexing
# negative indexing means start from the end
# -1 refers to the last item and -2  refers to the second last item etc
print(thislist1[-1])

# Range of indexes
# you can specify a range of indexes bby specifying where to start and where to end the ranges
# when specifying a range the return value will be a new list with the specified items
thislist2 = ["Black tea", "Green tea", "Oolong tea", "Barley tea", "Pu-erh tea"]
print(thislist2[2:4])
# Note: The search will start at index 2 (included) and end at index 4 (not included).
# by leaving out the start value the range will start at the first item
print(thislist2[:4])
# by leaving out the end value the range will go on to the end of the list
print(thislist2[2:])


# Range of Negative indexes
# specify negative indexes if we want to start the search from the end of the list
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[-4:-1])
# this example returns the items from "orange"(-4) to but not including "mango"(-1)

# Check if the item Exists
# to determine if a specified item is present in a list use the "in" keyword
if "Kikyam" in thislist1:
    print("Yes! There is Kikyam in the List")
