alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(txt, shft):
    message = []
    for char in range(len(txt)):
        # find the index in alphabet that the current index of the character is located
        index = alphabet.index(txt[char])
        # if index goes beyond alphabet range of 25, go back to front of alphabet list
        if index + shft >= 26:
            index -= 26
        # add to message, the letter shifted x spaces over in alphabet
        message.append(alphabet[index + shft])
    # change list to string and print it
    message = ''.join(message)
    print(f"The encoded message is: {message}")


def decrypt(txt, shft):
    message = []
    for char in range(len(txt)):
        # find the index in alphabet that the current index of the character is located
        index = alphabet.index(txt[char])
        # if index goes beyond alphabet range of 0, go to the back of alphabet list
        if index - shft <= -1:
            index = (index - shft) + 26
            # add to message, the letter shifted x spaces over in alphabet
            message.append(alphabet[index])
        else:
            # add to message, the letter shifted x spaces over in alphabet
            message.append(alphabet[index - shft])
    # change list to string and print it
    message = ''.join(message)
    print(f"The decoded message is: {message}")

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and
# print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# #HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# #🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
# message.


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("You did not select a proper choice. Re-run the program and try again")
