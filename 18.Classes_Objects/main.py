# Python Classes and Objects Crash Course

# Basic Class Definition
class SimpleClass:
    """
    This is a simple class demonstration
    Classes are blueprints for creating objects
    """
    # Class variable (shared by all instances)
    class_variable = "I am shared by all instances"

    def __init__(self):
        """
        The __init__ method is called when creating a new instance
        It's like a constructor in other programming languages
        """
        pass

# More Practical Class Example
class Person:
    """
    A class representing a person with name, age, and various methods
    This is a more practical example of OOP in Python
    """
    
    # Class variable (shared by all instances)
    species = "Homo Sapiens"
    
    def __init__(self, name, age):
        """
        Initialize a new Person instance
        self: refers to the instance being created
        name: person's name (string)
        age: person's age (integer)
        """
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        self._private_var = "I am a private variable"  # Convention for private variables
    
    def __str__(self):
        """
        Special method that returns string representation of the object
        Called when print() is used on the object
        """
        return f"Person(name='{self.name}', age={self.age})"
    
    def introduce(self):
        """
        Instance method to introduce the person
        Uses instance variables through self
        """
        return f"Hi, I'm {self.name} and I'm {self.age} years old!"
    
    def have_birthday(self):
        """
        Method to increment the person's age
        Demonstrates modifying instance variables
        """
        self.age += 1
        return f"Happy Birthday! {self.name} is now {self.age} years old!"
    
    @classmethod
    def get_species(cls):
        """
        Class method example
        Can be called on the class itself, not just instances
        """
        return cls.species
    
    @staticmethod
    def is_adult(age):
        """
        Static method example
        Doesn't need instance or class reference
        """
        return age >= 18

# Example Usage
def main():
    # Creating instances of the Person class
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)
    
    # Using instance methods
    print(person1.introduce())  # Output: Hi, I'm Alice and I'm 25 years old!
    print(person2.introduce())  # Output: Hi, I'm Bob and I'm 30 years old!
    
    # Using the __str__ method implicitly
    print(person1)  # Output: Person(name='Alice', age=25)
    
    # Modifying object properties
    print(person1.have_birthday())  # Output: Happy Birthday! Alice is now 26 years old!
    
    # Using class method
    print(Person.get_species())  # Output: Homo Sapiens
    
    # Using static method
    print(Person.is_adult(20))  # Output: True
    print(Person.is_adult(15))  # Output: False
    
    # Demonstrating class variables
    print(person1.species)  # Accessing class variable through instance
    print(Person.species)   # Accessing class variable through class
    
    # Modifying instance variables
    person1.name = "Alicia"
    print(person1.introduce())  # Output: Hi, I'm Alicia and I'm 26 years old!

if __name__ == "__main__":
    main()
