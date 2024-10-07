# Instance Methods
# Instance methods are functions defined within a class that operate on instances of the class:
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

my_instance = MyClass("Alice")
print(my_instance.greet())  # Output: Hello, Alice!

# Class Attributes
# Class attributes are shared among all instances of a class:
class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self, name):
        self.name = name

my_instance = MyClass("Alice")
print(MyClass.class_attribute)  # Output: I am a class attribute
print(my_instance.class_attribute)  # Output: I am a class attribute