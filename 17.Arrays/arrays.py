# Python Arrays/Lists Crash Course

# Note: Python doesn't have built-in arrays, but lists can be used as arrays
# Lists are more flexible than traditional arrays as they can store different data types

# 1. Creating a List
cars = ["Ford", "Volvo", "BMW"]  # Creating a list of strings
numbers = [1, 2, 3, 4, 5]  # Creating a list of integers
mixed = [1, "Hello", 3.14, True]  # Lists can store different data types

# 2. Accessing Elements
print("\n--- Accessing Elements ---")
print(f"First car: {cars[0]}")  # Accessing first element (index 0)
print(f"Last car: {cars[-1]}")  # Negative indexing to access from end
print(f"Subset of numbers: {numbers[1:3]}")  # Slicing (from index 1 to 2)

# 3. Modifying Elements
print("\n--- Modifying Elements ---")
cars[0] = "Toyota"  # Changing the first element
print(f"Modified cars list: {cars}")

# 4. List Length
print("\n--- List Length ---")
print(f"Number of cars: {len(cars)}")  # len() returns the number of elements

# 5. Looping Through Lists
print("\n--- Looping Through List ---")
print("All cars:")
for car in cars:  # Using for loop to iterate
    print(car)

# 6. List Methods
print("\n--- List Methods ---")

# Adding elements
cars.append("Honda")  # Adds element at the end
print(f"After append: {cars}")

cars.insert(1, "Nissan")  # Adds element at specific position
print(f"After insert: {cars}")

# Removing elements
removed_car = cars.pop(1)  # Removes element at index 1
print(f"Removed car: {removed_car}")
print(f"After pop: {cars}")

cars.remove("BMW")  # Removes first occurrence of "BMW"
print(f"After remove: {cars}")

# Other useful methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"\nOriginal numbers: {numbers}")

numbers.sort()  # Sorts the list in ascending order
print(f"Sorted numbers: {numbers}")

numbers.reverse()  # Reverses the list
print(f"Reversed numbers: {numbers}")

# 7. List Operations
print("\n--- List Operations ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # Concatenating lists
print(f"Combined lists: {combined}")

multiplied = list1 * 2  # Repeating lists
print(f"Multiplied list: {multiplied}")

# 8. List Comprehension
print("\n--- List Comprehension ---")
# Creating a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(f"Squares using list comprehension: {squares}")

# 9. Checking if Element Exists
print("\n--- Element Existence ---")
print(f"Is 'Toyota' in cars? {'Toyota' in cars}")
print(f"Is 'Porsche' in cars? {'Porsche' in cars}")

# 10. Clearing a List
cars.clear()  # Removes all elements
print(f"\nAfter clearing cars list: {cars}")
