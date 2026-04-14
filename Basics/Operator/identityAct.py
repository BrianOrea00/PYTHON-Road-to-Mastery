# AI generated problem
# use this
a = [1, 2, 3]
b = [1, 2, 3]
c = a
x = 10
y = 10

# 1. Check if a and b are the same object
# 2. Check if a and c are the same object
# 3. Check if a and b have equal value
# 4. Check if a is not b
# 5. Check if c is not a
# 6. Check if x is y
# 7. Explain why #6 might be True (no code, just comment)
# 8. Fix this mistake:
# if a == c:
#     print("Same object")
# 9. Create a condition:
# print "Same" if a is c, else print "Different"
# 10. Compare:
# check if b is not c

print(a is b)

print(a is c)

print(a == b)

print(a is not b)

print(c is not a)

print(x == y)

# Python reuses small integers (-5 to 256), so both variables may point to same memory object

if a is c:
    print("Same object")

if a is c:
    print("Same")
else:
    print("Different")

print(b is not c)
