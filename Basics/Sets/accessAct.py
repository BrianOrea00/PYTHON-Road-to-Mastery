# Ai generated problem

s = {"apple", "banana", "cherry"}

# 1. Print all items using loop
# 2. Check if "banana" exists
# 3. Check if "grape" is NOT in set
# 4. Fix this error:
# print(s[0])
# 5. Print each item with:
# "Fruit: apple"
# 6. Count number of items using loop
# (not len)
# 7. Explain (comment):
# why sets cannot use indexing
# 8. Explain (comment):
# why order in sets is unreliable

for x in s:
    print(x)

print("banana" in s)

print("grape" not in s)

for x in s:
    print(x)

for x in s:
    print("Fruit:", x)

count = 0
for x in s:
    count += 1
print(count)

# Sets are implemented using hash tables where elements are stored based on their calculateed hash value rather than a sequential position making integer based indexing impossible

# order is unreliable because sets use hashing and do not store elements in a fixed sequence
