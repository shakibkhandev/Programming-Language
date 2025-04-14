# Python If-Else Statement Crash Course
# This file demonstrates various ways to use conditional statements in Python

# 1. Basic If Statement
print("1. Basic If Statement Example:")
a = 33
b = 200

if b > a:
    print(f"{b} is greater than {a}")  # Using f-string for better output formatting

# 2. If-Elif-Else Statement
print("\n2. If-Elif-Else Example:")
x = 33
y = 33

if y > x:
    print("y is greater than x")
elif x == y:
    print("x and y are equal")
else:
    print("x is greater than y")

# 3. Short Hand If (One-liner)
print("\n3. Short Hand If Example:")
age = 20
# Using one-line if statement when we have a single condition
if age >= 18: print("You are an adult")

# 4. Ternary Operator (One-line If-Else)
print("\n4. Ternary Operator Example:")
a, b = 2, 330
# Format: [value_if_true] if [condition] else [value_if_false]
result = "A" if a > b else "B"
print(f"Result of ternary operation: {result}")

# 5. Multiple Conditions using and, or, not
print("\n5. Multiple Conditions Example:")
age = 25
income = 50000
has_degree = True

# Using 'and' operator - all conditions must be True
if age >= 18 and income >= 30000:
    print("You are eligible for a basic credit card")

# Using 'or' operator - at least one condition must be True
if income >= 100000 or has_degree:
    print("You are eligible for a premium credit card")

# Using 'not' operator - reverses the boolean value
if not age < 18:
    print("You are not a minor")

# 6. Nested If Statements
print("\n6. Nested If Statements Example:")
score = 85

if score >= 60:
    print("You passed!")
    if score >= 80:
        print("With distinction!")
        if score >= 90:
            print("With high distinction!")
    else:
        print("Keep working to improve!")

# 7. The pass Statement
print("\n7. Pass Statement Example:")
# pass is used when we need an empty if statement (placeholder)
if score > 100:
    pass  # TODO: Handle invalid scores

# 8. Complex Example combining multiple concepts
print("\n8. Complex Example:")
def check_eligibility(age, income, credit_score):
    """
    Function to check loan eligibility using multiple conditions
    """
    if age < 18:
        return "Too young for a loan"
    
    if income >= 50000 and credit_score >= 700:
        if age >= 25:
            return "Eligible for premium loan"
        else:
            return "Eligible for standard loan"
    elif income >= 30000 or credit_score >= 650:
        return "Eligible for basic loan"
    else:
        return "Not eligible for loan"

# Test the complex example
test_age = 30
test_income = 60000
test_credit_score = 750

result = check_eligibility(test_age, test_income, test_credit_score)
print(f"Loan eligibility result: {result}")
