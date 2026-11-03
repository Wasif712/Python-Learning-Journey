print("Student Marks Calculator")

# Get the number of subjects
student_name = input("Enter Student Name: ")
math_marks = input("Enter Math Marks: ")
programming_marks = input("Enter Programming Marks: ")
data_science = input("Enter Data Science Marks: ")

# Calculate the total and average
total_marks = int(math_marks) + int(programming_marks) + int(data_science)
average_marks = total_marks / 3

print("Student Name: " + student_name)
print("Total Marks: " + str(total_marks))
print("Average Marks: " + str(average_marks))
print("Percentage: " + str(average_marks) + "%")