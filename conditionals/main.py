print("Conditional Statement")

# if else condtion
marks = int(input("Enter your marks: "))
if marks >= 50:
    print("Pass")
else:
    print("Fail")

if marks > 90:
    print("Position Holder")
else:
    print("Not Position Holder")

# elif & How the Chain Works
if marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")
elif marks >= 60:
    print("D Grade")
elif marks >= 50:
    print("E Grade")
else:
    print("Fail")

# Logic Operators (and, or, not)
age = 20
if age >= 18 and marks >= 50:
     print("Eligible")

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Weekend")


is_student = True
if not is_student:
    print("Not a student")
