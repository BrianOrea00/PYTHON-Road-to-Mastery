# AI generated problem
# 1. Remove Spaces: Remove the spaces at the beginning and end.
# 2. Change Case: From the cleaned string: Print it in upper/lowercase.
# 3. Replace Characters: Replace "World" with "Python".
# 4. Split String: Split the string using ",".
# 5. Debug this.
#   text = " Hello "
#   text.strip()
#   print(text)
# From the cleaned string Answer the 2 to 4.
text = "  Hello, World!  "# use this
text.strip()

print(text.strip())

print(text.strip().upper())
print(text.strip().lower())

print(text.strip().replace("World!", "Python!"))

print(text.strip().split(","))

text2 = " Hello  "
text2.strip()
print(text2.strip())
