#!/usr/bin/env python3

"""
Python Regular Expressions (RegEx) Crash Course
-------------------------------------------
Demonstrates various operations with regular expressions using the re module.
"""

import re

# 1. Basic Pattern Matching
print("1. Basic Pattern Matching")
print("-" * 35)

text = "The rain in Spain falls mainly in the plain."

# Simple pattern matching
pattern = "rain"
match = re.search(pattern, text)
print(f"Finding '{pattern}':")
print(f"Match found at position: {match.start() if match else 'Not found'}")

# Case-insensitive matching
pattern = "SPAIN"
match = re.search(pattern, text, re.IGNORECASE)
print(f"\nFinding '{pattern}' (case-insensitive):")
print(f"Match found at position: {match.start() if match else 'Not found'}")

print("\n")

# 2. Pattern Metacharacters
print("2. Pattern Metacharacters")
print("-" * 35)

# Different pattern examples
patterns = {
    "^The": "Starts with 'The'",
    "plain.$": "Ends with 'plain.'",
    "^The.*plain.$": "Starts with 'The' and ends with 'plain.'",
    "rain|falls": "Contains 'rain' or 'falls'",
    "[Tt]he": "Contains 'The' or 'the'",
    "in[gs]": "Contains 'ing' or 'ins'"
}

print("Pattern matching examples:")
for pattern, description in patterns.items():
    match = re.search(pattern, text)
    print(f"\nPattern '{pattern}' ({description}):")
    print(f"Match found: {bool(match)}")
    if match:
        print(f"Matched text: '{match.group()}'")

print("\n")

# 3. Quantifiers and Special Sequences
print("3. Quantifiers and Special Sequences")
print("-" * 35)

# Test text for various patterns
test_text = """
Phone: 123-456-7890
Email: user@example.com
Date: 2024-03-15
Time: 14:30:45
IP: 192.168.1.1
"""

patterns = {
    r"\d{3}-\d{3}-\d{4}": "Phone number format",
    r"\w+@\w+\.\w+": "Email format",
    r"\d{4}-\d{2}-\d{2}": "Date format",
    r"\d{2}:\d{2}:\d{2}": "Time format",
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}": "IP address format"
}

print("Pattern matching with quantifiers:")
for pattern, description in patterns.items():
    match = re.search(pattern, test_text)
    print(f"\nPattern '{pattern}' ({description}):")
    print(f"Match found: {match.group() if match else 'Not found'}")

print("\n")

# 4. findall() and finditer()
print("4. findall() and finditer()")
print("-" * 35)

text = "The price is $23.45, and the discount is $5.67"

# Find all price values
pattern = r'\$\d+\.\d{2}'
matches = re.findall(pattern, text)
print(f"All prices found: {matches}")

# Using finditer() for more detailed match information
print("\nDetailed price information:")
for match in re.finditer(pattern, text):
    print(f"Price '{match.group()}' found at position {match.start()}-{match.end()}")

print("\n")

# 5. Split and Replace Operations
print("5. Split and Replace Operations")
print("-" * 35)

# Split text
text = "Python;Java,C++;Ruby,JavaScript"
print("Original text:", text)

# Split on multiple delimiters
split_text = re.split(r'[;,]', text)
print(f"Split text: {split_text}")

# Replace using sub()
text = "I love cats, but cats can be annoying when cats are hungry"
replaced_text = re.sub(r'cats', 'dogs', text)
print(f"\nOriginal text: {text}")
print(f"Replaced text: {replaced_text}")

# Replace with count
replaced_text = re.sub(r'cats', 'dogs', text, count=2)
print(f"Replaced text (first 2 only): {replaced_text}")

print("\n")

# 6. Groups and Named Groups
print("6. Groups and Named Groups")
print("-" * 35)

# Parsing with groups
text = "John Doe, age 30, john.doe@example.com"
pattern = r"(\w+ \w+), age (\d+), (\S+@\S+)"

match = re.search(pattern, text)
if match:
    print("Groups found:")
    print(f"Full name: {match.group(1)}")
    print(f"Age: {match.group(2)}")
    print(f"Email: {match.group(3)}")

# Named groups
pattern = r"(?P<name>\w+ \w+), age (?P<age>\d+), (?P<email>\S+@\S+)"
match = re.search(pattern, text)
if match:
    print("\nNamed groups:")
    print(f"Name: {match.group('name')}")
    print(f"Age: {match.group('age')}")
    print(f"Email: {match.group('email')}")

print("\n")

# 7. Practical Examples
print("7. Practical Examples")
print("-" * 35)

def validate_email(email):
    """Validate email address format"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_password(password):
    """
    Validate password strength:
    - At least 8 characters
    - Contains uppercase and lowercase
    - Contains numbers
    - Contains special characters
    """
    patterns = {
        r'.{8,}': "at least 8 characters",
        r'[A-Z]': "uppercase letter",
        r'[a-z]': "lowercase letter",
        r'\d': "digit",
        r'[!@#$%^&*(),.?":{}|<>]': "special character"
    }
    
    results = []
    for pattern, description in patterns.items():
        if not re.search(pattern, password):
            results.append(f"Missing {description}")
    
    return results

# Test email validation
emails = [
    "user@example.com",
    "invalid.email@com",
    "no@dots",
    "multiple@dots.are.valid.com"
]

print("Email validation:")
for email in emails:
    print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")

# Test password validation
print("\nPassword validation:")
passwords = [
    "weak",
    "Stronger123",
    "SuperStrong123!",
    "noUPPERCASE123!"
]

for password in passwords:
    issues = validate_password(password)
    if issues:
        print(f"'{password}' is invalid:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print(f"'{password}' is valid")
