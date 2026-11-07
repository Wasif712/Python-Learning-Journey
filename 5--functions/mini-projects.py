students = [{"name": "Wasif", "age": 21, "marks": [80, 90, 86]},
            {"name": "Anus",  "age": 20, "marks": [75, 85, 60]},
            {"name": "Ahmed", "age": 22, "marks": [88, 92, 95]},
            {"name": "Sara", "age": 19, "marks":  [45, 51, 40]}]

def calculate_average(marks):
    total = sum(marks)
    return total / len(marks)

def get_status(average):
    if average >= 80:
        return "Exellent"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"

for student in students:
    average = calculate_average(student["marks"])
    status = get_status(average)
    print(student["name"], "Average:", average, "Status:", status)
