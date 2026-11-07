students = [{ "name": "Wasif", "marks": 85, "attendance": 90},
            { "name": "Ali", "marks": 72, "attendance": 80},
            { "name": "Ahmed", "marks": 45, "attendance": 70},
            { "name": "Sara", "marks": 92, "attendance": 95}]
# Now process:
for student in students:
    if student["marks"] >= 80 and student["attendance"] >= 75:
            status = "Excellent"
    elif student["marks"] >= 50 and student["attendance"] >= 75:
            status = "Pass"
    else:
            status = "Fail"
print(student["name"], "→", status)
# Output:
# Wasif → Excellent
# Ali → Pass
# Ahmed → Fail
# Sara → Excellent
# Is project mein tumne combine kiya:
# List
# Dictionary
# Loop
# if
# elif
# else
# and
# Data filtering