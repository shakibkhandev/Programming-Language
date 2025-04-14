#!/usr/bin/env python3

# Python Scope Crash Course
# -----------------------
# Scope determines the visibility and accessibility of variables in Python
# There are four types of scope:
# 1. Local Scope (variables inside a function)
# 2. Enclosing Scope (variables in outer function of nested functions)
# 3. Global Scope (variables defined at module level)
# 4. Built-in Scope (Python's built-in names)

# 1. Local Scope
print("1. Local Scope Examples")
print("-" * 30)

def demonstrate_local_scope():
    """Demonstrates local scope of variables"""
    # x is local to this function
    x = 100
    print(f"Local x inside function: {x}")

demonstrate_local_scope()
# This would raise an error because x is not accessible here
# print(x)  # NameError: name 'x' is not defined

print("\n")

# 2. Enclosing (Nonlocal) Scope
print("2. Enclosing Scope Examples")
print("-" * 30)

def outer_function():
    """Demonstrates enclosing scope with nested functions"""
    x = "outer value"
    
    def inner_function():
        print(f"Inner function can access x: {x}")
    
    inner_function()
    print(f"Outer function x: {x}")

outer_function()

print("\nNonlocal Keyword Example:")

def counter_function():
    """Demonstrates the use of nonlocal keyword"""
    count = 0
    
    def increment():
        nonlocal count  # Use nonlocal to modify outer function's variable
        count += 1
        return count
    
    print("Counting with nonlocal:")
    print(increment())  # 1
    print(increment())  # 2
    print(increment())  # 3

counter_function()

print("\n")

# 3. Global Scope
print("3. Global Scope Examples")
print("-" * 30)

# Global variable
global_var = "I am global"

def show_global():
    """Demonstrates accessing global variable"""
    print(f"Accessing global_var inside function: {global_var}")

def modify_global_wrong():
    """Demonstrates what happens when trying to modify global without global keyword"""
    try:
        global_var = "Modified?"  # This creates a new local variable
        print(f"Inside function: {global_var}")
    except UnboundLocalError as e:
        print(f"Error: {e}")

def modify_global_correct():
    """Demonstrates correct way to modify global variable"""
    global global_var
    global_var = "Successfully modified!"

print(f"Original global_var: {global_var}")
show_global()
modify_global_wrong()
print(f"After wrong modification: {global_var}")
modify_global_correct()
print(f"After correct modification: {global_var}")

print("\n")

# 4. Complex Scope Example
print("4. Complex Scope Example")
print("-" * 30)

global_value = 100

def complex_scope_example():
    """Demonstrates interaction between different scope levels"""
    # Enclosing scope variable
    value = 200
    
    def level1():
        # Local scope variable
        value = 300
        print(f"Level 1 (Local) value: {value}")
        
        def level2():
            nonlocal value  # Refers to value in level1
            value = 400
            print(f"Level 2 (Nonlocal) value: {value}")
            
            def level3():
                global global_value  # Refers to global_value
                print(f"Level 3 - Current global value: {global_value}")
                global_value = 500
            
            level3()
        
        print(f"Before level2, value is: {value}")
        level2()
        print(f"After level2, value is: {value}")
    
    print(f"Before level1, value is: {value}")
    level1()
    print(f"After level1, value is: {value}")

print(f"Initial global_value: {global_value}")
complex_scope_example()
print(f"Final global_value: {global_value}")

print("\n")

# 5. Best Practices
print("5. Scope Best Practices")
print("-" * 30)

class ConfigManager:
    """Demonstrates a better way to handle global state using classes"""
    _instance = None
    
    def __init__(self):
        self.settings = {
            'debug': False,
            'api_key': 'secret',
            'max_connections': 100
        }
    
    @classmethod
    def get_instance(cls):
        """Singleton pattern to manage global state"""
        if cls._instance is None:
            cls._instance = ConfigManager()
        return cls._instance

def good_practice_example():
    """Demonstrates better practices for handling scope"""
    # Use class instance instead of global variables
    config = ConfigManager.get_instance()
    
    print("Accessing global state through class:")
    print(f"Debug mode: {config.settings['debug']}")
    print(f"Max connections: {config.settings['max_connections']}")
    
    # Modify settings through class method
    config.settings['debug'] = True
    print(f"After modification - Debug mode: {config.settings['debug']}")

good_practice_example()
