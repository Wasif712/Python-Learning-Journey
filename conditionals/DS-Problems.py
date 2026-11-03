# 1 — Student Scholarship Eligibility
marks = 85
attendance = 82
if marks >= 80 and attendance >= 75:
    print("Eligible for Scholarship")
else:
    print("Not Eligible")

# 2 — Customer Segmentation Rule
spending = 150000
if spending >= 100000:
    print("Premium Customer")
else:
    print("Regular Customer")

# 3 — Transaction Risk
amount = 150000
unusual_location = True
if amount > 100000 and unusual_location:
    print("Flag Transaction")
else:
    print("Normal Transaction")

    
# Nested Conditions: A nested conditional is a conditional statement placed inside another conditional statement.
marks = 85
attendance = 80
if marks >= 50:
    if attendance >= 75:
        print("Pass and Attendance Requirement Met")
    else:
        print("Pass but Attendance Requirement Not Met")
else:
    print("Fail")