# AI generated problem
# 1. Debug this
#   age = 20
#   text = "I am " + age
#   print(text)
# 2. Using format() Method: Create name variable and age variable that will make a sentence.
# 3. F-String: Create a variable that uses f-string.
# 4. Multiple Values: Create 3 or more variables that will make a sentence.
# 5. Format with Decimal: Using price = 123 make a sentence out of this

age = 23
text = f"I am {age}"
print(text)

name = "Brian Orea"
print("Hi! my name is {} and I am {} years old".format(name,age))

a = "F-String"
print(f"This is {a}")

emotion = "Love"
food1 = "Adobo"
food2 = "Kare-Kare"
print("I {} eating {} and {}".format(emotion,food1,food2))

price = 123
print(f"The Price of Adobo is {price:.2f} same as Kare-Kare")
