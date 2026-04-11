# Assignment
# assignment operators are used to assign values to variables.
# we have "=" equal.
a = 5
print(a)

# we have "+=" addition.
a += 3
print(a)
# this is same as a = a + 3

# we have "-=" subtraction.
a -= 2
print(a)
# this same as a = a - 2

# we have "*=" multiplication.
a *= 3
print(a)
# this is same as a = a * 3

# we have "/=" division.
a /= 3
print(a)
# this is same as a = a / 3

# we have "%=" modulus.
a %= 5
print(a)
# this is same as a = a % 5

# we have "//=" floor division.
b = 7
b //= 2
print(b)
# this is same as b = b // 2

# we have "**=" exponent.
b **= 3
print(b)
# this is same as b = b ** 3

# Bitwise Assignment
# bitwise operators works on binary (bits: 1 and 0) not normal decimal math.
# they are mainly used in low level tasks optimization or flags.
# first is to understand then binary
# in here we have an example
c = 5 # in binary 0101 
d = 3 # in binary 0011

# we have "&" AND : compare bits both must be 1 
print(c & d)
# the output will be 1, why? because
# 0101
# 0011
# ----
# 0001 so thats it is 1

# we have "|" OR : at least one is 1
print(c | d)
# the output will be 7, why? because
# 0101
# 0011
# ----
# 0111 if we convert this into whole num this will be 7

# we have "^" XOR : different bit is 0 and same is 1
print(c ^ d)
# the output will be 6, why? because
# 0101
# 0011
# ----
# 0110 if we convert thiis into whole num this will be 6

# we have "~" NOT : flips bits 0 =1 and 1 - 0
print(~ c)
# This looks weird because Python uses signed binary (two’s complement)

# we have "<<" LEFT SHIFT : moves bits to the left (adds zeros)
print(c << 1)
# this will be 10 why is that? because we add zeros
# 0101 then we add 0
# this will be 1010 and if we convert this the answer is 10

# we have ">>" RIGHT SHIFT : moves bits to the right (adds zeros)
print(c >> 1)
# this will be 2 why is that? because we add zeros
# 0101 thien we add 0
# this will be 0010

# so every left shift = multiple by 2
# and every right shift = floor division by 2
# simple way to remember
# <<  makes number bigger
# >>  makes number smaller
