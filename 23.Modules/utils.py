#!/usr/bin/env python3

"""
Utilities Module
--------------
A collection of utility functions and constants.
"""

# Module constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# Example dictionary in a module
config = {
    "debug": True,
    "log_level": "INFO",
    "max_connections": 100
}

def format_number(number, decimal_places=2):
    """Format a number to specified decimal places"""
    return f"{number:.{decimal_places}f}"

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def is_positive(number):
    """Check if a number is positive"""
    return number > 0

# List of useful mathematical constants
MATH_CONSTANTS = {
    "pi": 3.14159,
    "e": 2.71828,
    "golden_ratio": 1.61803
}

# This will only run if this file is run directly
if __name__ == "__main__":
    print("Testing utility functions:")
    print(f"Format number: {format_number(3.14159, 3)}")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Is -5 positive? {is_positive(-5)}")
    print(f"Pi value: {MATH_CONSTANTS['pi']}") 