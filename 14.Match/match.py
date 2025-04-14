"""
Python Match Statement Crash Course
--------------------------------
The match statement (introduced in Python 3.10+) is a powerful way to do pattern matching
and replace complex if-elif-else chains with more readable code.
"""

# Basic Match Statement Example
def print_weekday(day):
    """Simple match statement to print weekday names"""
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:  # Default case (like 'else' in if statements)
            print("Invalid day number")

# Example with Default Case and Multiple Values
def check_weekend(day):
    """Match statement with multiple values using | (OR) operator"""
    match day:
        case 6 | 7:  # Multiple values using pipe operator
            print("It's the weekend!")
        case 1 | 2 | 3 | 4 | 5:
            print("It's a weekday")
        case _:  # Default case
            print("Invalid day number")

# Match with Guards (Conditional Matching)
def check_workday_in_month(day, month):
    """Match statement with guard conditions using if"""
    match day:
        case 1 | 2 | 3 | 4 | 5 if month == 4:
            print("This is a workday in April")
        case 1 | 2 | 3 | 4 | 5 if month == 5:
            print("This is a workday in May")
        case 6 | 7:
            print("It's the weekend!")
        case _:
            print("No specific match found")

# Advanced Pattern Matching with Sequences
def analyze_point(point):
    """Match statement with sequence pattern matching"""
    match point:
        case (0, 0):
            print("Point is at origin")
        case (0, y):
            print(f"Point is on y-axis at y={y}")
        case (x, 0):
            print(f"Point is on x-axis at x={x}")
        case (x, y):
            print(f"Point is at coordinates ({x}, {y})")
        case _:
            print("Not a valid point")

# Match with Class Patterns
class Command:
    def __init__(self, action, value=None):
        self.action = action
        self.value = value

def process_command(command):
    """Match statement with class pattern matching"""
    match command:
        case Command(action="quit"):
            print("Exiting program")
        case Command(action="save", value=str(filename)):
            print(f"Saving to {filename}")
        case Command(action="load", value=str(filename)):
            print(f"Loading from {filename}")
        case _:
            print("Unknown command")

# Example Usage
if __name__ == "__main__":
    print("\n--- Basic Weekday Example ---")
    print_weekday(1)  # Monday
    print_weekday(8)  # Invalid day number

    print("\n--- Weekend Check Example ---")
    check_weekend(6)  # It's the weekend!
    check_weekend(3)  # It's a weekday

    print("\n--- Workday in Month Example ---")
    check_workday_in_month(3, 4)  # This is a workday in April
    check_workday_in_month(6, 5)  # It's the weekend!

    print("\n--- Point Analysis Example ---")
    analyze_point((0, 0))  # Point is at origin
    analyze_point((5, 0))  # Point is on x-axis at x=5

    print("\n--- Command Processing Example ---")
    process_command(Command("quit"))  # Exiting program
    process_command(Command("save", "data.txt"))  # Saving to data.txt
