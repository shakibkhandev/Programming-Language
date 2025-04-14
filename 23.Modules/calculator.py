#!/usr/bin/env python3

"""
Calculator Module
---------------
A simple calculator module demonstrating module creation in Python.
"""

# Module level variables (can be accessed by importing module)
AUTHOR = "Python Developer"
VERSION = "1.0.0"

# Basic calculator operations
def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract y from x"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide x by y"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Example of a class in a module
class ScientificCalculator:
    """A more advanced calculator with additional operations"""
    
    def __init__(self):
        self.last_result = 0
    
    def square(self, x):
        """Calculate square of a number"""
        self.last_result = x ** 2
        return self.last_result
    
    def cube(self, x):
        """Calculate cube of a number"""
        self.last_result = x ** 3
        return self.last_result
    
    def power(self, x, y):
        """Calculate x raised to power y"""
        self.last_result = x ** y
        return self.last_result

# This will only run if this file is run directly (not when imported)
if __name__ == "__main__":
    print("Calculator module test:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"8 / 2 = {divide(8, 2)}")
    
    sci_calc = ScientificCalculator()
    print(f"2^3 = {sci_calc.power(2, 3)}") 