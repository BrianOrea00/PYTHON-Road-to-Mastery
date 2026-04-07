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

# we have istitle() -  returns True is the string follows  the rules of a title.
print(text.istitle())

# we have isupper() - returns True is all characters in the string are upper case.
print(text.isupper())

# we have join() - Joins the elements of an iterable to the end of the string.
print("-".join(["a", "b", "c"]))

# we have ljust() - returns a left justtified version of the string.
print(text2.ljust(10,"-"))

# we have lower() - converts a string into lower case.
print(text.lower())

# we have lstrip() - returns a left version of the string.
text8 = "   hi   "
print(text8.lstrip())

# we have maketrans() - Returns a translation table to be used in translations.
text9 = str.maketrans("a", "b")
print("apple".translate(text9))

# we have partition() - returns a tuple where the string is parted into three parts.
text10 = "Dog-Cat-Rat"
print(text10.partition("-"))

# we have replace() -  returns a string where a specified value is replaced with a specified value.
text11 = "Red Spider Lily is my favorite flower!"
print(text11.replace("Red Spider Lily", "Sun Flower"))

# we have rfind() - searches the string for a specified value and returns the last position of where it was found.
print(text.rfind("World"))

# we have rjust() - returns a right justtified version of the string.
print(text2.rjust(10,"-"))

# we have rpartition() - returns a tuple where the string is parted into three parts.
print(text10.rpartition("-"))

# we have rsplit() - splits  the string at the specified separator and returns a list.
text12 = "a,b,c"
print(text12.rsplit(","))

# we have rstrip() - returns a right version of the string.
print(text8.rstrip())

# we have split() - splits the string at the specified separator and returns a list.
print(text12.split())

# we have splitlines() splits the string at line breaks and returns a list.
text13 = "a\nb\nc"
print(text13.splitlines())

# we have startswith() - returns true is the string starts with the specified value.
text14 = "This is Startswith"
print(text14.startswith("This"))

# we have strip() - returns a trimmed version of the string.
print(text8.strip())

# we have swapcase() - swaps cases lower case becomes upper and vise versa.
print(text.swapcase())

# we have title() -  converts the first character of each word to upper.
print("this is sample title".title())

# we have translate() - returns a translated string.
print("orange".translate(text9))

# we have upper() - converts a string into upper case.
print(text.upper())

# we have zfill() - fills the string with a specified number of 0 values at the beginning.
text15 = "99"
print(text15.zfill(6))
