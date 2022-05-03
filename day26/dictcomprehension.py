import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# dictionary comprehension pseudocode
# new_dict = {new_key:new_value for item in list}
score_dict = {name: random.randint(0, 100) for name in names}

# now we have a new dictionary with student names as keys and random numbers as scores
print(score_dict)

# iterate over a dictionary to create a new dictionary based on a test
passed_students = {student: score for (student, score) in score_dict.items() if score >= 60}
print(passed_students)