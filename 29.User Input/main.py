#!/usr/bin/env python3

"""
Python User Input Crash Course
----------------------------
Demonstrates various ways to handle user input in Python.
"""

# 1. Basic Input Examples
print("1. Basic Input Examples")
print("-" * 35)

# Simple string input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Numeric input (with type conversion)
try:
    age = int(input("Enter your age: "))
    print(f"In 5 years, you will be {age + 5} years old")
except ValueError:
    print("Please enter a valid number for age")

print("\n")

# 2. Input Validation
print("2. Input Validation")
print("-" * 35)

def get_valid_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")

def get_valid_choice(prompt, valid_options):
    """Get a valid choice from a list of options"""
    while True:
        choice = input(prompt).lower()
        if choice in valid_options:
            return choice
        print(f"Please enter one of: {', '.join(valid_options)}")

# Example usage of input validation
price = get_valid_number("Enter the price: $")
print(f"Price entered: ${price:.2f}")

# Choice validation
valid_options = ['yes', 'no']
response = get_valid_choice("Would you like to continue? (yes/no): ", valid_options)
print(f"You chose: {response}")

print("\n")

# 3. Interactive Calculator
print("3. Interactive Calculator")
print("-" * 35)

def calculator():
    """Simple interactive calculator"""
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    
    print("Simple Calculator")
    print("Available operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+,-,*,/): ")
        
        if op in operations:
            result = operations[op](num1, num2)
            print(f"Result: {num1} {op} {num2} = {result}")
        else:
            print("Invalid operation")
    except ValueError:
        print("Please enter valid numbers")

calculator()

print("\n")

# 4. Multi-line Input
print("4. Multi-line Input")
print("-" * 35)

def get_multiline_input():
    """Get multiple lines of input until empty line is entered"""
    print("Enter multiple lines (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return lines

# Get and display multi-line input
notes = get_multiline_input()
print("\nYour notes:")
for i, note in enumerate(notes, 1):
    print(f"{i}. {note}")

print("\n")

# 5. Password Input
print("5. Password Input")
print("-" * 35)

import getpass  # For secure password input

def login_system():
    """Simulate a simple login system"""
    username = input("Username: ")
    # getpass hides the input (works in terminal/command prompt)
    try:
        password = getpass.getpass("Password: ")
    except Exception:
        # Fallback to regular input if getpass fails
        password = input("Password: ")
    
    # Simple validation (in real systems, use proper authentication)
    if username == "admin" and password == "password123":
        print("Login successful!")
    else:
        print("Invalid credentials")

login_system()

print("\n")

# 6. Interactive Menu System
print("6. Interactive Menu System")
print("-" * 35)

def display_menu():
    """Display the main menu"""
    print("\nMenu Options:")
    print("1. View profile")
    print("2. Edit settings")
    print("3. Help")
    print("4. Exit")

def handle_menu():
    """Handle menu selections"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("Viewing profile...")
        elif choice == '2':
            print("Editing settings...")
        elif choice == '3':
            print("Displaying help...")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

handle_menu()

print("\n")

# 7. Form Input
print("7. Form Input")
print("-" * 35)

def get_form_input():
    """Simulate a form input system"""
    form_data = {}
    
    # Required fields
    required_fields = ['name', 'email', 'age']
    
    for field in required_fields:
        while True:
            value = input(f"Enter your {field}: ")
            if value.strip():  # Check if input is not empty
                # Additional validation for specific fields
                if field == 'age':
                    try:
                        value = int(value)
                        if value < 0 or value > 150:
                            print("Please enter a valid age (0-150)")
                            continue
                    except ValueError:
                        print("Please enter a valid number for age")
                        continue
                elif field == 'email':
                    if '@' not in value or '.' not in value:
                        print("Please enter a valid email address")
                        continue
                
                form_data[field] = value
                break
            else:
                print(f"{field} is required")
    
    # Optional fields
    form_data['comments'] = input("Any comments (optional): ")
    
    return form_data

print("Please fill out the form:")
form_data = get_form_input()

print("\nForm Summary:")
for field, value in form_data.items():
    print(f"{field.capitalize()}: {value}")
