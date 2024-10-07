# oop main concepts in python

# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to organize code. 
# Python is an object-oriented language and supports the following main concepts of OOP:

# 1. Classes and Objects
# •	Class: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# •	Object: An instance of a class. Each object can have unique values for the attributes defined in the class.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an instance (object) of the Dog class
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says woof!

# 2. Encapsulation
# Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit or class. 
# It also restricts direct access to some of the object's components, which can prevent the accidental modification of data.
class Dog:
    def __init__(self, name, age):
        self._name = name  # Using _ to indicate protected attributes
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

my_dog = Dog("Buddy", 3)
print(my_dog.get_name())  # Output: Buddy
my_dog.set_name("Max")
print(my_dog.get_name())  # Output: Max

# 3. Inheritance
# Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). 
# This promotes code reuse and establishes a relationship between classes.
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Dog")
        self.name = name
        self.age = age

    def make_sound(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.species)  # Output: Dog
print(my_dog.make_sound())  # Output: Buddy says woof!

# 4. Polymorphism
# Polymorphism allows methods to do different things based on the object it is acting upon, even if the method name is the same. 
# It enables a single interface to represent different underlying forms (data types).

class Cat:
    def make_sound(self):
        return "Meow"

class Dog:
    def make_sound(self):
        return "Woof"

def animal_sound(animal):
    print(animal.make_sound())

my_cat = Cat()
my_dog = Dog()

animal_sound(my_cat)  # Output: Meow
animal_sound(my_dog)  # Output: Woof

# 5. Abstraction
# Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object. 
# It can be achieved using abstract classes and interfaces.
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

my_dog = Dog()
my_cat = Cat()

print(my_dog.make_sound())  # Output: Woof
print(my_cat.make_sound())  # Output: Meow

# Summary
# •	Classes and Objects: Classes are blueprints for objects. Objects are instances of classes.
# •	Encapsulation: Bundling data and methods that operate on the data within one unit, and restricting access to some components.
# •	Inheritance: Mechanism for creating a new class using details of an existing class.
# •	Polymorphism: A single interface to different types of objects.
# •	Abstraction: Hiding complex implementation details and exposing only the necessary parts.
# These concepts form the foundation of OOP in Python and allow for the creation of modular, reusable, and organized code.
