import random
import art
import worddict

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(worddict.word_list)


# Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(art.logo)
print(f"The answer is {chosen_word}")

# Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_"
# representing each letter to guess.
display = []

for char in chosen_word:
    display.append("_")

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
# letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
solved = False

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters
# in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while not solved and lives > 0:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: \n").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}\n")

    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for idx in range(0, len(chosen_word)):
        if chosen_word[idx] == guess:
            display[idx] = guess

    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life\n.")
        if lives == 0:
            print("You Lose")

    # Print 'display' and you should see the guessed letter in the correct position and every other letter
    # replace with "_".
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # check if no "_" remain ie word solved
    if "_" not in display:
        solved = True
        print("You win!")

    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(art.stages[lives])

