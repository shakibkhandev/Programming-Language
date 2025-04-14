# Python Tuples Tutorial
# Tuples are ordered, immutable collections that can store multiple items

# 1. Creating a Tuple
print("\n1. Creating Tuples:")
# Simple tuple with strings
fruits_tuple = ("apple", "banana", "cherry")
print("Basic tuple:", fruits_tuple)

# Tuple with one item (note the comma)
single_tuple = ("apple",)  # This is a tuple
print("Single item tuple:", single_tuple)
not_tuple = ("apple")  # This is a string, not a tuple
print("Not a tuple:", type(not_tuple))

# Tuple with different data types
mixed_tuple = ("hello", 42, True, 3.14)
print("Mixed data types tuple:", mixed_tuple)

# 2. Accessing Tuple Items
print("\n2. Accessing Tuple Items:")
print("First item:", fruits_tuple[0])  # Positive indexing
print("Last item:", fruits_tuple[-1])  # Negative indexing

# Slicing tuples
numbers = (0, 1, 2, 3, 4, 5)
print("Slice (1:4):", numbers[1:4])  # Items from index 1 to 3
print("Slice (:3):", numbers[:3])    # Items from start to index 2
print("Slice (2:):", numbers[2:])    # Items from index 2 to end

# 3. Tuple Operations
print("\n3. Tuple Operations:")
# Checking if item exists
print("Is 'apple' in fruits_tuple?", "apple" in fruits_tuple)

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2
print("Concatenated tuples:", concatenated)

# Tuple repetition
repeated = tuple1 * 2
print("Repeated tuple:", repeated)

# 4. Tuple Methods
print("\n4. Tuple Methods:")
sample_tuple = (1, 2, 2, 3, 2, 4)
print("Count of 2:", sample_tuple.count(2))  # Counts occurrences of 2
print("Index of 3:", sample_tuple.index(3))  # Finds first occurrence of 3

# 5. Tuple Unpacking
print("\n5. Tuple Unpacking:")
# Basic unpacking
x, y, z = fruits_tuple
print(f"Unpacked values: x={x}, y={y}, z={z}")

# Extended unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"Extended unpacking: first={first}, middle={middle}, last={last}")

# 6. Converting Tuple to List (for modification)
print("\n6. Tuple Modification (via list conversion):")
temp_list = list(fruits_tuple)  # Convert to list
temp_list[1] = "kiwi"          # Modify the list
modified_tuple = tuple(temp_list)  # Convert back to tuple
print("Modified tuple:", modified_tuple)

# 7. Tuple Comparison
print("\n7. Tuple Comparison:")
tuple_1 = (1, 2, 3)
tuple_2 = (1, 2, 3)
tuple_3 = (1, 2, 4)
print("tuple_1 == tuple_2:", tuple_1 == tuple_2)  # True
print("tuple_1 < tuple_3:", tuple_1 < tuple_3)    # True (compares items sequentially)

# 8. Nested Tuples
print("\n8. Nested Tuples:")
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)
print("Accessing nested element:", nested_tuple[0][1])  # Accessing 2

# 9. Tuple vs List Performance
print("\n9. Tuple Benefits:")
# Tuples are more memory efficient than lists
# They are immutable, making them safer for data that shouldn't change
# They can be used as dictionary keys (unlike lists)
