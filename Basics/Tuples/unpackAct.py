# AI generated problem

t = ("red", "green", "blue", "yellow")

# 1. Unpack first 3 values into variables
# 2. Use * to store remaining values in one variable
# 3. Unpack first and last, middle should go to *
# 4. Fix this error:
# a, b = t
# 5. Create a tuple and unpack into 2 variables
# 6. Explain (comment):
# what * does in unpacking
# 7. Explain (comment):
# why number of variables must match values
# 8. Predict output:
a, *b = (1, 2, 3, 4)
# what is b?
# 9. Predict:
x, y = (10, 20)
# what is x and y?

(a, b, c) = ("red", "green", "blue")
print(a, b, c)

(d, e, f, *g) = t
print(d, e, f, g)

(h, *i, j) = t
print(h, i, j)

(a, *b) = t
print(a, b)

myTuple = ("First", "Second", "Third", "Forth")
(x, *y) = myTuple
print(x, y)

# the asterisk act as catch all that collects any remaining values into a list

# the number of variables must match values to ensure each variable receives exactly one value (unless using *)

# My predictio is it will print 2 to 4

# the x = 10 and y = 20
