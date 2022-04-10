alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function called 'ceaser' that takes the 'text' and 'shift' as inputs.
# and creates or decodes a cipher using the alphabet and shift to move to different letters
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

def caesar(txt, shft, dir):
    message = ""
    new_index = 0
    for char in range(len(txt)):
        # find the index in alphabet that the current index of the character is located
        index = alphabet.index(txt[char])
        if dir == "encode":
            # if index goes beyond alphabet range of 25, go back to front of alphabet list
            if index + shft >= 26:
                new_index = index - 26
            # other-wise simply add to update the index
            else:
                new_index = index + shft
        elif dir == "decode":
            # if index goes beyond alphabet range of 0, go to the back of alphabet list to get index
            if index - shft <= -1:
                new_index = (index - shft) + 26
            # other-wise simply subtract to update the index
            else:
                new_index = index - shft
        # append character to message string
        message += alphabet[new_index]
    # display the output message
    print(f"The {dir}d message is: {message}")


caesar(text, shift, direction)
