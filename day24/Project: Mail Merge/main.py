# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACE_HOLDER = "[name]"

# make a list to hold formatted names
names = []

# get to the location of the list of names and read from that file
with open("./Input/Names/invited_names.txt") as name_file:
    name = name_file.readlines()
    # go through the read lines and remove extra space or new line chars. add cleaned names to new list
    for invited in name:
        names.append(invited.strip())

# access the starting letter file
with open("./Input/Letters/starting_letter.txt") as file:
    # store all contents in a string
    letter_contents = file.read()
    # make a new letter using the stored names with replace
    for guest in names:
        # new_letter now holds string of specific name invite
        new_letter = letter_contents.replace(PLACE_HOLDER, guest)

        # create the name and the path of the new letters to create
        file_location = f"./Output/ReadyToSend/letter_for_{guest}.txt"

        # stick the example letter contents into newly made letter into the desired directory
        with open(file_location, mode="w") as finished_letter:
            finished_letter.write(new_letter)







