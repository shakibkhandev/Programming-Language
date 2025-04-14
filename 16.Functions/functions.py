# Python Functions Crash Course
# ========================

# 1. Basic Function Definition
# ---------------------------
def greet():
    """
    A simple function that prints a greeting.
    This is a docstring - used for documentation.
    """
    print("Hello from the function!")

# Calling the function
greet()  # Output: Hello from the function!


# 2. Functions with Parameters
# --------------------------
def greet_person(name):    # 'name' is a parameter
    """
    A function that greets a specific person.
    Args:
        name (str): The name of the person to greet
    """
    print(f"Hello, {name}!")

# Calling function with argument
greet_person("Alice")    # 'Alice' is an argument


# 3. Multiple Parameters
# --------------------
def calculate_sum(a, b):
    """
    Calculate the sum of two numbers.
    Args:
        a (number): First number
        b (number): Second number
    Returns:
        number: Sum of a and b
    """
    return a + b

result = calculate_sum(5, 3)
print(f"Sum is: {result}")  # Output: Sum is: 8


# 4. Default Parameter Values
# -------------------------
def greet_with_title(name, title="Mr."):    # title has a default value
    """
    Greet person with their title.
    Args:
        name (str): Person's name
        title (str, optional): Person's title. Defaults to "Mr."
    """
    print(f"Hello, {title} {name}")

greet_with_title("Smith")          # Uses default title
greet_with_title("Johnson", "Dr.") # Overrides default title


# 5. *args - Variable Number of Arguments
# ------------------------------------
def sum_all(*numbers):
    """
    Sum any number of arguments.
    Args:
        *numbers: Variable number of numeric arguments
    Returns:
        number: Sum of all arguments
    """
    return sum(numbers)

print(sum_all(1, 2, 3))       # Output: 6
print(sum_all(1, 2, 3, 4, 5)) # Output: 15


# 6. **kwargs - Keyword Arguments
# ----------------------------
def print_info(**kwargs):
    """
    Print all keyword arguments.
    Args:
        **kwargs: Variable number of keyword arguments
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")


# 7. Combined Positional, *args, and **kwargs
# ----------------------------------------
def mixed_arguments(a, b, *args, **kwargs):
    """
    Demonstrate different types of arguments.
    Args:
        a: First required argument
        b: Second required argument
        *args: Variable positional arguments
        **kwargs: Variable keyword arguments
    """
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

mixed_arguments(1, 2, 3, 4, 5, x=10, y=20)


# 8. Function with Type Hints (Python 3.5+)
# --------------------------------------
def calculate_area(length: float, width: float) -> float:
    """
    Calculate area of a rectangle using type hints.
    Args:
        length (float): Length of rectangle
        width (float): Width of rectangle
    Returns:
        float: Area of rectangle
    """
    return length * width

area = calculate_area(5.0, 3.0)
print(f"Area: {area}")


# 9. Recursion Example
# ------------------
def factorial(n: int) -> int:
    """
    Calculate factorial using recursion.
    Args:
        n (int): Number to calculate factorial for
    Returns:
        int: Factorial of n
    """
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(f"Factorial of 5: {factorial(5)}")  # Output: 120


# 10. Lambda Functions (Anonymous Functions)
# --------------------------------------
# Lambda functions are small anonymous functions that can have any number of arguments
# but can only have one expression. Syntax: lambda arguments : expression

# Basic lambda with one argument
add_ten = lambda a: a + 10
print(f"Add 10 to 5: {add_ten(5)}")  # Output: 15

# Lambda with multiple arguments
multiply = lambda a, b: a * b
print(f"3 x 4 = {multiply(3, 4)}")  # Output: 12

# Lambda with three arguments
sum_three = lambda a, b, c: a + b + c
print(f"Sum of 1, 2, 3: {sum_three(1, 2, 3)}")  # Output: 6

# Advanced Lambda Usage: Functions returning Lambda functions
def create_multiplier(n):
    """
    Create a function that multiplies its input by n.
    This demonstrates the power of lambda functions as return values.
    Args:
        n (number): The multiplier value
    Returns:
        function: A lambda function that multiplies its input by n
    """
    return lambda x: x * n

# Create specific multiplier functions
double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

# Test the multiplier functions
number = 10
print(f"Double {number}: {double(number)}")      # Output: 20
print(f"Triple {number}: {triple(number)}")      # Output: 30
print(f"Quadruple {number}: {quadruple(number)}") # Output: 40

# Lambda functions in built-in functions
numbers = [1, 2, 3, 4, 5, 6]

# Using lambda with filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # Output: [2, 4, 6]

# Using lambda with map() to square numbers
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")  # Output: [1, 4, 9, 16, 25, 36]

# Using lambda with sorted() for custom sorting
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_by_second = sorted(pairs, key=lambda x: x[1])
print(f"Sorted by second element: {sorted_by_second}")

# Lambda in list comprehension alternative
# Instead of lambda, you can often use list comprehension
# Lambda version
squared_lambda = list(map(lambda x: x**2, numbers))
# List comprehension version
squared_comprehension = [x**2 for x in numbers]
print(f"Lambda vs Comprehension (same result):")
print(f"Lambda: {squared_lambda}")
print(f"Comprehension: {squared_comprehension}")

# Note: While lambda functions are convenient for short operations,
# it's recommended to use regular functions (def) for complex operations
# or when the function needs to be reused multiple times.
# Lambda functions are best used when you need a simple function for a short period of time.
