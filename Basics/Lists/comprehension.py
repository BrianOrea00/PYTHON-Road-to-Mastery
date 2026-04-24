# List Comprehension
# list comprehension offers a shorter syntax when we want to create a new list based on the value of an existing list
# example
# based on a list of fruits we want a new list containing only the fruits with "a" in the name
# without list comprehension we will have to write "for" statement with a condition test inside
fruits1= ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = []

for x in fruits1:
    if "a" in x:
        newlist1.append(x)
print(newlist1)

# with list comprehension we can do all that with only one line of code
fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [a for a in fruits2 if "a" in a]
print(newlist2)

# the syntax
# newlist = [expression for item in iterable if condition == True]
# the return value is a newlist leaving the old list unchanged

# Condition
# the conddition is like a filter that only accept the items that evaluates True
# example
# only accept items that are not "apple"
fruits3 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist3 = [b for b in fruits3 if b != "apple"]
print(newlist3)
# the condition if x != "apple" will return True for all elements other than "apple"
# the condition is optional and can be omitted
# example
# with no if statement
fruits4 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist4 = [c for c in fruits4]
print(newlist4)

# iterable
#the iterable can be any iterable object, like a list,tuple,set etc
# we can use range() function to create an iterable
newlist5 = [d for d in range(10)]
print(newlist5)
# same example but with condition
# only accept numbers lower than 5
newlist6 = [e for e in range(10) if e < 5]
print(newlist6)

# expression
# the expression is the current item in the iteration but it is also the outcome which can manipulate before it ends up like a list item in the newlist
newlist7 = [f.upper() for f in fruits4]
print(newlist7)
# we can set the outcome to whatever we like
fruits5 = ["qwer", "asdf", "zxcv"]
newlist8 = ['wazzup' for g in fruits5]
print(newlist8)
# the expression can also contain conditions not like a filter but as a way to manipulate the outcome
# example
# return "orange" instead of "banana"
newlist9 = [h if h != "banana" else "orange" for h in fruits4]
print(newlist9)
# this expression return the item if it is not "banana" if it is "banana" return "orange"
