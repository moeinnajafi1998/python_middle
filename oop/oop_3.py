# Inheritance
# Classes in Python can inherit from other classes, allowing you to create a hierarchy of classes:
class ParentClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)  # Call the initializer of the parent class
        self.age = age

    def introduce(self):
        return f"I am {self.name} and I am {self.age} years old."

child_instance = ChildClass("Bob", 10)
print(child_instance.greet())  # Output: Hello, Bob!
print(child_instance.introduce())  # Output: I am Bob and I am 10 years old.

# Special Methods
# Python classes can implement special methods, also known as magic methods or dunder methods (because they have double underscores before and after their names), 
# to define behaviors for built-in operations:
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value: {self.value}"

    def __add__(self, other):
        return MyClass(self.value + other.value)

instance1 = MyClass(10)
instance2 = MyClass(20)
print(instance1)  # Output: MyClass with value: 10
print(instance1 + instance2)  # Output: MyClass with value: 30
