def remove_remaining_numbers(data):
        cleaned_data = []
        for i in data:
            if i is not None:
                cleaned_data.append(i)
        return cleaned_data
data = [1, 2, None, 4, None, 6]
cleaned_data = remove_remaining_numbers(data)
print(cleaned_data)  # Output: [1, 2, 4, 6]

def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    higest = max(marks)
    lowest = min(marks)
    return total, average, higest, lowest
marks = [85, 90, 78, 92, 88]
total, average, higest, lowest = analyze_marks(marks)
print("Total:", total)        # Output: Total: 433
print("Average:", average)    # Output: Average: 86.6
print("Highest:", higest)      # Output: Highest: 92  
print("Lowest:", lowest)        # Output: Lowest: 78

def validate_marks(marks):
    invalid = []
    for mark in marks:
        if mark < 0 or mark > 100:
            invalid.append(mark)
    return invalid
marks = [80, 90, 105, -10, 75]
invalid_marks = validate_marks(marks)
print("Invalid:", invalid_marks)