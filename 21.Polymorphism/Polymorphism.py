#!/usr/bin/env python3

# Python Polymorphism Crash Course
# ------------------------------
# Polymorphism means "many forms" and occurs when we have many 
# classes or functions that are related to each other by inheritance or common interface.

# 1. Built-in Function Polymorphism
print("1. Built-in Function Polymorphism")
print("-" * 35)

# len() function works with different types
print("Using len() with different types:")
text = "Hello World!"
number_list = [1, 2, 3, 4, 5]
sample_tuple = (1, "apple", 3.14)
sample_dict = {"name": "John", "age": 30}

print(f"Length of string: {len(text)}")
print(f"Length of list: {len(number_list)}")
print(f"Length of tuple: {len(sample_tuple)}")
print(f"Length of dictionary: {len(sample_dict)}")

print("\n")

# 2. Class Method Polymorphism
print("2. Class Method Polymorphism")
print("-" * 35)

class Animal:
    """Base class to demonstrate method polymorphism"""
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """Each animal makes a different sound"""
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Duck(Animal):
    def make_sound(self):
        return "Quack!"

# Creating instances of different animals
dog = Dog("Buddy")
cat = Cat("Whiskers")
duck = Duck("Donald")

# Demonstrating polymorphic behavior
animals = [dog, cat, duck]
print("Different animals making sounds:")
for animal in animals:
    print(f"{animal.name} says: {animal.make_sound()}")

print("\n")

# 3. Inheritance and Polymorphism
print("3. Inheritance and Polymorphism")
print("-" * 35)

class Vehicle:
    """Parent class for different types of vehicles"""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        return "Vehicle starting..."
    
    def stop(self):
        return "Vehicle stopping..."
    
    def describe(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def start(self):
        return "Car engine starting... Vroom!"
    
    def stop(self):
        return "Car engine stopping... Engine off!"

class ElectricCar(Vehicle):
    def start(self):
        return "Electric car powering up... Silently!"
    
    def stop(self):
        return "Electric car shutting down... Power off!"

class Motorcycle(Vehicle):
    def start(self):
        return "Motorcycle engine starting... Vrooom vrooom!"
    
    def stop(self):
        return "Motorcycle engine stopping... Kickstand down!"

# Creating different vehicles
regular_car = Car("Toyota", "Camry", 2022)
electric_car = ElectricCar("Tesla", "Model 3", 2023)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)

# Demonstrating polymorphic behavior with vehicles
vehicles = [regular_car, electric_car, motorcycle]

print("Vehicle Operations:")
for vehicle in vehicles:
    print(f"\n{vehicle.describe()}:")
    print(f"Starting: {vehicle.start()}")
    print(f"Stopping: {vehicle.stop()}")

print("\n")

# 4. Duck Typing Polymorphism
print("4. Duck Typing Polymorphism")
print("-" * 35)

class Printer:
    """Demonstrates duck typing - if it can print, it's a printer"""
    def print_document(self, document):
        print(f"Printing: {document}")

class Scanner:
    """Demonstrates duck typing - if it can scan, it's a scanner"""
    def scan_document(self, document):
        print(f"Scanning: {document}")

class AllInOnePrinter:
    """Class that can both print and scan"""
    def print_document(self, document):
        print(f"All-in-One Printing: {document}")
    
    def scan_document(self, document):
        print(f"All-in-One Scanning: {document}")

def process_document(machine, document):
    """Function demonstrating duck typing
    It doesn't care about the type of machine, only that it can perform the action
    """
    if hasattr(machine, 'print_document'):
        machine.print_document(document)
    if hasattr(machine, 'scan_document'):
        machine.scan_document(document)

# Creating different machines
printer = Printer()
scanner = Scanner()
all_in_one = AllInOnePrinter()

print("Processing documents with different machines:")
document = "Important Report.pdf"

print("\nUsing Regular Printer:")
process_document(printer, document)

print("\nUsing Scanner:")
process_document(scanner, document)

print("\nUsing All-in-One:")
process_document(all_in_one, document)
