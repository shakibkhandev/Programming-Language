#!/usr/bin/env python3

# Python Iterators Crash Course
# ----------------------------
# An iterator is an object that contains countable values and can be iterated upon.
# It must implement two methods: __iter__() and __next__()

# Basic Iterator Example with Built-in Types
print("1. Basic Iterator Examples")
print("-" * 30)

# Example 1: Tuple Iterator
mytuple = ("apple", "banana", "cherry")
tuple_iterator = iter(mytuple)  # Get iterator from tuple

print("Iterating through tuple using next():")
print(next(tuple_iterator))  # Output: apple
print(next(tuple_iterator))  # Output: banana
print(next(tuple_iterator))  # Output: cherry

print("\n")  # Empty line for readability

# Example 2: String Iterator
print("String Iterator Example:")
text = "Python"
string_iterator = iter(text)  # Get iterator from string

print("Iterating through string using next():")
for _ in range(len(text)):
    print(next(string_iterator))

print("\n")

# Example 3: Custom Iterator Class
print("2. Custom Iterator Implementation")
print("-" * 30)

class CountUpTo:
    """
    A custom iterator that counts up to a specified number.
    This demonstrates how to create your own iterator class.
    """
    
    def __init__(self, max_value):
        """Initialize the iterator with a maximum value"""
        self.max_value = max_value
    
    def __iter__(self):
        """
        Initialize the iterator.
        This method is called when the iterator is created.
        """
        self.current = 0
        return self
    
    def __next__(self):
        """
        Return the next value in the sequence.
        Raises StopIteration when the sequence is finished.
        """
        if self.current < self.max_value:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Using our custom iterator
counter = CountUpTo(5)
print("Using custom iterator with for loop:")
for num in counter:
    print(num)

print("\n")

# Example 4: Fibonacci Iterator
print("3. Fibonacci Sequence Iterator")
print("-" * 30)

class FibonacciSequence:
    """
    An iterator that generates Fibonacci numbers up to n terms.
    Demonstrates a more complex iterator implementation.
    """
    
    def __init__(self, terms):
        """Initialize with the number of terms to generate"""
        self.terms = terms
    
    def __iter__(self):
        """Initialize the iterator state"""
        self.current = 0
        self.next_num = 1
        self.count = 0
        return self
    
    def __next__(self):
        """Generate the next Fibonacci number"""
        if self.count < self.terms:
            # Store the current value to return
            result = self.current
            
            # Calculate the next Fibonacci number
            self.current, self.next_num = (
                self.next_num,
                self.current + self.next_num
            )
            
            self.count += 1
            return result
        else:
            raise StopIteration

# Using the Fibonacci iterator
print("First 10 numbers in Fibonacci sequence:")
fibonacci = FibonacciSequence(10)
for number in fibonacci:
    print(number, end=" ")

print("\n\n")

# Example 5: Practical Use Case
print("4. Practical Iterator Example")
print("-" * 30)

class DataProcessor:
    """
    An iterator that processes data in chunks.
    Demonstrates a practical use case for iterators.
    """
    
    def __init__(self, data, chunk_size):
        self.data = data
        self.chunk_size = chunk_size
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            # Get the next chunk of data
            chunk = self.data[self.index:self.index + self.chunk_size]
            self.index += self.chunk_size
            return chunk
        else:
            raise StopIteration

# Using the data processor
data = list(range(10))  # Sample data: [0,1,2,3,4,5,6,7,8,9]
processor = DataProcessor(data, chunk_size=3)

print("Processing data in chunks:")
for chunk in processor:
    print(f"Processing chunk: {chunk}")
