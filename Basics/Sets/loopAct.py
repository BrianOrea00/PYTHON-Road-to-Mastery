# AI generated problem

s = {"apple", "banana", "cherry"}

# 1. Print all items using loop
# 2. Print:
# "Fruit: apple
# 3. Count items using loop
# (not len)
# 4. Check if "banana" exists
# 5. Check if "grape" is NOT in set
# 6. Fix this:
# for i in range(len(s)):
#     print(s[i])
# 7. Explain (comment):
# why sets are usually looped directly
# 8. Explain (comment):
# why output order may change

for x in s:
    print(x)

for x in s:
    print("Fruit:", x)

c = 0
for x in s:
    c += 1
print(c)

print("banana" in s)

print("grape" not in s)

for x in s:
    print(x)

# sets must be looped directly because they are unordered and do not support indexing making it impossible to access elements by a numerical position

# the output order change because sets use a hash table for storage where the internal mapping of items is affected by a randomized hash seed that can vary between execution sessions
