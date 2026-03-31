# AI generated problem.
# 1. Create variables using both single and double quotation: 1 each then print both.
# 2. Create a quote inside a quote variable then print.
# 3. Create a multiline string then print.
# 4. Access the first character and third character in word = "Python".
# 5. Make 1 loop through string.
# 6. Print the length of word variable in number 4.
# 7. Check if "easy" is in the sentence and Check if "hard" is not in the sentence use "in" and "not in".
#   sentence = "Python is easy to learn"
singQuote = 'Brian'
doubQuote = "Orea"
print(singQuote, doubQuote)

quoteInQuote = "It's Summer!!!!"
print(quoteInQuote)

multiLine = """ I will code every day
to improve my skills.
No Zero days we win this! """
print(multiLine)

word = "Python"
print("the first word is:", word[0], "and the third word is:", word[2])

for x in "this is  loop":
    print(x)

print(len(word))

sentence = "Python is easy to learn"
print("easy" in sentence)
print("hard" not in sentence)
