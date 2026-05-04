# Unpack Tuple
# unpacking a tuple
# when we create a tuple we normally assign values to it this is called "packing" a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)
# but in python we are also allowed to extract the values back into variables
# this is called "unpacking"
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# Note: the number of variables must match the number of values in the tuple if not we must use an asterisk to collect the remaining values as a list
# Using Asterisk
# if the number of variables is less than the number of values we can add an "*" to the variable name and the values will be assigned to the variable as a list
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits2
print(green)
print(yellow)
print(red)
# if the asterisk is added to another variable name than the last python will assign values to the variable until the number of the values left matches the number of the variables left
fruits3 = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits3
print(green)
print(tropic)
print(red)
