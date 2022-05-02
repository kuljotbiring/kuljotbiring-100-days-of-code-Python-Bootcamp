"""
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a
Loop.
"""
# open both files and read into variables splitting lines - makes each line a list element
with open("file1.txt") as f:
    first_list = f.read().splitlines()

with open("file2.txt") as f:
    second_list = f.read().splitlines()

# make the result an integer and use list comprehension for two lists
result = [int(i) for i, j in zip(first_list, second_list) if i in second_list]

# can also simply do this
result_simple = [int(number) for number in first_list if number in second_list]

# Write your code above 👆

print(result)
print(result_simple)
