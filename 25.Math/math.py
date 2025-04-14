#!/usr/bin/env python3

"""
Python Math Operations Crash Course
--------------------------------
Demonstrates built-in math functions and the math module capabilities.
"""

import math
import random  # For random number examples
import statistics  # For statistical operations

# 1. Built-in Math Functions
print("1. Built-in Math Functions")
print("-" * 35)

# Basic arithmetic operations
x, y = 10, 3
print("Basic Arithmetic:")
print(f"Addition: {x} + {y} = {x + y}")
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")
print(f"Floor Division: {x} // {y} = {x // y}")
print(f"Modulus: {x} % {y} = {x % y}")
print(f"Power: {x} ** {y} = {x ** y}")

# min() and max() functions
numbers = [5, 10, 25, 3, 8]
print("\nMin and Max:")
print(f"Numbers: {numbers}")
print(f"Minimum value: {min(numbers)}")
print(f"Maximum value: {max(numbers)}")

# abs() function for absolute value
print("\nAbsolute Values:")
print(f"abs(-7.25) = {abs(-7.25)}")
print(f"abs(3.14) = {abs(3.14)}")

# pow() function for power calculations
print("\nPower Function:")
print(f"pow(4, 3) = {pow(4, 3)}")  # Same as 4 ** 3
print(f"pow(2, -2) = {pow(2, -2)}")  # Negative exponents

print("\n")

# 2. Math Module Functions
print("2. Math Module Functions")
print("-" * 35)

# Square root and exponential functions
print("Square Root and Exponential:")
print(f"Square root of 64: {math.sqrt(64)}")
print(f"e^2: {math.exp(2)}")  # e raised to power 2
print(f"2^3: {math.pow(2, 3)}")  # Same as built-in pow()

# Trigonometric functions (input in radians)
print("\nTrigonometric Functions:")
angle = math.pi / 4  # 45 degrees
print(f"sin(π/4): {math.sin(angle):.4f}")
print(f"cos(π/4): {math.cos(angle):.4f}")
print(f"tan(π/4): {math.tan(angle):.4f}")

# Angle conversion
print("\nAngle Conversion:")
degrees = 45
radians = math.radians(degrees)
print(f"{degrees} degrees = {radians:.4f} radians")
print(f"{radians:.4f} radians = {math.degrees(radians)} degrees")

# Ceiling and floor functions
print("\nCeiling and Floor:")
x = 1.4
print(f"ceil({x}) = {math.ceil(x)}")
print(f"floor({x}) = {math.floor(x)}")

# Constants from math module
print("\nMath Constants:")
print(f"π (pi): {math.pi:.6f}")
print(f"e: {math.e:.6f}")
print(f"tau (2π): {math.tau:.6f}")
print(f"infinity: {math.inf}")
print(f"nan: {math.nan}")

print("\n")

# 3. Advanced Math Operations
print("3. Advanced Math Operations")
print("-" * 35)

# Logarithmic functions
print("Logarithmic Functions:")
x = 100
print(f"Natural log of {x}: {math.log(x):.4f}")
print(f"Base-10 log of {x}: {math.log10(x):.4f}")
print(f"Base-2 log of {x}: {math.log2(x):.4f}")

# Hyperbolic functions
print("\nHyperbolic Functions:")
x = 1
print(f"sinh({x}): {math.sinh(x):.4f}")
print(f"cosh({x}): {math.cosh(x):.4f}")
print(f"tanh({x}): {math.tanh(x):.4f}")

print("\n")

# 4. Practical Examples
print("4. Practical Examples")
print("-" * 35)

# Calculate area of a circle
def circle_area(radius):
    """Calculate the area of a circle given its radius"""
    return math.pi * radius ** 2

radius = 5
print(f"Area of circle with radius {radius}: {circle_area(radius):.2f}")

# Calculate hypotenuse of a right triangle
def hypotenuse(a, b):
    """Calculate the hypotenuse of a right triangle using Pythagorean theorem"""
    return math.sqrt(a**2 + b**2)

a, b = 3, 4
print(f"\nHypotenuse of right triangle with sides {a} and {b}: {hypotenuse(a, b)}")

# Statistical operations
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nStatistical Operations:")
print(f"Numbers: {numbers}")
print(f"Mean: {statistics.mean(numbers)}")
print(f"Median: {statistics.median(numbers)}")
print(f"Standard Deviation: {statistics.stdev(numbers):.4f}")

# Random number generation
print("\nRandom Numbers:")
print(f"Random float between 0 and 1: {random.random()}")
print(f"Random integer between 1 and 10: {random.randint(1, 10)}")
print(f"Random choice from list: {random.choice(numbers)}")

# 5. Error Handling in Math Operations
print("\n5. Error Handling in Math Operations")
print("-" * 35)

def safe_sqrt(x):
    """Safely calculate square root with error handling"""
    try:
        return math.sqrt(x)
    except ValueError as e:
        return f"Error: {e}"

# Test with different values
print("Safe Square Root Function:")
print(f"sqrt(16) = {safe_sqrt(16)}")
print(f"sqrt(-16) = {safe_sqrt(-16)}")

# Handling division by zero
def safe_divide(x, y):
    """Safely divide two numbers with error handling"""
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero"

print("\nSafe Division Function:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

# 6. Working with Complex Numbers
print("\n6. Complex Numbers")
print("-" * 35)

# Creating complex numbers
c1 = complex(2, 3)  # 2 + 3j
c2 = complex(1, -2)  # 1 - 2j

print("Complex Number Operations:")
print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"Addition: {c1 + c2}")
print(f"Multiplication: {c1 * c2}")
print(f"Magnitude of c1: {abs(c1):.4f}")
print(f"Real part of c1: {c1.real}")
print(f"Imaginary part of c1: {c1.imag}")
