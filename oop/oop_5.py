# __init__ is as constructor?
# the __init__ method in Python acts as a constructor. 
# It is a special method that is called when an instance (object) of the class is created. 
# This method is typically used to initialize the attributes of the instance.
# Here’s a more detailed explanation and example:
# Using __init__ as a Constructor
# When you create a new instance of a class, Python automatically calls the __init__ method to initialize the object. 
# This method can take arguments (other than self), which can be used to set up the initial state of the object.

# Example:
class Dog:
    def __init__(self, name, age):
        self.name = name  # Initialize the name attribute
        self.age = age    # Initialize the age attribute

    def bark(self):
        return f"{self.name} says woof!"

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Milo", 5)

# Accessing attributes and methods
print(dog1.name)  # Output: Buddy
print(dog1.age)   # Output: 3
print(dog1.bark())  # Output: Buddy says woof!

print(dog2.name)  # Output: Milo
print(dog2.age)   # Output: 5
print(dog2.bark())  # Output: Milo says woof!

# Breakdown
# 1.	Class Definition: The Dog class is defined with an __init__ method that takes self, name, and age as arguments.
# 2.	Initialization: When dog1 = Dog("Buddy", 3) is executed, the __init__ method is called with name="Buddy" and 
# age=3. Inside __init__, self.name is set to "Buddy" and self.age is set to 3.
# 3.	Attributes and Methods: The attributes name and age are initialized for each instance. 
# The bark method returns a string that includes the instance's name.

# Why __init__ is Called a Constructor
# •	Construction: It constructs the instance of the class with initial values.
# •	Initialization: It initializes the instance with the given arguments, setting the initial state of the object.
# While __init__ is not the only method related to object creation (there is also __new__, which is responsible for creating the instance), 
# it is the most commonly used method for setting up an object after it has been created.
# how to have default values for attributes class
# You can provide default values for attributes in a class by specifying default arguments in the __init__ method. This way, 
# if no value is provided for an attribute when an instance of the class is created, the default value will be used.
# Example
# Here’s an example of how to use default values for class attributes:
class Dog:
    def __init__(self, name="Unknown", age=0):
        self.name = name  # Initialize the name attribute with a default value
        self.age = age    # Initialize the age attribute with a default value

    def bark(self):
        return f"{self.name} says woof!"

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)  # Provided name and age
dog2 = Dog("Milo")      # Provided name, default age
dog3 = Dog()            # Default name and age

# Accessing attributes and methods
print(dog1.name)  # Output: Buddy
print(dog1.age)   # Output: 3
print(dog1.bark())  # Output: Buddy says woof!

print(dog2.name)  # Output: Milo
print(dog2.age)   # Output: 0
print(dog2.bark())  # Output: Milo says woof!

print(dog3.name)  # Output: Unknown
print(dog3.age)   # Output: 0
print(dog3.bark())  # Output: Unknown says woof!

# Breakdown
# 1.	Class Definition: The Dog class is defined with an __init__ method that has default values for name ("Unknown") and age (0).
# 2.	Instance Creation:
# o	dog1 = Dog("Buddy", 3): Both name and age are provided, so these values are used.
# o	dog2 = Dog("Milo"): Only name is provided, so age defaults to 0.
# o	dog3 = Dog(): Neither name nor age are provided, so both default to "Unknown" and 0, respectively.

# Using Default Values for Mutable Types
# When using mutable types (like lists or dictionaries) as default values, you should be careful because the default value is shared across all instances of the class. 
# Instead, use None as the default value and create a new instance of the mutable type inside the __init__ method.
# Example with Mutable Default Values
class Dog:
    def __init__(self, name="Unknown", age=0, toys=None):
        self.name = name
        self.age = age
        self.toys = toys if toys is not None else []  # Create a new list if none is provided

    def add_toy(self, toy):
        self.toys.append(toy)

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Milo")

# Adding toys
dog1.add_toy("Ball")
dog2.add_toy("Frisbee")

# Accessing attributes
print(dog1.name)  # Output: Buddy
print(dog1.toys)  # Output: ['Ball']

print(dog2.name)  # Output: Milo
print(dog2.toys)  # Output: ['Frisbee']

# In this example, each instance of the Dog class gets its own list of toys, even if the toys parameter is not provided when creating the instance. 
# This avoids the issue of all instances sharing the same default list.