# AI generated problem

fruits = ["banana", "apple", "cherry", "orange"]
numbers = [5, 2, 9, 1]
# 1. Sort fruits alphabetically
# 2. Sort fruits in descending order
# 3. Sort numbers ascending
# 4. Sort numbers descending
# 5. Sort fruits by length of word
# 6. Fix case issue:
words = ["banana", "Orange", "kiwi", "Cherry"]
# sort ignoring case
# 7. Reverse fruits list (not sort)
# 8. Explain (comment):
# difference between sort() and reverse()
# 9. Explain (comment):
# what key= does in sorting
# 10. Predict (no code):
# what happens if you sort a list with numbers and strings mixed

fruits.sort()
print(fruits)

fruits.sort(reverse = True)
print(fruits)

numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)

fruits.sort(key = len)
print(fruits)

words.sort(key = str.lower)
print(words)

fruits.reverse()
print(fruits)

# sort() arranges items in order
# reverse() just reverses the current order without sorting

# key= tells Python what value to use when comparing items during sorting

# the code will crash and gives us TypeError
