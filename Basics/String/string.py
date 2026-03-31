# String
# string in python is surrounded by single quotation or double quotation marks.
# 'hello' is same as "hello".
# we can display a string literal with the print() function.
# example1
print("hello")
print('hello')

# quotes inside quotes
# we can use quotes inside a string as long as they dont have a match that surruonds a string.
# example2
print("it's a quote inside a quotes")
print('this is "quotes"')
print("this is also a 'quotes'")

# assign string to a variable
# to do this we need a variable name then equal sign then the string.
# example3
a = "string"
print(a)

# multiline string
# we can assign a multiline string to a variable by using three quotes.
# example4
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)
# we can also use three single quotes.
c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c)

# strings are array
# like in other popular PL string in python are arrays of unicode characters.
# however in python there is no character data type.
# a single character is simply a string with a length of 1.
# square brackets can be used to access elements of the string
# example5
d = "Hello"
print(d[1])

# loop through a string
# since string are arrays we can loop through the characters in a string with a for loop.
# example6
for x in "Brian":
    print(x)

# string length
# the len() function returns the length of a string.
# example7
e = "Hello, Everyone!"
print(len(e))

# check string
# to check if certain phrase or characters are present in the string.
# we can use the keyword "in".
# example8
f = "I love free food!"
print("free" in f)
# or we can use if statement.
# example9 we will use the f variable
if "food" in f:
    print('"Food" Found!')

# check if not
# to check is certain phrase or characters are not in the string.
# we can use the keyword "not in".
# example10
g = "I hate bitter melon"
print("love" not in g)
# we can also use if statement
# example11 we will use the g variable.
if "love" not in g:
    print('"Love" not Found!')

