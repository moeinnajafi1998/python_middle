# Tuples in Python are immutable, ordered collections of elements. 
# They are similar to lists but, once created, their elements cannot be modified. 
# Here’s a comprehensive look at tuple operations:

# Creating Tuples
# 1.	Empty tuple:
empty_tuple = ()

# 2.	Non-empty tuple:
fruits = ("apple", "banana", "cherry")

# 3.	Single-element tuple (Note the comma):
single_element_tuple = ("apple",)

# 4.	Without parentheses:
fruits = "apple", "banana", "cherry"

# Accessing Elements
# 1.	By index:
first_fruit = fruits[0]  # "apple"

# 2.	Negative index:
last_fruit = fruits[-1]  # "cherry"

# Tuple Operations
# 1.	Concatenate tuples:
combined = fruits + ("kiwi", "orange")

# 2.	Repeat tuples:
repeated_fruits = fruits * 2

# 3.	Check for membership:
has_apple = "apple" in fruits  # True

# 4.	Length of a tuple:
length = len(fruits)  # 3

# 5.	Slicing tuples:
sliced = fruits[1:3]  # ("banana", "cherry")

# Tuple Methods
# 1.	Count occurrences of an element:
count_apple = fruits.count("apple")

# 2.	Find index of an element:
index_cherry = fruits.index("cherry")

# Unpacking Tuples
# 1.	Basic unpacking:
fruit1, fruit2, fruit3 = fruits

# 2.	Unpacking with wildcard:
fruit1, *rest = fruits  # rest will be ["banana", "cherry"]

# 3.	Nested unpacking:
nested_tuple = (1, 2, ("apple", "banana"))
a, b, (fruit1, fruit2) = nested_tuple

# Tuple Functions
# 1.	zip function: Combining two or more iterables into a list of tuples.
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
combined = list(zip(names, ages))  # [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# 2.	sorted function: Returning a sorted list of a tuple’s elements.
sorted_fruits = sorted(fruits)  # ["apple", "banana", "cherry"]

# Example Usage
# Example 1: Basic Operations
fruits = ("apple", "banana", "cherry")
print(fruits[1])  # Access second element
print(fruits[-1])  # Access last element
print(fruits[1:3])  # Slice the tuple
print(fruits + ("kiwi",))  # Concatenate tuples
print(fruits * 2)  # Repeat tuple
print("apple" in fruits)  # Check membership
print(len(fruits))  # Length of the tuple

# Example 2: Tuple Methods
numbers = (1, 2, 3, 2, 4, 2, 5)
print(numbers.count(2))  # Count occurrences of 2
print(numbers.index(4))  # Find index of first occurrence of 4

# Example 3: Unpacking Tuples/
person = ("Alice", 30, "New York")
name, age, city = person
print(name)  # "Alice"
print(age)  # 30
print(city)  # "New York"

# Unpacking with wildcard
data = (1, 2, 3, 4, 5)
first, *rest = data
print(first)  # 1
print(rest)  # [2, 3, 4, 5]

# Nested unpacking
nested_tuple = (1, 2, ("apple", "banana"))
a, b, (fruit1, fruit2) = nested_tuple
print(a)  # 1
print(b)  # 2
print(fruit1)  # "apple"
print(fruit2)  # "banana"

# Use Cases for Tuples
# 1.	Immutable Data: When you need to ensure that a collection of values does not change.
coordinates = (10, 20)

# 2.	Dictionary Keys: Using tuples as keys in dictionaries because they are hashable.
location = {(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"}

# 3.	Returning Multiple Values: Returning multiple values from a function.
def get_min_max(numbers):
    return min(numbers), max(numbers)
min_num, max_num = get_min_max([1, 2, 3, 4, 5])

# 4.	Grouping Data: Grouping related data together.
student = ("Alice", 23, "A")

# 5.	Using with zip: Combining multiple iterables.
names = ("Alice", "Bob")
scores = (90, 85)
combined = list(zip(names, scores))  # [("Alice", 90), ("Bob", 85)]

# Tuples are a fundamental part of Python, providing an efficient way to work with ordered collections of items that should not change.
# when we use tuples?
# Tuples in Python are used primarily in situations where immutable, 
# ordered collections of elements are needed. Here are some common scenarios where tuples are particularly useful:
# When to Use Tuples
# 1.	Immutable Data:
# o	Tuples are immutable, meaning their elements cannot be changed after creation. Use tuples when you have data that should remain constant throughout the program's execution.
dimensions = (800, 600)

# 2.	Data Integrity:
# o	Tuples ensure data integrity because they cannot be modified accidentally. This is useful in scenarios where changing data could lead to errors or unintended consequences.
point = (10, 20)

# 3.	Function Return Values:
# o	Tuples are often used to return multiple values from a function in a single return statement.
def get_coordinates():
    x = 10
    y = 20
    return x, y
coord = get_coordinates()

# 4.	Efficiency:
# o	Tuples are more memory efficient than lists because they are immutable. Use tuples when storing large amounts of data that should not change to optimize memory usage.
months = ("January", "February", "March", "April", "May", "June")

# 5.	Sequence Unpacking:
# o	Tuples support unpacking, making it easy to assign multiple variables in a single statement.
person = ("Alice", 30, "New York")
name, age, city = person

# 6.	Dictionary Keys:
# o	Tuples can be used as keys in dictionaries because they are immutable and hashable. This makes tuples suitable for scenarios where you need to create dictionaries with composite keys.
locations = {("40.7128", "-74.0060"): "New York", ("34.0522", "-118.2437"): "Los Angeles"}

# 7.	Ordered Data:
# o	Use tuples when the order of elements matters and should be preserved. Tuples maintain the order of elements as they are defined.
menu_items = ("Pizza", "Burger", "Salad")

# Example Use Cases
# Example 1: Immutable Configuration Data
# Configuration settings that should not change
database_config = ("localhost", 3306, "username", "password")

# Example 2: Returning Multiple Values from a Function
def divide_numbers(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder
result = divide_numbers(10, 3)

# Example 3: Dictionary Keys with Tuples
# Using tuples as keys in a dictionary
coordinates = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (51.5074, -0.1278): "London"
}

# Example 4: Sequence Unpacking
# Unpacking a tuple into variables
person = ("Alice", 30, "New York")
name, age, city = person

# Example 5: Storing Constants
# Constants that should not change
PI = 3.14
EARTH_RADIUS = 6371

# When Not to Use Tuples
# 1.	When Mutable Operations Are Required:
# o	Use lists if you need to modify the collection of items, such as adding or removing elements.
# Mutable list example
tasks = ["task1", "task2", "task3"]
tasks.append("task4")

# 2.	For Large Data Sets with Frequent Updates:
# o	Lists are more suitable if you frequently update or modify the data set, as they support mutable operations.
# Mutable list example for frequent updates
temperatures = [23, 24, 25, 22, 26]
temperatures[2] = 30

# 3.	If Order of Elements Does Not Matter:
# o	Use sets if the order of elements is not important and you need to ensure uniqueness of elements.
# Set example
unique_numbers = {1, 2, 3, 4, 5}

# Summary
# Tuples are ideal when you need an ordered, 
# immutable collection of elements that should not change throughout the program's execution. They offer efficiency, data integrity, 
# and are well-suited for scenarios involving constant data, multiple return values from functions, and dictionary keys with composite values. However, 
# if you need to modify the collection of elements or the order does not matter, consider using lists instead.
