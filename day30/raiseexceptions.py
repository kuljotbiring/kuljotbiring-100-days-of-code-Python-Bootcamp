# raise is making your own exception
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# # you can grab the error message that the except catches
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # create your own exception here
#     raise TypeError("This is an error that I made up")

# create your own exception
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")
bmi = weight / height ** 2
print(bmi)