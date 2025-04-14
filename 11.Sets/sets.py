# Python Sets - A Comprehensive Guide
# Sets are unordered collections of unique elements

# 1. Creating Sets
print("\n1. Creating Sets:")
# Using curly braces
fruits_set = {"apple", "banana", "cherry"}
print("Set created with curly braces:", fruits_set)

# Using the set() constructor
numbers_set = set([1, 2, 3, 4, 5])
print("Set created with constructor:", numbers_set)

# 2. Set Properties
print("\n2. Set Properties:")
# Sets are unordered (elements have no index)
# Sets are mutable (can add/remove elements)
# Sets contain unique elements (no duplicates)
duplicate_set = {"apple", "banana", "apple", "cherry"}
print("Set with duplicates (notice duplicates are removed):", duplicate_set)

# Special case: True == 1 and False == 0 in sets
bool_set = {True, 1, False, 0}
print("Set with boolean and numbers:", bool_set)  # Will show {False, True} or {0, 1}

# 3. Set Operations
print("\n3. Set Operations:")
# Adding elements
fruits_set.add("orange")
print("After adding 'orange':", fruits_set)

# Removing elements (multiple ways)
fruits_set.remove("banana")  # Raises error if element not found
print("After removing 'banana':", fruits_set)

fruits_set.discard("nonexistent")  # No error if element not found
print("After discarding nonexistent item:", fruits_set)

# Pop removes and returns an arbitrary element
popped_item = fruits_set.pop()
print("Popped item:", popped_item)
print("Set after pop:", fruits_set)

# 4. Set Mathematical Operations
print("\n4. Set Mathematical Operations:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (all unique elements from both sets)
print("Union:", set1.union(set2))  # Alternative: set1 | set2

# Intersection (elements common to both sets)
print("Intersection:", set1.intersection(set2))  # Alternative: set1 & set2

# Difference (elements in set1 but not in set2)
print("Difference:", set1.difference(set2))  # Alternative: set1 - set2

# Symmetric Difference (elements in either set, but not both)
print("Symmetric Difference:", set1.symmetric_difference(set2))  # Alternative: set1 ^ set2

# 5. Set Methods for Comparison
print("\n5. Set Comparisons:")
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# Subset check
print("Is A subset of B?", A.issubset(B))  # Alternative: A <= B

# Superset check
print("Is B superset of A?", B.issuperset(A))  # Alternative: B >= A

# Disjoint check (no common elements)
print("Are A and B disjoint?", A.isdisjoint({6, 7, 8}))

# 6. Set Comprehension
print("\n6. Set Comprehension:")
# Creating a set using set comprehension
squares_set = {x**2 for x in range(5)}
print("Squares set using comprehension:", squares_set)

# 7. Practical Example
print("\n7. Practical Example:")
# Finding unique characters in a string
text = "hello world"
unique_chars = set(text)
print("Unique characters in 'hello world':", unique_chars)

# Finding common elements in lists
list1 = [1, 2, 3, 4, 5, 5, 5]
list2 = [4, 5, 6, 7, 7, 7]
common_elements = set(list1).intersection(set(list2))
print("Common elements between lists:", common_elements)
