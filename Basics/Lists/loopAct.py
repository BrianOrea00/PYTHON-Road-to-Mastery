# AI generated problem

fruits = ["apple", "banana", "cherry"]
# 1. Print all items using a for loop
# 2. Print all items using index (range + len)
# 3. Print all items using while loop
# 4. Print each item with text:
# example: "Fruit: apple"
# 5. Count how many items are in the list using len()
# 6. Print only the first 2 items using slicing + loop
# 7. Print the last item using loop (not direct index)
# 8. Create a new list:
numbers = [10, 20, 30]
# Loop and print each number multiplied by 2
# 9. Explain (comment):
# difference between for loop and while loop
# 10. Explain (comment):
# why for loop is easier for lists

for a in fruits:
    print(a)

for b in range(len(fruits)):
    print(fruits[b])

c = 0
while c < len(fruits):
    print(fruits[c])
    c += 1

for d in fruits:
    print("Fruit:", d)

print(len(fruits))

for e in fruits[:2]:
    print(e)

lastItem = ""
for f in fruits:
    lastItem = f
print(lastItem)

for g in numbers:
    print(g * 2)

# for loop is used to iterate through items in a sequence automatically
# while loop runs based on a condition and requires manual control

# for loop is easier for lists because it handles the iteration logic automatically so we dont need to create counter variable or 
# increment it manually or out of range index errors
