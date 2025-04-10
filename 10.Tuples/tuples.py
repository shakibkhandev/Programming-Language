# Python Tuples Crash Course

# Tuples are ordered, immutable sequences of elements
# Unlike lists (which use square brackets []), tuples use parentheses ()
# Once created, tuples cannot be modified (immutable)

# 1. Creating tuples
empty_tuple = ()
single_element_tuple = (1,)  # Note the comma is necessary for single-element tuples
mixed_tuple = (1, "hello", 3.14, True)
nested_tuple = (1, (2, 3), (4, 5, 6))

# 2. Accessing tuple elements (using index)
coordinates = (10, 20, 30)
x = coordinates[0]  # Gets first element (10)
y = coordinates[1]  # Gets second element (20)
z = coordinates[2]  # Gets third element (30)

# 3. Negative indexing (counting from the end)
last_element = coordinates[-1]  # Gets the last element (30)
second_to_last = coordinates[-2]  # Gets the second to last element (20)

# 4. Tuple slicing (getting a range of elements)
numbers = (0, 1, 2, 3, 4, 5)
subset = numbers[2:4]  # Gets elements from index 2 to 3 (2, 3)
first_three = numbers[:3]  # Gets first three elements (0, 1, 2)
last_three = numbers[-3:]  # Gets last three elements (3, 4, 5)

# 5. Tuple operations
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2  # Results in (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 3  # Results in (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 6. Tuple methods
sample_tuple = (1, 2, 2, 3, 2, 4, 5)
count_2 = sample_tuple.count(2)  # Counts how many times 2 appears (3 times)
index_4 = sample_tuple.index(4)  # Finds the index of 4 (5th position, index 5)

# 7. Tuple unpacking
# A convenient way to assign multiple variables at once
point3D = (100, 200, 300)
x, y, z = point3D  # x = 100, y = 200, z = 300

# Extended unpacking with *
first, *middle, last = (1, 2, 3, 4, 5)  # first = 1, middle = [2, 3, 4], last = 5

# 8. Using tuples in practice
# Tuples are often used for returning multiple values from functions
def get_coordinates():
    return (3, 4)

point_x, point_y = get_coordinates()  # Tuple unpacking the returned values

# 9. Tuple comparison
# Tuples are compared element by element
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)
comparison = tuple_a < tuple_b  # True because 3 < 4 in the last position

# 10. Converting other sequences to tuples
list_to_tuple = tuple([1, 2, 3])  # Converts a list to a tuple
string_to_tuple = tuple("Python")  # Converts a string to a tuple of characters

# Demonstrating tuple immutability
try:
    coordinates[0] = 100  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)  # Will print: TypeError: 'tuple' object does not support item assignment

# 11. Advanced Tuple Operations

# Accessing nested tuples
nested = ((1, 2), (3, 4), (5, 6))
first_pair = nested[0]  # Gets (1, 2)
first_element = nested[0][0]  # Gets 1

# "Updating" tuples (creating new tuples)
original = (1, 2, 3)
# To "update" a tuple, we create a new one
updated = (original[0], 99, original[2])  # Changes second element to 99

# Advanced unpacking
# Nested unpacking
(a, b), (c, d) = ((1, 2), (3, 4))  # a=1, b=2, c=3, d=4

# Ignoring values with underscore
first, _, third = (1, 2, 3)  # Ignores second value

# 12. Looping through tuples
# Basic for loop
fruits = ('apple', 'banana', 'cherry')
print("\nLooping through tuple:")
for fruit in fruits:
    print(fruit)

# Loop with index
print("\nLooping with index:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 13. Joining tuples
# Using + operator
tuple3 = (7, 8, 9)
joined = tuple1 + tuple2 + tuple3

# Using tuple() constructor with unpacking
joined_alt = tuple([*tuple1, *tuple2, *tuple3])

# 14. Additional tuple methods and operations
# Length of tuple
tuple_length = len(fruits)  # Returns 3

# Check if element exists
has_apple = 'apple' in fruits  # Returns True
has_orange = 'orange' in fruits  # Returns False

# Maximum and minimum values (for numeric tuples)
numbers_tuple = (5, 2, 8, 1, 9)
max_value = max(numbers_tuple)  # Returns 9
min_value = min(numbers_tuple)  # Returns 1

# Sum of numeric tuple
sum_values = sum(numbers_tuple)  # Returns 25

# 15. Tuple as dictionary keys
# Tuples can be used as dictionary keys because they're immutable
coordinate_dict = {
    (0, 0): 'origin',
    (1, 0): 'right',
    (0, 1): 'up'
}

# Print some examples to see the results
if __name__ == "__main__":
    print("Basic tuple:", mixed_tuple)
    print("Nested tuple:", nested_tuple)
    print("Sliced tuple:", subset)
    print("Combined tuples:", combined)
    print("Tuple element count (2s):", count_2)
    print("Converted string to tuple:", string_to_tuple)
    print("\nAdvanced examples:")
    print("Nested access:", first_element)
    print("Updated tuple:", updated)
    print("Joined tuples:", joined)
    print("Tuple length:", tuple_length)
    print("Max value:", max_value)
    print("Min value:", min_value)
    print("Sum of values:", sum_values)
    print("Coordinate dictionary:", coordinate_dict)
