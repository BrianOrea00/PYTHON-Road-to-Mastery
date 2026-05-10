# AI generated problem

s = {"apple", "banana", "cherry"}

# 1. Remove "banana" using remove()
# 2. Remove "apple" using discard()
# 3. Use pop() and print set
# 4. Create:
nums = {1, 2, 3}
# clear the set
# 5. Print nums after clear()
# 6. Fix this safely:
# s.remove("grape")
# 7. Explain (comment):
# difference between remove() and discard()
# 8. Explain (comment):
# why pop() removes random item

s.remove("banana")
print(s)

s.discard("apple")
print(s)

x = s.pop()
print(x)
print(s)

nums = {1, 2, 3}
nums.clear()

print(nums)

s.discard("grape")

# this both methods delete a specified elements from a set remove() raises a KeyError if the item is missing and as for discard() will suppress the error and do nothing

# since python sets are unordered collections backed by a hash table pop() simply removes the first element currently stored in the internal memory structure which appears random to the user
