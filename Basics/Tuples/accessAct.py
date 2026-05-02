# AI generated problem
t = ("a", "b", "c", "d", "e")

# 1. Print second item
# 2. Print last item
# 3. Slice from index 1 to 4
# 4. Slice from start to index 3
# 5. Slice from index 2 to end
# 6. Slice using negative index (-4 to -1)
# 7. Check if "c" is in tuple
# 8. Check if "x" is not in tuple

print(t[1])

print(t[-1])

print(t[1:4])

print(t[:3])

print(t[2:])

print(t[-4:-1])

if "c" in t:
    print("Exists")

if "x" not in t:
    print("Not found")
