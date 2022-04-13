"""
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
"""
import art
import random

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

# get player difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# set the lives to player chosen to difficulty
lives = 0
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

# choose a random lucky number
lucky_number = random.randint(1, 100)
print(lucky_number)
run_game = True

# keep running the game while flag is true
while run_game:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == lucky_number:
        print(f"You got it! The answer was {lucky_number}")
        run_game = False
    else:
        if guess > lucky_number:
            print("Too high.")
            lives -= 1
        else:
            print("Too low.")
            lives -= 1
        if lives == 0:
            print("You've run out of guesses, you lose.")
            run_game = False
        else:
            print("Guess again.")
