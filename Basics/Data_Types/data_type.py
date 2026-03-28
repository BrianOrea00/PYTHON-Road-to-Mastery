# Data Types
# in Python there is a built in data types by default.
# 1. we have text type or str.
# 2. we have numeric type this are int, float, complex
# 3. we have sequence types and this are list, tuple, range.
# 4. we have mapping type or dict.
# 5. we have set types and this are set and frozenset.
# 6. we have boolean type or bool
# 7. we have binary type and this are bytes, bytearray, memoryview
# 8. then the none type or NoneType.
# here are the examples.
x1 = "Hello world" # used for text
print(x1)

x2 = 99 # used for whole number
print(x2)

x3 = 99.9 # used for decimal number
print(x3)

x4 = 1j # used for number with real + imaginary part this also used for advance math not common in basic apps
print(x4)

x5 = ["Hotdog", "Pizza", "Adobong paa ng  manok"] # ordered and changeable
print(x5)

x6 = ("Nilaga", "Mechado", "Kare-kare")# ordered and not changeable
print(x6)

x7 = range(10) # sequence of number
print(x7)

x8 = {'Name': 'Brian Orea', 'Age': 23} # dictionary, by pair, key-value
print(x8)

x9 = {"Desktop", "Laptop", "Phone"} # changeable
print(x9)

x10 = frozenset({"Meat Ball", "Spaghetti", "Lomi"}) # not changeable
print(x10)

x11 = True # yes or no, 1 or 0, true or false
print(x11)

x12 = b"Nyahalo" # immutable binary
print(x12)

x13 = bytearray(5) # mutable binary
print(x13)

x14 = memoryview(bytes(5))# access binary without copying
print(x14)

x15 = None # means “no value”
print(x15)

# If you want to specify the data type, you can use the following constructor functions
# example
x16 = str("Hello World")
print(x16)
