students = [
[80, 75, 90],
[65, 70, 85],
[90, 95, 88],
[40, 45, 50]
]
student_number = 1
for marks in students:
    total = 0
    for mark in marks:
        total += mark
    average = total / len(marks)

    if average >= 80:
        status = "Excellent"
    elif average >= 50:
        status = "Pass"
    else:
        status = "Fail"
    print(
        "Student:", student_number,
        "Average:", average,
        "Status:", status)
    student_number += 1