# AI generated problem

fruits = ["apple", "banana", "cherry", "banana", "orange"]
# 1. Remove "banana" using remove()
# 2. Remove the first item using del
# 3. Remove the item at index 2 using pop()
# 4. Remove the last item using pop() without index
# 5. Store the removed item from pop() into a variable and print it
# 6. Create a new list:
numbers = [1, 2, 3, 4]
# Remove the second item using del
# 7. Clear the numbers list
# 8. Print numbers (after clear)
# 9. Explain (comment):
# difference between remove() and pop()
# 10. Explain (comment):
# what happens when you clear a list

fruits.remove("banana")
print(fruits)

del fruits[0]
print(fruits)

fruits.pop(2)
print(fruits)

fruits.pop()
print(fruits)

removed = fruits.pop()
print(removed)
print(fruits)

del numbers[1]
print(numbers)

numbers.clear()

print(numbers)

# in remove() method removes by value
# in pop() method this removes by index and returns the removed item

# when we clear a list it will remove all item but the list still remains
