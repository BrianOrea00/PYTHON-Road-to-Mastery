# Format
# we cannot combine strings and numbers.
# but we can combine the strings and numbers by using f-strings or the format() method.

# F-strings
# f-strings was introduced in python 3.6 and is now the preferred way of formatting strings.
# to specify a string as an f string simply put an "f" in the front of the string literal and add curly brackets {} as placeholder for variables and other operations.
# example1
age = 23
intro = f"My name is Brian, I am {age}"
print(intro)

# Placeholder and modifiers
# a placeholder can contain variables, operations, functions, and modifiers to format the value.
# a placeholder can include a modifier to format the value.
# a modifier is included by adding a colon ":" followed by a legal formatting type like ".2f"
# which means fixed point number with 2 decimals.
# example2
price = 99
prod = f"The Price of the Hotdog is {price:.2f} pesos."
print(prod)

# a placeholder can contain python code like math operations.
# example3
total = f"The total are: {99 * 2} pesos."
print(total)

