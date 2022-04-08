"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

    Take both people's names and check for the number of times the letters in the word TRUE occurs.

    Then check for the number of times the letters in the word LOVE occurs.

    Then combine these numbers to make a 2 digit number.

"""
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = str.lower(name1)
name2 = str.lower(name2)


first_true = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e')
second_true = name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')

first_love = name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e')
second_love = name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')

first_count = first_true + second_true
second_count = first_love + second_love

love_score = str(first_count) + str(second_count)

love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score >=40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")