student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# loop through a dictionary
for key, values in student_dict.items():
    print(key, values)

import pandas

# create a data frame
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a data frame
for key, value in student_data_frame.items():
    print(value)

# pandas actually has a build in loop method that loop through rows
for (index, row) in student_data_frame.iterrows():
    print(row.student)
