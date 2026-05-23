# Nested Dictionaries
# Nested Dictionaries
# a dictionary can contain dictionaries this is called nested dictionaries
myfam = {
    "child1" : {
        "name" : "childone",
        "age" : 10
    },
    "child2" : {
        "name" : "childtwo",
        "age" : 9
    },
    "child3" : {
        "name" : "childthree",
        "age" : 77
    }
}
print(myfam)
# or if we want to add three dictionaries into a new dictionaries
child1 = {
    "name" : "wan",
    "age" : 1
}
child2 = {
    "name" : "tu",
    "age" : 2
}
child3 = {
    "name" : "tri",
    "age" : 3
}
thechildrens = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(thechildrens)

# Access Items in Nested Dictionaries
# to access items from a nested dictionary we use the name of the dictionaries starting with the outer dictionary
print(myfam["child1"]["name"])

# Loop Through Nested Dictionaries
# we can loop through a dictionary by using the items() method
for x, obj in myfam.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
