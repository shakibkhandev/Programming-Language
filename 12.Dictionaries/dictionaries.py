# Python Dictionaries Crash Course

# 1. Creating a Dictionary
# Dictionaries store key-value pairs using curly brackets {}
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Alternative way to create a dictionary using dict() constructor
person = dict(name="John", age=36, country="Norway")

# 2. Accessing Dictionary Items
print("\n--- Accessing Dictionary Items ---")
print(f"Car brand (using []): {car_dict['brand']}")  # Using square brackets
print(f"Car brand (using get()): {car_dict.get('brand')}")  # Using get() method

# 3. Dictionary Properties
print("\n--- Dictionary Properties ---")
print(f"Dictionary length: {len(car_dict)}")  # Number of key-value pairs
print(f"Dictionary type: {type(car_dict)}")   # Type of the dictionary

# 4. Dictionary Methods
print("\n--- Dictionary Methods ---")
# Get all keys
keys = car_dict.keys()
print(f"Keys: {keys}")

# Get all values
values = car_dict.values()
print(f"Values: {values}")

# Get all items (key-value pairs)
items = car_dict.items()
print(f"Items: {items}")

# 5. Modifying Dictionaries
print("\n--- Modifying Dictionaries ---")
# Adding new items
car_dict["color"] = "red"  # Add new key-value pair
print(f"After adding color: {car_dict}")

# Updating existing items
car_dict["year"] = 2020  # Update existing value
print(f"After updating year: {car_dict}")

# Update using update() method
car_dict.update({"color": "blue", "price": 45000})
print(f"After update() method: {car_dict}")

# 6. Removing Items
print("\n--- Removing Items ---")
# Using pop() - removes specific key
removed_value = car_dict.pop("price")
print(f"Removed value: {removed_value}")
print(f"After pop(): {car_dict}")

# Using popitem() - removes last inserted item
last_item = car_dict.popitem()
print(f"Last removed item: {last_item}")
print(f"After popitem(): {car_dict}")

# 7. Checking Keys
print("\n--- Checking Keys ---")
print(f"Is 'model' in dictionary? {'model' in car_dict}")
print(f"Is 'price' in dictionary? {'price' in car_dict}")

# 8. Looping Through Dictionaries
print("\n--- Looping Through Dictionaries ---")
# Loop through keys
print("Keys:")
for key in car_dict:
    print(key)

# Loop through values
print("\nValues:")
for value in car_dict.values():
    print(value)

# Loop through both keys and values
print("\nKey-Value pairs:")
for key, value in car_dict.items():
    print(f"{key}: {value}")

# 9. Copying Dictionaries
print("\n--- Copying Dictionaries ---")
# Using copy() method
dict_copy1 = car_dict.copy()
# Using dict() function
dict_copy2 = dict(car_dict)

# 10. Nested Dictionaries
print("\n--- Nested Dictionaries ---")
family = {
    "child1": {
        "name": "Emil",
        "age": 12
    },
    "child2": {
        "name": "Tobias",
        "age": 9
    }
}

# Accessing nested dictionary items
print(f"First child's name: {family['child1']['name']}")

# Loop through nested dictionary
print("\nFamily details:")
for member, details in family.items():
    print(f"{member}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
