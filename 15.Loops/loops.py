"""
Python Loops - A Comprehensive Guide
-----------------------------------
This tutorial covers both while and for loops in Python with detailed examples.
"""

# ----------------------
# While Loops
# ----------------------
print("\n=== While Loops ===")

# Basic while loop example
print("\n1. Basic while loop:")
i = 1
while i < 6:
    print(i)
    i += 1  # Important: Always remember to increment the counter to avoid infinite loops

# While loop with break statement
print("\n2. While loop with break:")
i = 1
while i < 6:
    if i == 3:
        break  # Exit the loop when i equals 3
    print(i)
    i += 1

# While loop with continue statement
print("\n3. While loop with continue:")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # Skip the rest of the loop body when i equals 3
    print(i)

# While loop with else statement
print("\n4. While loop with else:")
i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("Loop completed successfully!")  # Executes when the while condition becomes False

# ----------------------
# For Loops
# ----------------------
print("\n=== For Loops ===")

# Basic for loop with list
print("\n1. For loop with list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# For loop with string
print("\n2. For loop with string:")
for char in "Python":
    print(char)  # Prints each character in the string

# For loop with range
print("\n3. For loop with range:")
# range(stop) - starts from 0 by default
for i in range(3):
    print(f"range(3): {i}")

# range(start, stop)
for i in range(2, 5):
    print(f"range(2, 5): {i}")

# range(start, stop, step)
for i in range(0, 10, 2):
    print(f"range(0, 10, 2): {i}")  # Prints even numbers from 0 to 8

# For loop with break
print("\n4. For loop with break:")
for fruit in fruits:
    if fruit == "banana":
        break  # Exit the loop when banana is found
    print(fruit)

# For loop with continue
print("\n5. For loop with continue:")
for fruit in fruits:
    if fruit == "banana":
        continue  # Skip banana and continue with next iteration
    print(fruit)

# Nested loops
print("\n6. Nested loops:")
colors = ["red", "blue"]
items = ["car", "bike"]
for color in colors:
    for item in items:
        print(f"{color} {item}")

# For loop with else
print("\n7. For loop with else:")
for i in range(3):
    print(i)
else:
    print("Loop finished successfully!")  # Executes when loop completes normally

# Example of loop with pass
print("\n8. For loop with pass:")
for x in range(3):
    pass  # Pass is used as a placeholder when no action is needed

"""
Key Points to Remember:
1. while loops repeat as long as a condition is True
2. for loops iterate over a sequence (list, tuple, string, etc.)
3. break exits the loop completely
4. continue skips to the next iteration
5. else in loops executes when loop completes normally (not through break)
6. range() is commonly used to generate number sequences
7. pass is used as a placeholder when no action is needed
"""
