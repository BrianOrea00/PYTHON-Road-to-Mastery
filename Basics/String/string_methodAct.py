# AI ggenerated problem
# use this
text = "hello world"
text2 = "  python programming  "
text3 = "a,b,c,d"
text4 = "HelloWorld123"
# 1. Convert the first letter of text to uppercase using a method
# 2. Convert the entire text to uppercase
# 3. Count how many times the letter "o" appears in text
# 4. Remove spaces at the beginning and end of text2
# 5. Replace "world" with "Python" in text
# 6. Split text3 into a list using ","
# 7. Check if text4 is alphanumeric
# 8. Check if text4 contains only letters
# 9. Find the position of "world" in text
# 10. Join this list into a string using "-" as separator
# ["x", "y", "z"]
# 11. Check if text starts with "hello"
# 12. Check if text ends with "world"
# 13. Convert text to title format
# 14. Swap the case of text (lower → upper, upper → lower)
# 15. Add leading zeros to "45" to make it length 5

print(text.capitalize())

print(text.upper())

print(text.count("o"))

print(text2.strip())

print(text.replace("world","Python"))

print(text3.split(","))

print(text4.isalnum())

print(text4.isalpha())

print(text.find("world"))

print("-".join(["x","y","z"]))

print(text.startswith("hello"))

print(text.endswith("world"))

print(text.title())

print(text.swapcase())

print("45".zfill(5))
