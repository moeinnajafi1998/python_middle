# Sets in Python are unordered collections of unique elements. 
# They are defined by enclosing elements within curly braces {} and can contain any immutable data type (numbers, strings, tuples). 
# Sets are particularly useful for tasks that involve unique items, membership testing, and mathematical operations like union, intersection, and difference. 
# Here’s a comprehensive look at sets and their operations:

# Creating Sets
# 1.	Empty set:
empty_set = set()

# 2.	Non-empty set:
fruits = {"apple", "banana", "cherry"}

# 3.	Using the set constructor:
vowels = set("aeiou")

# Adding and Removing Elements
# 1.	Adding elements:
fruits.add("orange")

# 2.	Removing elements:
fruits.remove("banana")

# Set Operations
# 1.	Membership test:
"apple" in fruits

# 2.	Set operations: Union, Intersection, Difference, Symmetric Difference
# o	Union: Elements present in either set.
# set1.union(set2)

# o	Intersection: Elements present in both sets.
# set1.intersection(set2)

# o	Difference: Elements present in the first set but not in the second.
# set1.difference(set2)

# o	Symmetric Difference: Elements present in either set, but not in both.
# set1.symmetric_difference(set2)

# Set Methods
# 1.	add() method:
# o	Adds an element to the set.
fruits.add("grape")

# 2.	remove() method:
# o	Removes a specified element from the set. Raises KeyError if element is not found.
fruits.remove("cherry")

# 3.	discard() method:
# o	Removes a specified element from the set if it is present.
fruits.discard("banana")

# 4.	clear() method:
# o	Removes all elements from the set.
fruits.clear()

# 5.	copy() method:
# o	Returns a shallow copy of the set.
fruits_copy = fruits.copy()

# Iterating Through Sets
# Sets are iterable, and you can loop through them to access each element:
for fruit in fruits:
    print(fruit)

# Example Use Cases
# Example 1: Checking Membership
# Checking membership in a set
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)  # True
print("orange" in fruits)  # False

# Example 2: Performing Set Operations
# Set operations: Union, Intersection, Difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Union
print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection
print(set1.intersection(set2))  # {4, 5}
# Difference
print(set1.difference(set2))  # {1, 2, 3}

# Example 3: Adding and Removing Elements
# Adding and removing elements from a set
fruits = {"apple", "banana", "cherry"}
# Adding an element
fruits.add("orange")
print(fruits)  # {"apple", "banana", "cherry", "orange"}
# Removing an element
fruits.remove("banana")
print(fruits)  # {"apple", "cherry", "orange"}

# Example 4: Iterating Through a Set
# Iterating through a set
vowels = {"a", "e", "i", "o", "u"}
for vowel in vowels:
    print(vowel)

# Use Cases for Sets
# 1.	Removing Duplicates:
# o	Use sets to remove duplicate elements from a list or sequence.
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = set(names)

# 2.	Membership Testing:
# o	Quickly check if an element exists in a collection without iterating through the entire collection.
allowed_users = {"Alice", "Bob", "Charlie"}
user = "Alice"
if user in allowed_users:
    print("Access granted")

# 3.	Mathematical and Statistical Operations:
# o	Use sets for operations like union, intersection, and difference, which are fundamental in various computational tasks.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)

# 4.	Finding Unique Elements:
# o	Determine unique items in a dataset or sequence.
words = {"apple", "banana", "apple", "cherry"}
unique_words = set(words)

# 5.	Set Operations in Database Queries:
# o	Sets can be used to represent query results and perform set operations efficiently in database applications.
# Example could involve querying database results and performing set operations

# Summary
# Sets in Python are valuable for managing collections of unique elements, performing efficient membership tests, and conducting mathematical operations. 
# They provide a straightforward way to ensure uniqueness and simplify various computational tasks. 
# Understanding when and how to use sets can greatly enhance the clarity and efficiency of your Python programs,
# especially in scenarios where uniqueness and efficient data access are paramount.

# Where should we use sets?
# Sets in Python are particularly useful in scenarios where you need to manage collections of unique elements and perform operations like membership testing, 
# intersection, union, and difference efficiently. Here are some specific situations where sets are commonly used:
# 1. Removing Duplicates
# Sets are ideal for removing duplicate elements from a collection while preserving the uniqueness of items:
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = set(names)
print(unique_names)  # {"Alice", "Bob", "Charlie"}

# 2. Membership Testing
# Sets provide average O(1) time complexity for membership tests, making them efficient for checking if an element exists in a collection:
allowed_users = {"Alice", "Bob", "Charlie"}
user = "Alice"
if user in allowed_users:
    print("Access granted")

# 3. Mathematical Operations
# Sets support mathematical operations like union, intersection, difference, and symmetric difference, which are useful in various computational tasks:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Union
print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection
print(set1.intersection(set2))  # {4, 5}
# Difference
print(set1.difference(set2))  # {1, 2, 3}
# Symmetric Difference
print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}

# 4. Data Analysis and Statistics
# Sets are useful for data analysis tasks where you need to find unique items or perform set operations on datasets:
# Finding unique words in a text
text = "hello world hello python world"
unique_words = set(text.split())
print(unique_words)  # {"hello", "world", "python"}

# 5. Handling Unordered Data
# When the order of elements does not matter, sets can be used to efficiently manage and manipulate data without concern for sequence:
# Managing unique tags associated with a blog post
tags = {"python", "programming", "tutorial", "python"}
print(tags)  # {"python", "programming", "tutorial"}

# 6. Checking for Subsets and Supersets
# Sets allow for easy checking of subsets and supersets, which is helpful in many algorithmic and computational tasks:
set1 = {1, 2, 3}
set2 = {1, 2}
# Checking if set2 is a subset of set1
if set2.issubset(set1):
    print("set2 is a subset of set1")
# Checking if set1 is a superset of set2
if set1.issuperset(set2):
    print("set1 is a superset of set2")

# 7. Set Operations in Database Applications
# In database applications, sets can be used to represent query results and perform set operations efficiently:

# Example could involve querying database results and performing set operations
# Conclusion
# Sets in Python provide a powerful way to handle collections of unique elements and perform efficient operations like membership testing, 
# set arithmetic, and uniqueness checks. They are particularly valuable in scenarios where uniqueness and efficient data manipulation are key requirements. 
# By leveraging sets effectively, you can simplify your code and improve the performance of operations that involve managing collections of data.
