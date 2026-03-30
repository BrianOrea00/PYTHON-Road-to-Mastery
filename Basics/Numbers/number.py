# Numbers
# there are three numeric types in python.
# int, float, complex.
# variables of numeric type are created when you assign a value to them.
# example1
x = 1
y = 2.2
z = 1j
# to verify the type of any object in python we can use type() function.
print(type(x))
print(type(y))
print(type(z))

# Int or integer is a whole number it can be positive or negative, without decimals, can be unlimited length.
# example2
xInt = 1
yInt = 4525734573567245656387689769753245
zInt = -56744
print(type(xInt))
print(type(yInt))
print(type(zInt))

# float or floatinf point number is a number it can also be positive, negative and containing one or more decimals.
# float can also be scientific number with an "e" to indicate the power of 10.
#example3
xFloat = 1.10
yFloat = -1254.345
zFloat = 78.865
print(type(xFloat))
print(type(yFloat))
print(type(zFloat))

xScie = 30e5
yScie = 11E2
zScie = -235.5e234
print(type(xScie))
print(type(yScie))
print(type(zScie))

# Complex numbers are written with a "j" as the imaginary part
# example4
xCom = 3+5j
yCom = 5j
zCom = -5j
print(type(xCom))
print(type(yCom))
print(type(zCom))

# You can convert from one type to another with the int(), float(), and complex() methods
# example5
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 
