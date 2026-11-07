def calculate_average(marks):  # A function is a reusable block of code designed to perform a specific task
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)
print(calculate_average([85, 90, 78, 92, 88]))  # An argument is a value passed to a function when the function is called.

def greet():
    return "Hello, World!"
print(greet())

def show_massage():
    print("This is a simple message.")
show_massage()

def greet(name):  # A parameter is a variable specified in a function definition that receives a value when the function is called.
    print("Hello,", name)
greet("Wasif")  # A function call is an instruction that executes a previously defined function.


def greet(name="Student"):
    print("Hello", name)
greet()

def student_info(name, marks):
    print("Name:", name)
    print("Marks:", marks)
student_info("Wasif", 84)

def add(a,b):
    result = a + b
    print("The sum of", a, "and", b, "is", result)
add(23, 5)

def multiply(a,b):   # Important
    return a * b     # The return statement terminates a function and sends a value back to the caller
result = multiply( 4, 5)
print("The product of 4 and 5 is", result)

def calculate():
    x = 10       # A local variable is a variable created inside a function and accessible only within that function.
    print(x)
calculate()

x = 100    # A global variable is a variable defined outside a function and generally accessible throughout the program.
def show():
    print(x)
show()

def check_result(marks):
    if marks >= 90:
        print("Congratulations you got position")
        return "Pass"
    elif marks >= 80:
        print("A Grade")
        return "Pass"
    elif marks >= 70:
        print("B Grade")
        return "Pass"
    elif marks >= 60:
        print("C Grade")
        return "Pass"
    elif marks >= 50:
        print("D Grade")
        print("Passed")
        return "Improvement Required!"
    else:
        return "Fail"
print(check_result(int(input("Enter your marks: "))))