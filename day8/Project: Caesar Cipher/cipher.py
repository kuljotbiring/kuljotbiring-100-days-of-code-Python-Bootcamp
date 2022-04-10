import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(art.logo)


# Create a function called 'ceaser' that takes the 'text' and 'shift' as inputs.
# and creates or decodes a cipher using the alphabet and shift to move to different letters
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"


def caesar(txt, shift_num, encdec):
    message = ""
    new_index = 0
    for char in range(len(txt)):
        if txt[char].isalpha():
            # find the index in alphabet that the current index of the character is located
            index = alphabet.index(txt[char])
            if encdec == "encode":
                # if index goes beyond alphabet range of 25, go back to front of alphabet list
                if index + shift_num >= 26:
                    new_index = (index + shift_num) % 26
                # other-wise simply add to update the index
                else:
                    new_index = index + shift_num
            elif encdec == "decode":
                # if index goes beyond alphabet range of 0, go to the back of alphabet list to get index
                if index - shift_num <= -1:
                    new_index = (index - shift_num) % 26
                # other-wise simply subtract to update the index
                else:
                    new_index = index - shift_num
            # append character to message string
            message += alphabet[new_index]
        else:
            message += txt[char]
            # display the output message
    print(f"The {direction}d message is: {message}")


# use while loop to continue prompting user to continue until they decode to quit
use_cipher = True
while use_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    # prompt user to continue or not
    try_again = input("Would you like to continue? (Yes/No) ").lower()
    # update flag to continue to break out of loop and exit program
    if try_again == "no":
        use_cipher = False
    elif try_again == "yes":
        use_cipher = True
