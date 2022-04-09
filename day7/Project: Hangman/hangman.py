import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_"
# representing each letter to guess.

display = []

for char in chosen_word:
    display.append("_")

print(display)

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
# letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

solved = False

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters
# in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while solved == False:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for idx in range(0, len(chosen_word)):
        if chosen_word[idx] == guess:
            display[idx] = guess

    # Print 'display' and you should see the guessed letter in the correct position and every other letter
    # replace with "_".
    # print(display)
    print(display)

    # check if no "_" remain ie word solved
    if "_" in display:
        continue
    else:
        solved = True
        print("You won!")



