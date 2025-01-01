
# In Python, methods are functions associated with objects.
# They can be classified into different types based on their purpose and how they interact with the object or class. Here's an overview:

# 1. Instance Methods
# Definition: These methods operate on an instance of a class and can access or modify its instance attributes.
# Usage: Defined with self as the first parameter.
# Example:
class Example:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        return f"The value is {self.value}"

obj = Example(10)
print(obj.instance_method())  # Output: The value is 10

# 2. Class Methods
# Definition: These methods operate on the class itself, rather than on an instance. They can access or modify class-level attributes.
# Usage: Defined using the @classmethod decorator with cls as the first parameter.
# Example:
class Example:
    class_attribute = "Class Level"

    @classmethod
    def class_method(cls):
        return f"Accessing: {cls.class_attribute}"

print(Example.class_method())  # Output: Accessing: Class Level

# 3. Static Methods
# Definition: These methods do not depend on any instance or class attributes. They are independent utility functions that belong to the class's namespace.
# Usage: Defined using the @staticmethod decorator.
# Example:
class Example:
    @staticmethod
    def static_method(x, y):
        return x + y

print(Example.static_method(3, 4))  # Output: 7

# 4. Magic (or Dunder) Methods
# Definition: These special methods are surrounded by double underscores (e.g., __init__, __str__). They enable operator overloading and define object behavior in specific contexts.
# Examples:
# __init__: Initialization (constructor)
# __str__: String representation
# __add__: Overloads the + operator
# Example:
class Example:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Value: {self.value}"

obj = Example(42)
print(obj)  # Output: Value: 42

# 5. Abstract Methods
# Definition: These methods are defined in an abstract base class and must be implemented by subclasses.
# Usage: Created using the @abstractmethod decorator from the abc module.
# Example:
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        return "Implemented in subclass"

obj = ConcreteClass()
print(obj.abstract_method())  # Output: Implemented in subclass

# 6. Getter, Setter, and Deleter Methods (Property Methods)
# Definition: These methods allow controlled access to instance attributes.
# Usage: Use the @property, @<property_name>.setter, and @<property_name>.deleter decorators.
# Example:
class Example:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    def value(self):
        del self._value

obj = Example(10)
print(obj.value)  # Output: 10
obj.value = 20
print(obj.value)  # Output: 20
del obj.value