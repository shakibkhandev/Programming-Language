#!/usr/bin/env python3

"""
Python JSON Operations Crash Course
--------------------------------
Demonstrates working with JSON data in Python using the json module.
"""

import json
from datetime import datetime
import os

# 1. Basic JSON Operations
print("1. Basic JSON Operations")
print("-" * 35)

# Simple Python dictionary
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "married": True,
    "hobbies": ["reading", "music", "hiking"],
    "children": None
}

# Converting Python to JSON (Serialization)
json_string = json.dumps(person)
print("Python dict to JSON string:")
print(json_string)

# Converting JSON to Python (Deserialization)
python_dict = json.loads(json_string)
print("\nJSON string back to Python dict:")
print(f"Name: {python_dict['name']}")
print(f"First hobby: {python_dict['hobbies'][0]}")

print("\n")

# 2. Formatting JSON Output
print("2. Formatting JSON Output")
print("-" * 35)

# Pretty printing with indentation
print("Pretty printed JSON (indent=4):")
print(json.dumps(person, indent=4))

# Custom separators
print("\nCustom separators:")
print(json.dumps(person, indent=4, separators=(". ", " = ")))

# Sorting keys
print("\nSorted keys:")
print(json.dumps(person, indent=4, sort_keys=True))

print("\n")

# 3. Complex Data Types
print("3. Complex Data Types")
print("-" * 35)

# Complex nested structure
complex_data = {
    "website": "example.com",
    "created_at": str(datetime.now()),  # Convert datetime to string
    "stats": {
        "visitors": 100000,
        "pages": 50,
        "bounce_rate": 0.45
    },
    "products": [
        {
            "id": 1,
            "name": "Product A",
            "price": 29.99,
            "in_stock": True,
            "tags": ["electronics", "gadgets"]
        },
        {
            "id": 2,
            "name": "Product B",
            "price": 49.99,
            "in_stock": False,
            "tags": ["accessories", "lifestyle"]
        }
    ]
}

# Pretty print complex data
print("Complex nested JSON:")
print(json.dumps(complex_data, indent=4))

print("\n")

# 4. Working with JSON Files
print("4. Working with JSON Files")
print("-" * 35)

# Writing JSON to a file
filename = "data.json"
with open(filename, 'w') as f:
    json.dump(complex_data, f, indent=4)
print(f"Data written to {filename}")

# Reading JSON from a file
with open(filename, 'r') as f:
    loaded_data = json.load(f)
print("\nData loaded from file:")
print(f"Website: {loaded_data['website']}")
print(f"First product: {loaded_data['products'][0]['name']}")

print("\n")

# 5. Error Handling
print("5. Error Handling")
print("-" * 35)

# Function to safely parse JSON
def parse_json(json_str):
    """Safely parse JSON string with error handling"""
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        return f"Error parsing JSON: {e}"

# Test with valid and invalid JSON
valid_json = '{"name": "John", "age": 30}'
invalid_json = '{"name": "John", age: 30}'  # Missing quotes around age

print("Parsing valid JSON:")
print(parse_json(valid_json))

print("\nParsing invalid JSON:")
print(parse_json(invalid_json))

print("\n")

# 6. Advanced JSON Operations
print("6. Advanced JSON Operations")
print("-" * 35)

# Custom encoding
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def point_encoder(obj):
    """Custom JSON encoder for Point class"""
    if isinstance(obj, Point):
        return {'x': obj.x, 'y': obj.y}
    raise TypeError(f'Object of type {type(obj)} is not JSON serializable')

# Data with custom object
data_with_custom_obj = {
    "name": "Graph",
    "point1": Point(10, 20),
    "point2": Point(30, 40)
}

print("JSON with custom encoder:")
print(json.dumps(data_with_custom_obj, default=point_encoder, indent=4))

# 7. JSON Schema Validation Example
print("\n7. JSON Schema Validation")
print("-" * 35)

# Define a simple schema
user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "email": {"type": "string"}
    },
    "required": ["name", "email"]
}

# Example validation function (basic)
def validate_json(data, schema):
    """Basic JSON validation against schema"""
    try:
        # Check required fields
        for field in schema.get("required", []):
            if field not in data:
                return False, f"Missing required field: {field}"
        
        # Check types
        for field, value in data.items():
            if field in schema["properties"]:
                expected_type = schema["properties"][field]["type"]
                if expected_type == "string" and not isinstance(value, str):
                    return False, f"Field {field} should be a string"
                elif expected_type == "number" and not isinstance(value, (int, float)):
                    return False, f"Field {field} should be a number"
        
        return True, "Validation successful"
    except Exception as e:
        return False, f"Validation error: {e}"

# Test data
valid_user = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com"
}

invalid_user = {
    "name": "John Doe",
    "age": "30"  # age should be a number
}

print("Validating valid user data:")
is_valid, message = validate_json(valid_user, user_schema)
print(f"Valid user: {is_valid}, {message}")

print("\nValidating invalid user data:")
is_valid, message = validate_json(invalid_user, user_schema)
print(f"Invalid user: {is_valid}, {message}")

# Clean up the created file
os.remove(filename)
print(f"\nCleaned up {filename}")
