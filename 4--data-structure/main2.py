#  Tuples : Tuple list jaisa hota hai, lekin normally immutable hota hai.

coordinates = (24.86, 67.01) # yeh ek tuple hai jo 2 coordinates ko store karta hai. Tuple me different data types ko store kar sakte hai.
print(coordinates[0])  # python m index 0 sy start hoti hai. Positive index 0,1 hoti hai.

# coordinates[0] = 25  # yeh error dega kyunki tuple immutable hota hai. Tuple me element ko update nahi kar sakte hai.
# When to Use Tuple?  // Agar data logically fixed hai: location = (24.86, 67.01) to tuple useful ho sakta hai.


# Sets : Set unique elements store karta hai.
# Exam Definition : A set is an unordered collection of unique elements in Python.
# Set me different data types ko store kar sakte hai.
# Set me duplicate values ko remove kar deta hai. 
# Set me order maintain nahi hota hai. 
# Set me indexing nahi hoti hai. 
# Set me slicing nahi hoti hai. 
# Set me mutable hota hai. 

numbers = {1, 2, 3, 4}
# Agar duplicate values:
numbers = {1, 2, 2, 3, 3, 4}

print(set(numbers))  # yeh set ko print karta hai. 
# Python set: {1, 2, 3, 4}


#  Why Sets Are Useful in Data Science?  // Suppose dataset:
cities = [ "Hyderabad","Islamabad", "Karachi", "Lahore", "Hyderabad", "Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar", "Islamabad"]

# Convert the list to a set to remove duplicates
unique_cities = set(cities)  # Duplicates remove ho gaye.
print(unique_cities)

# Set Operations:

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

# Union
union = set(a) | set(b)
print("Union:", union)

# Intersection
intersection = set(a) & set(b)
print("Intersection:", intersection)

# Difference
difference = set(a) - set(b)
print("Difference:", difference)

# Symmetric Difference
symmetric_difference = set(a) ^ set(b)
print("Symmetric Difference:", symmetric_difference)






