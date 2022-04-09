"""
You are going to write a program that calculates the average student height from a List of heights.

Important You should not use the sum() or len() functions in your answer. You should try to replicate their
functionality using what you have learnt about for loops.
"""
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

num_students = 0
sum_heights = 0

for student in student_heights:
    sum_heights += student
    num_students += 1

ave_height = round(sum_heights/num_students)

print(ave_height)