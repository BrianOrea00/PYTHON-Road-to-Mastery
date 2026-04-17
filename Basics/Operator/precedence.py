# Operator Precedense
# operator precedense describes the order in which operations are performed
# example 1
# parenthesis has the highest precedence meaning that expresions inside parentheses must be evaluated first
print((6 + 3) - (6 + 3))

# example 2
# multiplication has higher precedense than addition and therefore multiplications are evaluated before additions
print(100 + 5 * 3)

# Precedense Order
# the precedense order is described below starting with the highest precedense at the top:
# we have "()" parenthesis
print((4 + 6) - (4 + 6))

# we have "**" exponentiation
print(100 - 3 ** 3)

# we have "+x, -x, ~x" Unary plus, unary minus, and bitwise NOT
print(100 + ~3)

# we have "*, /, //, %" Multiplication, division, floor division, and modulus
print(85 + 5 * 3)

# we have "+, -" Addition and subtraction
print(115 - 5 * 3)

# we have "<< >>" Bitwise left and right shift
print(8 >> 4 - 2)

# we have "&" Bitwise AND
print(6 & 2 + 1)

# we have "^" Bitwise XOR
print(6 ^ 2 + 1)

# we have "|" Bitwise OR
print(6 | 2 + 1)

# we have "==, !=, >, >=, <, <=, is, is not, in, in not" Comparison, Identity, and membership operator
print(5 == 4 + 1)

# we have "not" logical not
print(not 5 == 5)

# we have "and" logical AND
print(1 or 2 and 3)

# we have "or" logical OR
print(4 or 5 + 10 or 8)

# Left to Right Evaluation
# if two operator have same precedense the expresion is evaluated from left to right
print(5 + 4 - 7 + 3)
