# Crash Course: Python String Formatting
# Learn how to format strings using f-strings (Python 3.6+) and the older format() method.

# ----------------------------------
# F-Strings: The Modern Way (Python 3.6+)
# ----------------------------------
# F-strings are the preferred method for string formatting: fast, readable, and concise.
# Add 'f' before a string literal to create an f-string.

# Basic f-string
txt = f"The price is 49 dollars"
print(txt)  # Output: The price is 49 dollars

# ----------------------------------
# Placeholders and Variables
# ----------------------------------
# Use {} as placeholders to insert variables, values, or expressions.

price = 59
txt = f"The price is {price} dollars"
print(txt)  # Output: The price is 59 dollars

# ----------------------------------
# Modifiers: Formatting Values
# ----------------------------------
# Add a colon (:) and a format specifier to control how values are displayed.
# Example: .2f for fixed-point number with 2 decimals.

txt = f"The price is {price:.2f} dollars"
print(txt)  # Output: The price is 59.00 dollars

# Direct value formatting (no variable needed)
txt = f"The price is {95:.2f} dollars"
print(txt)  # Output: The price is 95.00 dollars

# Thousand separator (comma)
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)  # Output: The price is 59,000 dollars

# ----------------------------------
# Operations in F-Strings
# ----------------------------------
# Perform calculations or logic directly inside {}.

# Math operation
txt = f"The price is {20 * 59} dollars"
print(txt)  # Output: The price is 1180 dollars

# Math with variables
price = 59
tax = 0.25
txt = f"The price with tax is {price + (price * tax):.2f} dollars"
print(txt)  # Output: The price with tax is 73.75 dollars

# Conditional logic (ternary operator)
price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)  # Output: It is very Cheap

# ----------------------------------
# Functions in F-Strings
# ----------------------------------
# Call built-in or custom functions inside {}.

# Built-in string method
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)  # Output: I love APPLES

# Custom function
def feet_to_meters(feet):
    return feet * 0.3048  # Convert feet to meters

txt = f"The plane flies at {feet_to_meters(30000):.1f} meters"
print(txt)  # Output: The plane flies at 9144.0 meters

# ----------------------------------
# Common Formatting Types
# ----------------------------------
# Use these modifiers after : in placeholders for specific formats:
# :.2f  - Fixed-point, 2 decimals (e.g., 59.00)
# :,    - Thousand separator (e.g., 1,000)
# :_    - Thousand separator with underscore (e.g., 1_000)
# :b    - Binary format (e.g., 1010 for 10)
# :x    - Hex format, lowercase (e.g., a for 10)
# :X    - Hex format, uppercase (e.g., A for 10)
# :%    - Percentage (e.g., 0.5 becomes 50%)
# :>10  - Right-align in 10 spaces
# :<10  - Left-align in 10 spaces
# :^10  - Center-align in 10 spaces

# Example: Multiple modifiers
value = 42
txt = f"Binary: {value:b}, Hex: {value:x}, Right-aligned: {value:>10}"
print(txt)  # Output: Binary: 101010, Hex: 2a, Right-aligned:         42

# ----------------------------------
# Legacy: String format() Method
# ----------------------------------
# Before f-strings, format() was used. It's slower but still works.
# Use {} as placeholders and pass values to format().

price = 49
txt = "The price is {} dollars"
print(txt.format(price))  # Output: The price is 49 dollars

# Specify formatting
txt = "The price is {:.2f} dollars"
print(txt.format(price))  # Output: The price is 49.00 dollars

# Multiple values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))  # Output: I want 3 pieces of item 567 for 49.00 dollars

# Index numbers for explicit ordering
myorder = "I want {0} pieces of item {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))  # Output: I want 3 pieces of item 567 for 49.00 dollars

# Reusing values with index
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))  # Output: His name is John. John is 36 years old.

# Named indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))  # Output: I have a Ford, it is a Mustang.

# ----------------------------------
# Quick Tips
# ----------------------------------
# - Use f-strings for new code: they're faster and clearer.
# - Use format() only for compatibility with Python < 3.6.
# - Modifiers like .2f, :, are the same in both methods.
# - F-strings support any Python expression in {}, but keep them readable!