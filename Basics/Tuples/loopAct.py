# AI generated problem

t = ("a", "b", "c", "d")

# 1. Print all items using for loop
# 2. Print all items using index
# 3. Print all items using while loop
# 4. Print:
# "Item: a", "Item: b", ...
# 5. Print only first 2 items using loop
# 6. Print last item using loop (no direct index)
# 7. Count number of items using loop (not len)
# 8. Create new tuple:
nums = (1, 2, 3)
# print each number * 3

for x in t:
    print(x)

for x in range(len(t)):
    print(t[x])

x = 0
while x < len(t):
    print(t[x])
    x += 1

for x in t:
    print("Item:", x)

for x in t[:2]:
    print(t[x])

lastItem = None
for x in t:
    lastItem = x
print(lastItem)

count = 0
for x in t:
    count += 1
print(count)

for x in nums:
    print(x * 3)
