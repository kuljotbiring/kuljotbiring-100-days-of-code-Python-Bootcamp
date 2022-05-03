"""
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given
sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.

You can get a list of the words in a string by using the .split() method:
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

# make each word into a list item
result = {word: len(word) for word in sentence.split()}

print(result)
