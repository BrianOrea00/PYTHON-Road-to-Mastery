# Bitwise Operator
# bitwise operators are used to compare (binary) numbers
# we have "&" AND: sets each bit to 1 if both bits are 1 otherwise it is set to 0
print(6 & 3)
"""
6 = 0110
3 = 0011
--------
2 = 0010
========
"""

# we have "|" OR: sets each bit to 1 if one of two bits is 1 otherwise it is set to 0
print(6 | 3)
"""
6 = 0110
3 = 0011
--------
7 = 0111
========
"""

# we have "^" XOR: sets each bit to 1 if only one of two bits is 1 otherwise it is set to 0
print(6 ^ 3)
"""
6 = 0110
3 = 0011
--------
5 = 0101
"""

# we have "~" NOT: inverts all the bits
print(~3)
"""
Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""

# we have "<<" Zero fill left shift: shift left by pushing zeros in from the right and let the left most bits fall off
print(3 << 2)
"""
If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

# we have ">>" Zero fill right shift: shift right by pushing copies of the left most bit in from left and let the right most bits fall off
print(8 >> 2)
"""
If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
