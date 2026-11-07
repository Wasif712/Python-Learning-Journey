print("Hello World")

x = 3
y = 4
print(x+y)

# Data Types
age = 20
percentage = 85.5
name = "Wasif"
is_student = True

# Type Checking Function
print(type(age))
print(type(percentage))
print(type(name))
print(type(is_student))

a = 10
b = 3
# Arithmetic Operations
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # Floor Division
print(a ** b)  # Exponentiation
print(a % b) # Modulus (Remainder)

#  Comparison Operators & == vs is 

num1 = 10
num2 = 20

print(num1 == num2)  # False
print(num1 is num2)  # False
print(num1 != num2)  # True
print(num1 > num2)   # False
print(num1 < num2)   # True
print(num1 >= num2)  # False
print(num1 <= num2)  # True
print(num1 is not num2)  # True
print(num1 is num1)  # True
# == → same value?        // The == operator tests whether two values are equal.
# is → same object        // The is operator checks whether two references refer to the same object.

email = input("Enter Your Email: ")
print("Your Email is: " + email)

tell = int(input("Enter Your Phone Number: "))
print("Your Phone Number is: " + str(tell))

amount = float(input("Enter Your Amount: "))
print("Your Amount is: " + str(amount))