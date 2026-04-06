# String Method
# Python has a set of built in methods that you can use on strings.
# All string methods return new values they do not change the original string.
# we have capitalize() - converts the first character to upper case.
text = "hello World"
print(text.capitalize())

# we have casefold() -  converts string to lower case.
print(text.casefold())

#we have center() - returns a centered string.
text2 = "hi"
print(text2.center(10, "-"))

# we have count() - returns the number of times a specified value occur in a string.
print(text.count("o"))

# we have encode() - returns an encode version of the strings.
print(text.encode())

# we have endswith() - returns true if the string ends with the specified value.
print(text.endswith("World"))

# we have expandtabs() - set the tab size of the string.
text3 = "Brian\tOrea"
print(text3.expandtabs(5))

# we have find() - searches the string for a specified value and returns the position of where it was found.
print(text.find("World"))

# we have format() - formats specified value in string.
Fname = "Brian"
Lname = "Orea"
print("My name is {} {}.".format(Fname, Lname))

# we have isalnum() - returns true if all characters in the string are alphanumeric.
text4 = "Brian999"
print(text4.isalnum())

# we have isalpha() - returns true if all characters in the string are in the alphabet.
print(text4.isalpha())

# we have isascii() -  returns true if all characters in the strings are ascii characters.
print(text4.isascii())

# we have isdecimal() - returns true if all characters in the string are decimal.
print(text4.isdecimal())

# we have isdigit() - returns true if all characters in the string are digits.
text5 = "8996"
print(text5.isdigit())

# we have isidentifier() - returns true if the string is an identifier.
text6 = "HelloWorld"
print(text6.isidentifier())

# we have islower() - returns true if all characters in the string are lower case.
text7 = "all lower"
print(text.islower())
print(text7.islower())

# we have isprintable() - returns True if all characters in the string are printable.
print(text7.isprintable())

# we have isspace() - returns True if all characters in the string are whitespaces.
print(text.isspace())
