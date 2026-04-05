# Escape Character
# to insert character that are illegal in a string we can use an escape character.
# an escape character is a backslash "\" followed by the character you want to insert.
# an example of an illegal character is a double quote inside a string that is surrounded by double quote.
# txt = "We are the so-called "Vikings" from the north." this is wrong.
# do this instead
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# so we have here a list of other escape character for python.
# we have \' single quote.
print("It\'s Summer")

# we have \\ backslash.
print("This will insert one \\ (backslash).")

# we have \n new line.
print("1st line \n2nd line")

# we have \r carriage return.
print("Hello\rWorld!")

# we have \t tab.
print("This is \ttab")

# we have \b backspace.
print("the \bbackspaces \bare \bgone")

# we have \ooo octal value.
# A backslash followed by three integers will result in a octal value:
print("\110\145\154\154\157")

# we have \xhh hex value.
# A backslash followed by an 'x' and a hex number represents a hex value.
print("\x48\x65\x6c\x6c\x6f")
