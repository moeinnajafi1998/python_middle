# Let's delve into Python lists and their operations. 
# Lists are one of the most versatile and widely used data structures in Python.
# They are ordered, mutable, and can contain elements of different types.

# Creating Lists
# •	Empty list:
my_list = []

# •	Non-empty list:
fruits = ["apple", "banana", "cherry"]

# Accessing Elements
# •	By index:
first_fruit = fruits[0]  # "apple"

# •	Negative index:
last_fruit = fruits[-1]  # "cherry"

# Modifying Lists
# •	Change element:
fruits[0] = "avocado"

# •	Add element (append):
fruits.append("orange")

# •	Insert element at a specific position:
fruits.insert(1, "blueberry")

# •	Extend list with another list:
more_fruits = ["kiwi", "grape"]
fruits.extend(more_fruits)

# •	Remove element by value:
fruits.remove("banana")

# •	Remove element by index (pop):
fruits.pop(1)  # Removes "blueberry"

# •	Clear all elements:
fruits.clear()

# List Operations
# •	Length of list:
len(fruits)

# •	Concatenate lists:
combined = fruits + more_fruits

# •	Repeat list:
repeated_fruits = fruits * 2

# Slicing Lists
# •	Basic slicing:
sliced = fruits[1:3]  # From index 1 to 2

# •	Slicing with step:
step_slice = fruits[0:5:2]  # Every second element from index 0 to 4

# •	Negative slicing:
reverse_slice = fruits[::-1]  # Reverse the list

# List Comprehensions
# •	Basic list comprehension:
squares = [x ** 2 for x in range(10)]

# •	With condition:
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]

# Sorting Lists
# •	Sort in place:
fruits.sort()

# •	Sort with custom key:
fruits.sort(key=len)  # Sort by length of the fruit names

# •	Sort and return new list:
sorted_fruits = sorted(fruits)

# Other Useful Methods
# •	Count occurrences of an element:
count_apple = fruits.count("apple")

# •	Find index of an element:
fruits = ["apple", "banana", "cherry"]
index_cherry = fruits.index("cherry")

# •	Copy a list:
fruits_copy = fruits.copy()


# Examples
# Example 1: Basic Operations
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Access second element
fruits[1] = "blueberry"  # Change second element
fruits.append("orange")  # Add new element at the end
fruits.insert(1, "kiwi")  # Insert "kiwi" at second position
print(fruits)  # ['apple', 'kiwi', 'blueberry', 'cherry', 'orange']
fruits.remove("kiwi")  # Remove "kiwi"
fruits.pop(2)  # Remove element at index 2 ("blueberry")
print(fruits)  # ['apple', 'cherry', 'orange']

# Example 2: Slicing and Comprehensions
numbers = list(range(10))
print(numbers[2:7])  # [2, 3, 4, 5, 6]
print(numbers[::2])  # [0, 2, 4, 6, 8]
print(numbers[::-1])  # Reverse the list

squares = [x ** 2 for x in numbers]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example 3: Sorting
fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(fruits)  # ['apple', 'banana', 'cherry']

fruits = ["banana", "apple", "cherry"]
sorted_fruits = sorted(fruits, reverse=True)
print(sorted_fruits)  # ['cherry', 'banana', 'apple']


# Summary of List Methods
# •	append(): Adds an element at the end.
# •	insert(): Adds an element at a specific position.
# •	extend(): Extends the list by appending elements from another list.
# •	remove(): Removes the first occurrence of an element.
# •	pop(): Removes the element at a specified position.
# •	clear(): Removes all elements from the list.
# •	index(): Returns the index of the first matched element.
# •	count(): Returns the count of the specified element.
# •	sort(): Sorts the list in ascending order.
# •	reverse(): Reverses the list.
# •	copy(): Returns a shallow copy of the list.
# These operations cover most of the essential functionalities you'll need when working with lists in Python.

# where should we use list?
# Lists in Python are versatile and can be used in a variety of scenarios. 
# Here are some common use cases and guidelines for when to use lists:
# When to Use Lists
# 1.	Ordered Collection of Items:
# o	Use lists when you need to maintain the order of items.
# o	Example: Storing a sequence of user inputs or events.
user_inputs = ["yes", "no", "maybe"]

# 2.	Mutable Collection:
# o	Use lists when you need a collection that can be modified (i.e., add, remove, or change elements).
# o	Example: Managing a dynamic list of tasks in a to-do application.
tasks = ["write code", "test application", "debug errors"]
tasks.append("deploy application")

# 3.	Heterogeneous Data:
# o	Use lists when you need to store items of different types.
# o	Example: A list of mixed data types for a single entity.
student_info = ["Alice", 23, "A"]

# 4.	Iteration and Access:
# o	Use lists when you need to iterate over a collection of items or access items by index.
# o	Example: Processing a list of numbers to calculate their squares.
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]

# 5.	Collections That May Contain Duplicates:
# o	Use lists when duplicates are allowed and you need to maintain all instances of items.
# o	Example: Storing a list of responses from users where duplicates are meaningful.
responses = ["yes", "no", "yes", "maybe", "no"]

# Specific Use Cases
# 1.	Data Storage and Manipulation:
# o	Use lists to store and manipulate collections of data in applications.
temperatures = [23, 20, 25, 22, 26]

# 2.	Return Multiple Values from Functions:
# o	Use lists to return multiple values from functions.
def calculate_statistics(numbers):
    mean = sum(numbers) / len(numbers)
    median = sorted(numbers)[len(numbers) // 2]
    return [mean, median]
stats = calculate_statistics([1, 2, 3, 4, 5])

# 3.	Stack or Queue Implementations:
# o	Use lists to implement stack (LIFO) or queue (FIFO) structures.
# o	Example: Stack
stack = []
stack.append(1)
stack.append(2)
stack.pop()  # 2

# o	Example: Queue
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()  # 1

# 4.	Temporary Data Storage:
# o	Use lists to temporarily store data that will be processed and then discarded.
buffer = []
for i in range(100):
    buffer.append(i)

# 5.	Grouping Related Data:
# o	Use lists to group related data items together.
# coordinates = [x, y, z]

# When Not to Use Lists
# 1.	Unordered Collections:
# o	Use a set or dictionary if the order of elements does not matter.
unique_items = {"apple", "banana", "cherry"}

# 2.	Fixed-Size Collections:
# o	Use a tuple if you need an immutable, fixed-size collection.
point = (10, 20)

# 3.	Key-Value Pairs:
# o	Use a dictionary if you need to associate keys with values.
person = {"name": "Alice", "age": 25}

# Example: To-Do List Application
# Here's an example that demonstrates using lists in a simple to-do list application:

# Initialize an empty to-do list
todo_list = []

# Function to add a task
def add_task(task):
    todo_list.append(task)

# Function to remove a task by name
def remove_task(task):
    todo_list.remove(task)

# Function to display all tasks
def show_tasks():
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

# Adding tasks
add_task("Write code")
add_task("Test application")
add_task("Deploy application")

# Displaying tasks
show_tasks()

# Removing a task
remove_task("Test application")

# Displaying tasks again
show_tasks()


# Summary
# Use lists when you need an ordered, mutable collection that can hold heterogeneous items and allows duplicates. 
# Lists are suitable for a wide range of applications, from simple data storage to complex data processing tasks. 
# However, consider other data structures like sets, tuples, or dictionaries when the use case requires unique items, immutability, or key-value pairs.
