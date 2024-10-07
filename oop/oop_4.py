# Encapsulation
# Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit or class, 
# and restricting access to some of the object's components:
class MyClass:
    def __init__(self, value):
        self._value = value  # _ indicates a "protected" variable

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

instance = MyClass(10)
print(instance.get_value())  # Output: 10
instance.set_value(20)
print(instance.get_value())  # Output: 20
# These are some of the basic concepts of classes in Python. 
# They allow for the creation of more complex and structured code by grouping related properties and methods together.