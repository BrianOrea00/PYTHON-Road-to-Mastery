# AI generated problem

fruits = ["apple", "banana", "cherry", "orange"]

# 1. Change "banana" to "mango"
# 2. Change "cherry" to "grape"
# 3. Replace "banana" and "cherry"
# with ["x", "y"]
# 4. Replace ONLY "banana"
# but insert 2 items instead
# 5. Replace "banana" and "cherry"
# with only one item
# 6. Insert "pineapple" at index 2
# 7. Insert "lemon" at the beginning
# 8. Insert "melon" at the end using insert()
# 9. Explain (comment):
# what happens when you replace 1 item with 2 items
# 10. Explain (comment):
# what happens when you replace 2 items with 1 item

fruits[1] = "mango"
print(fruits)

fruits[2] = "grape"
print(fruits)

fruits[1:3] = ["x", "y"]
print(fruits)

fruits[1:2] = ["kiwi", "blueberry"]
print(fruits)

fruits[1:3] = ["jackfruit"]
print(fruits)

fruits.insert(2, "pineapple")
print(fruits)

fruits.insert(0, "lemon")
print(fruits)

fruits.insert(len(fruits), "melon")
print(fruits)

# if we replace 1 item with 2 items it will increase the list size and the remaining items will move accordingly

# if we replace 2 items with 1 item it will reduce the the list size and the remaining items will move accordingly
