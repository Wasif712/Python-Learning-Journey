#  Exam Definition : A dictionary is a mutable collection of key-value pairs used to store and retrieve data using keys.
# Dictionaries : Ab extremely important structure. Dictionary data ko: key → value form mein store karta hai. Example:
# Think:
# name → Wasif
# age → 20
# marks → 85
student = { "name": "Wasif", "age": 20, "marks": 85 }  # yeh ek dictionary hai jo student ke name, age aur marks ko store karta hai. Dictionary me different data types ko store kar sakte hai.
print(student["name"])  # yeh dictionary me se specific key ka value ko print karta
print(student["age"])  # yeh dictionary me se specific key ka value ko print karta
print(student["marks"])  # yeh dictionary me se specific key ka value ko print karta

# Add New Key-Value Pair:
student["city"] = "Karachi"  # yeh dictionary me new key-value pair ko add karta hai.
print(student)

# Modify Existing Key-Value Pair:
student["age"] = 21  # yeh dictionary me existing key ka value ko modify karta hai.
print(student)

# Remove Existing Key-Value Pair:
student.pop("marks")  # yeh dictionary me existing key-value pair ko remove karta hai.
print(student)

# Dictionary Methods:
# keys() : yeh dictionary me se all keys ko print karta hai.
print(student.keys())

# values() : yeh dictionary me se all values ko print karta hai.
print(student.values())

# items() : yeh dictionary me se all key-value pairs ko print karta hai.
print(student.items())

for key, value in student.items():  # yeh loop pory dictionary ko iterate karta hai aur har key-value pair ko print karta hai.
    print(key, ":", value)

students = [ {"name": "Wasif", "marks": 85}, {"name": "Ali", "marks": 78}, {"name": "Ahmed", "marks": 92} ]
for student in students:
    print(student["name"], student["marks"])

for student in students:
    if student["marks"] >= 80:
            print(student["name"])

total = 0
for student in students:
    total += student["marks"]
    average = total / len(students)
    print("Average:", average)


# Nested Data Structures : Real-world data often nested hota hai. Example:
student = { "name": "Wasif", "subjects": {"Math": 80, "Python": 90, "Data Science": 85} }
# Access:
print(student["subjects"]["Python"])
for subject, marks in student["subjects"].items():
    print(subject, marks)