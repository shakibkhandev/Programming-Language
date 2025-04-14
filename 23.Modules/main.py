#!/usr/bin/env python3

"""
Main Module
----------
Demonstrates different ways to import and use modules in Python.
"""

# 1. Import entire module
print("1. Importing entire module")
print("-" * 30)
import calculator

print(f"Calculator module version: {calculator.VERSION}")
print(f"2 + 3 = {calculator.add(2, 3)}")
print(f"10 - 4 = {calculator.subtract(10, 4)}")

# Create instance of ScientificCalculator from the module
sci_calc = calculator.ScientificCalculator()
print(f"2³ = {sci_calc.cube(2)}")

print("\n")

# 2. Import with alias
print("2. Import with alias")
print("-" * 30)
import utils as u

print(f"Pi value: {u.MATH_CONSTANTS['pi']}")
print(f"Is 7 even? {u.is_even(7)}")
print(f"Format Pi: {u.format_number(u.MATH_CONSTANTS['pi'], 4)}")

print("\n")

# 3. Import specific items from module
print("3. Import specific items")
print("-" * 30)
from calculator import multiply, divide

print(f"5 × 6 = {multiply(5, 6)}")
print(f"20 ÷ 4 = {divide(20, 4)}")

print("\n")

# 4. Import with different name
print("4. Import with different name")
print("-" * 30)
from utils import format_number as fmt, config as settings

print(f"Formatted number: {fmt(123.456789, 3)}")
print(f"Debug mode: {settings['debug']}")
print(f"Log level: {settings['log_level']}")

print("\n")

# 5. Import multiple items
print("5. Import multiple items")
print("-" * 30)
from utils import (
    MAX_RETRIES,
    DEFAULT_TIMEOUT,
    is_positive
)

print(f"Max retries: {MAX_RETRIES}")
print(f"Default timeout: {DEFAULT_TIMEOUT}")
print(f"Is 42 positive? {is_positive(42)}")

print("\n")

# 6. Using dir() function
print("6. Using dir() function")
print("-" * 30)
print("Contents of calculator module:")
print([item for item in dir(calculator) if not item.startswith("__")])

print("\nContents of utils module:")
print([item for item in dir(u) if not item.startswith("__")])

# 7. Error handling with modules
print("\n7. Error handling with modules")
print("-" * 30)
try:
    result = calculator.divide(10, 0)
except ValueError as e:
    print(f"Caught error: {e}")

# 8. Module documentation
print("\n8. Module documentation")
print("-" * 30)
print("Calculator module doc:")
print(calculator.__doc__)

print("\nUtils module doc:")
print(u.__doc__) 