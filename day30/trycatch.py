
# File not found
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
# you can grab the error message that the except catches
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

# KeyError

# IndexError

# TypeError


"""
try: - something that might cause an exception
except: - do this if there was an exception
else: - do this if there were no exceptions
finally: - do this no matter what happens
"""
