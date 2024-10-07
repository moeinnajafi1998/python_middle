# Classes are a fundamental part of object-oriented programming (OOP) in Python. 
# They provide a way to bundle data and functionality together. 
# Creating a new class creates a new type of object, allowing new instances of that type to be made.
# Each instance of a class can have attributes attached to it for maintaining its state, and methods for modifying its state.
# Here's an overview of classes in Python:
# Defining a Class
# You define a class using the class keyword:

class MyClass:
    pass  # An empty block
# Creating an Instance of a Class
# To create an instance of a class, you call the class using its name and pass any arguments that the __init__ method requires:
my_instance = MyClass()

# The __init__ Method
# The __init__ method is a special method that is called when an instance of the class is created. 
# It's commonly used to initialize the instance's attributes:
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

my_instance = MyClass("value1", "value2")
