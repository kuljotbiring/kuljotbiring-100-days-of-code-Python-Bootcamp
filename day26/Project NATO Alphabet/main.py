import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# make the csv file into a data frame
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# make the data frame into a dictionary
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_word = False

while not is_word:
    # get the user input
    user_input = input("Enter a word: ").upper()
    try:
        # make a list of the phonetic words associated with the user input
        phonetic_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters n the alphabet please")
    else:
        print(phonetic_list)
        is_word = True

