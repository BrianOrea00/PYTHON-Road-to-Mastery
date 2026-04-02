# Modify string
# python has a built in methods that we can use on string.

# Upper Case
# the upper() method return string in upper case,
# example1
a = "this is upper"
print(a.upper())

# Lower Case
# the lower() method return string in  lower case.
# example2
b = "THIS IS LOWER"
print(b.lower())

# Remove Whitespace
# Whitespace is a space before and/or after the actual text and very often we want to remove this space.
# the strip() method removes any whitespace from the beginning and/or the end.
# example3
c = " This is Whitespace "
print(c.strip())

# Replace string
# the replace() method replaces a string with another string.
# example4
d = "Replace the J"
print(d.replace("J", "K"))

# Split string
# the split() method  split string inti substrings if it finds instances of the separator.
# examle5
e = "Hello, World!"
print(e.split(","))
