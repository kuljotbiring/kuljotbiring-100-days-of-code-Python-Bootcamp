# regular way of creating a new list
numbers = [1, 2, 3]
new_list = []

for n in numbers:
    new_number = n + 1
    new_list.append(new_number)

# new_ list will now hold [2, 3, 4]
print(new_list)

# using list comprehension we use the following format:
# new_list = [new_item for item in list]
# where new_item is what you want to happen, n is the iterator and list is what to iterate over

newer_list = [n + 1 for n in numbers]
print(newer_list)

# you can use list comprehension on lists, strings, range, and tuples
name = "Kuljot"

char_list = [letter for letter in name]
print(char_list)

double_list = [num * 2 for num in range(1, 5)]
print(double_list)

# conditional list comprehension
# new_list = [new_item for item in list if test]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# use list comprehension to make a list of names only four letters long
short_names = [name for name in names if len(name) < 5]
print(short_names)

# now take the names that are 5 letters or longer and turn them into uppercase names
cap_names = [name.upper() for name in names if len(name) >= 5]
print(cap_names)

