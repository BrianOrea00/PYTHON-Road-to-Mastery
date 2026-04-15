# Memebership Operator
# membership operators are used to test if a sequence is presented in an object
# we have "in" returns true if a sequence with the specified value is present in the object
x = ["Adobo","Nilaga"]
print("Adobo" in x)
# returns True because a sequence with the value "Adobo" is in the list

# we have "not in" returns true if a sequence with the specified value is not present in the object
print("Kare-Kare" not in x)
# returns True because a sequence with the value "Kare-Kare" is not in the list

# membership in string
# membership operators also work with string
text = "Waffle Maker"
print("W" in text)
print("waffle" in text)
print("Hotdog" not in text)
