# AI generated problem
# use this
x = 10
y = 5

# 1. Assign 20 to variable a
# 2. Add 5 to x using +=
# 3. Subtract 2 from y using -=
# 4. Multiply x by 2 using *=
# 5. Divide x by 2 using /=
# 6. Get remainder of x divided by 3 using %=
# 7. Use floor division on x by 2 using //=
# 8. Raise y to the power of 2 using **=
# 9. Rewrite this using assignment operator:
# x = x + 3
# 10. Explain this:
# x += y

# --- Bitwise Assignment ---
# 11. Use &= operator between x and y
# 12. Use |= operator between x and y
# 13. Use ^= operator between x and y
# 14. Use right shift assignment on x by 1 (>>=)
# 15. Use left shift assignment on x by 1 (<<=)

a = 20
print(a)

x += 5
print(x)

y -= 2
print(y)

x *= 2
print(x)

x /= 2
print(x)

x %= 3
print(x)

x //= 2
print(x)

y **= 2
print(y)

x += 3
print(x)

# this is called augmented assignment operator
# is it shorthand way of writing
# x = x + y

x = int(x) # why i do this? because the x became float so i need to convert in to int to do this 

print(f"This is X: {x} and This is Y: {y}")
x &= y
print(x)

x |= y
print(x)

x ^= y
print(x)

x >>= 1
print(x)

x <<= 1
print(x)
