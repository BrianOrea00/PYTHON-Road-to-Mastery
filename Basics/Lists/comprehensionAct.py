# List Comprehension Activity (basic)

fruits = ["apple", "banana", "cherry", "kiwi"]
# 1. Create a new list with all items (copy list)
# 2. Create a list with items that contain letter "a"
# 3. Create a list with items that are NOT "banana"
# 4. Create a list where all items are uppercase
# 5. Create a list with numbers from 0 to 4 using range()
# 6. Create a list with numbers less than 5 from range(10)
# 7. Create a list where each number is multiplied by 2
numbers = [1, 2, 3]
# 8. Replace "banana" with "orange" using comprehension
# 9. Explain (comment):
# difference between for loop and list comprehension
# 10. Explain (comment):
# when NOT to use list comprehension

newlist1 = [a for a in fruits]
print(newlist1)

newlist2 = [b for b in fruits if "a" in b]
print(newlist2)

newlist3 = [c for c in fruits if c != "banana"]
print(newlist3)

newlist4 = [d.upper() for d in fruits]
print(newlist4)

newlist5 = [e for e in range(5)]
print(newlist5)

newlist6 = [f for f in range(10) if f < 5]
print(newlist6)

newlist7 = [g * 2 for g in numbers]
print(newlist7)

newlist8 = [h if h != "banana" else "orange" for h in fruits]
print(newlist8)

# a loop is a statement that used for general iteration and perform many actions
# a list comprehension is an expression that create new list in a shorter and cleaner way

# do not use list comprehension when the logic is too complex pr hard to read
# also avoid it when we are not creating new list
