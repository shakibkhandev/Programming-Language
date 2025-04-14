#!/usr/bin/env python3

"""
Python Error Handling Crash Course
--------------------------------
Demonstrates various error handling techniques using try-except blocks.
"""

# 1. Basic Exception Handling
print("1. Basic Exception Handling")
print("-" * 35)

# Simple try-except
print("Simple try-except example:")
try:
    # Trying to access undefined variable
    print(undefined_variable)
except:
    print("An error occurred - variable not defined")

# Specific exception handling
print("\nHandling specific exceptions:")
try:
    number = int("abc")  # This will raise ValueError
except ValueError:
    print("ValueError: Could not convert string to integer")
except TypeError:
    print("TypeError: Invalid type for conversion")

print("\n")

# 2. Multiple Exception Handling
print("2. Multiple Exception Handling")
print("-" * 35)

def divide_numbers(a, b):
    """Function to demonstrate multiple exception handling"""
    try:
        result = float(a) / float(b)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero!"
    except ValueError:
        return "Error: Invalid numbers!"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Test cases for division
test_cases = [
    (10, 2),        # Normal division
    (10, 0),        # Division by zero
    ('a', 2),       # Invalid number
    (10.5, 2.0),    # Float division
]

print("Testing division with different inputs:")
for a, b in test_cases:
    print(f"{a} / {b} = {divide_numbers(a, b)}")

print("\n")

# 3. try-except-else-finally
print("3. try-except-else-finally")
print("-" * 35)

def process_file(filename):
    """Demonstrate file handling with try-except-else-finally"""
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    else:
        try:
            content = file.read()
            print(f"File contents: {content[:50]}...")  # Show first 50 chars
        except Exception as e:
            print(f"Error reading file: {str(e)}")
        finally:
            file.close()
            print("File closed successfully")

# Test with existing and non-existing files
print("Testing file handling:")
process_file("nonexistent.txt")
try:
    # Create a test file
    with open("test.txt", "w") as f:
        f.write("This is a test file content")
    process_file("test.txt")
finally:
    # Clean up - remove test file
    import os
    if os.path.exists("test.txt"):
        os.remove("test.txt")

print("\n")

# 4. Custom Exceptions
print("4. Custom Exceptions")
print("-" * 35)

class AgeError(Exception):
    """Custom exception for age validation"""
    pass

class NameTooShortError(Exception):
    """Custom exception for name validation"""
    pass

def validate_person(name, age):
    """
    Validate person data with custom exceptions
    """
    if len(name) < 2:
        raise NameTooShortError("Name must be at least 2 characters long")
    
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    
    if age < 0 or age > 150:
        raise AgeError("Age must be between 0 and 150")
    
    return f"Valid person: {name}, {age} years old"

# Test person validation
test_cases = [
    ("John", 25),       # Valid
    ("A", 30),          # Name too short
    ("Mary", -5),       # Invalid age
    ("Bob", "twenty"),  # Invalid age type
]

print("Testing person validation:")
for name, age in test_cases:
    try:
        result = validate_person(name, age)
        print(f"Success: {result}")
    except (NameTooShortError, AgeError, TypeError) as e:
        print(f"Error: {str(e)}")

print("\n")

# 5. Context Managers (with statement)
print("5. Context Managers")
print("-" * 35)

class DatabaseConnection:
    """Simulate a database connection using context manager"""
    
    def __init__(self, host):
        self.host = host
        self.connected = False
    
    def __enter__(self):
        print(f"Connecting to database at {self.host}...")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection...")
        self.connected = False
        if exc_type is not None:
            print(f"An error occurred: {exc_val}")
            return False  # Re-raise the exception
    
    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected to database")
        print(f"Executing query: {sql}")

# Test database connection with context manager
print("Testing database connection:")
try:
    with DatabaseConnection("localhost:5432") as db:
        db.query("SELECT * FROM users")
        # Simulate an error
        raise ValueError("Simulated database error")
except ValueError as e:
    print(f"Caught error: {e}")

print("\n")

# 6. Practical Examples
print("6. Practical Examples")
print("-" * 35)

def safe_operation(func):
    """Decorator for safe operation execution"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {str(e)}")
            return None
    return wrapper

@safe_operation
def process_data(data):
    """Process data with potential errors"""
    result = []
    for item in data:
        # Perform risky operations
        number = float(item)
        result.append(number ** 2)
    return result

# Test data processing
print("Testing data processing:")
valid_data = ["1", "2", "3", "4"]
invalid_data = ["1", "a", "3", "b"]

print("Processing valid data:")
print(process_data(valid_data))

print("\nProcessing invalid data:")
print(process_data(invalid_data))

# 7. Exception Chaining
print("\n7. Exception Chaining")
print("-" * 35)

def outer_function():
    try:
        inner_function()
    except Exception as e:
        raise RuntimeError("Error in outer function") from e

def inner_function():
    raise ValueError("Error in inner function")

print("Testing exception chaining:")
try:
    outer_function()
except RuntimeError as e:
    print(f"Caught error: {e}")
    if e.__cause__:
        print(f"Caused by: {e.__cause__}")
