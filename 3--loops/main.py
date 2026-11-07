# Loops

# for variable in sequence:
#   statement

for i in range(5):
    print("Hellow World")

# RULE : range(n) generates values starting from 0 up to but not including n.
for i in range(5):
    print(i)

for i in range(0, 10, 2):
    print(i)
for i in range(10, 0, -1):
    print(i)

for student_id in range(1, 11):
    print("Processing student:", student_id)

marks = [70, 80, 36, 76, 50, 44, 28, 90, 60, 85]
total_marks = 0
for mark in marks:
    print(mark)
    total_marks += mark

print("Total Marks:", total_marks)
average = total_marks / len(marks)
print("Average Marks:", average)

min = marks[0]  # minimum mark array ka pehla element store kar do.

for i in marks:
    if i < min:  # agar naya number purany number sy chota hai to
        min = i  # naya number ko min main store kar do.
print("Minimum Marks:", min)

max = marks[0]  # maximum mark array ka pehla element store kar do.
for i in marks:
    if i > max:  # agar naya number purany number sy bara hai to
        max = i  # naya number ko max main store kar do.
print("Maximum Marks:", max)

passed_students = 0
for i in marks:
    if i >= 50:
        passed_students += 1
print("Number of students Passed:", passed_students)

failed_students = 0
for i in marks:
    if i < 50:
        failed_students += 1
print("Number of students Failed:", failed_students)



