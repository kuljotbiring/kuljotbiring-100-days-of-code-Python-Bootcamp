# open the specified file
with open("my_file.txt") as file:

    # store the contents of the file into a string
    contents = file.read()

    print(contents)

    # close the file
    # file close not needed when using with
    # file.close()

# this will overwrite the text using w for write
# if no file with this name exists it will be created
with open("new_file.txt", mode="w") as file:
    # new stuff to be overwritten with
    file.write("New Text")


# this will append the text using a for append
with open("my_file.txt", mode="a") as file:
    # new stuff to be overwritten with
    file.write("\nI love burritos")
