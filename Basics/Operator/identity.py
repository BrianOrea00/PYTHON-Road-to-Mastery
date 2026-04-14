# Identity
# identity operators are used to compare the object not if they are equal but if they are actually the same object with the same memory location.
# we have "is" returns true if both variables are the same object
x = ["adobo", "sinigang"]
y = ["adobo", "sinigang"]
z = x

print(x is z)
# returns true because z is the same as object as x

print(x is y)
# returns false because x is not the same object as y evem if they have the same content

print(x == y)
# to demonstrate the difference between "is" and "==":  this comparison returns true becausex is equal to y

# we have "is not" returns true if both variables are not the same object
print(x is not z)
# returns false because z is the same object as x

print(x is not y)
# returns true because x is not the same object as y even if they have the same content

print(x != y)
# to demonstrate the difference between "is not" and "!=": this comparison returns false because x is equal to y
