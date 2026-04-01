# slicing
# wew can return a range of character by using the slicing syntax.
# specify the start index and the end index separated by a colon ":" to return a part of the string.
# example1
a = "Hello, World"
print(a[2:5])
# here it will show "llo" why is that?
# because the start is 0 so H = 0, e = 1, l = 2, l = 3, o = 4 then "," is 5.
# why "," is not included?
# because it makes length calculation easier: len(b[2:5]) = 5 - 2 = 3.

# Slice from the start
# by leaving out the start index the range will start at the first character.
# example2 (we will use the hello world above)
print(a[:5])

# Slice to the end
# by leaving out the end index the range will go to the end.
# example3 (we will use the hello world above)
print(a[2:])

# Negative Indexing
# use negative indexes to start the slice from the end of the string.
# example4 (we will use the hello world above)
print(a[-5:-2])
