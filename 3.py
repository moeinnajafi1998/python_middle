# Dictionaries in Python are versatile data structures used to store key-value pairs. 
# They are unordered, mutable, and allow for efficient lookups and modifications. 
# Here's a comprehensive look at dictionary operations and usage:

# Creating Dictionaries
# 1.	Empty dictionary:
empty_dict = {}

# 2.	Non-empty dictionary:
person = {"name": "Alice", "age": 30, "city": "New York"}

# 3.	Using the dict constructor:
person = dict(name="Alice", age=30, city="New York")

# Accessing Elements
# 1.	Accessing by key:
name = person["name"]  # "Alice"

# 2.	Using get() method (to avoid KeyError if key is not present):
age = person.get("age")  # 30

# Modifying Dictionaries
# 1.	Adding or updating an element:
person["email"] = "alice@example.com"  # Add new key-value pair
person["age"] = 31  # Update existing value

# 2.	Removing an element:
del person["city"]  # Remove a specific key-value pair

# 3.	Clearing all elements:
person.clear()  # Remove all items

# Dictionary Operations
# 1.	Checking membership:
"name" in person  # Check if key exists

# 2.	Length of a dictionary:
len(person)  # Number of key-value pairs

# 3.	Copying dictionaries:
new_person = person.copy()  # Shallow copy of the dictionary

# Iterating Through a Dictionary
# 1.	Iterating through keys:
for key in person:
    print(key, person[key])

# 2.	Iterating through key-value pairs:
for key, value in person.items():
    print(key, value)

# Dictionary Methods
# 1.	keys() method:
# o	Returns a view of all keys in the dictionary.
keys = person.keys()

# 2.	values() method:
# o	Returns a view of all values in the dictionary.
values = person.values()

# 3.	items() method:
# o	Returns a view of all key-value pairs (tuples) in the dictionary.
items = person.items()

# Example Usage
# Example 1: Basic Operations

# Creating a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing elements
print(person["name"])  # Accessing by key

# Modifying dictionary
person["email"] = "alice@example.com"  # Adding a new key-value pair
del person["age"]  # Removing a key-value pair

# Iterating through dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Example 2: Dictionary Methods

# Dictionary methods
keys = person.keys()  # Get all keys
values = person.values()  # Get all values
items = person.items()  # Get all key-value pairs

# Iterating through keys
for key in keys:
    print(key)

# Iterating through values
for value in values:
    print(value)

# Iterating through items (key-value pairs)
for key, value in items:
    print(f"{key}: {value}")

# Example 3: Checking Membership

# Checking membership
if "email" in person:
    print("Email exists:", person["email"])
else:
    print("Email not found")

# Use Cases for Dictionaries
# 1.	Storing Related Information:
# o	Dictionaries are ideal for storing and retrieving related information based on keys.
person = {"name": "Alice", "age": 30, "city": "New York"}

# 2.	Configurations and Settings:
# o	Use dictionaries to store configurations or settings for applications.
config = {"debug_mode": True, "max_connections": 10}

# 3.	Database-Like Operations:
# o	Dictionaries can simulate database operations by storing records with unique keys.
users = {
    "user1": {"name": "Alice", "age": 30},
    "user2": {"name": "Bob", "age": 25}
}

# 4.	Caching and Memoization:
# o	Use dictionaries to cache results of expensive computations based on input parameters (memoization).
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

# 5.	Mapping Keys to Values:
# o	Dictionaries are fundamental for mapping keys to corresponding values efficiently.
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

# Summary
# Dictionaries in Python are versatile and powerful data structures used to store and retrieve key-value pairs efficiently. 
# They are suitable for a wide range of applications including storing configurations, database-like operations, caching, and more. 
# Understanding dictionary operations and methods allows you to leverage dictionaries effectively in your Python programs.

# where should we use dictionaries?
# Dictionaries in Python are incredibly useful and versatile data structures that can be applied in various scenarios where key-value mappings are beneficial. 
# Here are some common situations where dictionaries shine:
# 1. Mapping Relationships and Attributes
# Dictionaries are ideal for mapping relationships between entities or for storing attributes associated with a particular entity. For example:

# Mapping student names to their grades
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
# Storing attributes of a person
person = {"name": "Alice", "age": 30, "city": "New York"}

# 2. Fast Lookups
# Dictionaries provide average O(1) time complexity for lookups, making them efficient for scenarios where quick access to data based on a key is required. 
# This is useful in applications such as:
# Checking if a user has access to a resource
user_permissions = {"Alice": "admin", "Bob": "user", "Charlie": "moderator"}

# 3. Storing Configuration Settings
# Dictionaries are commonly used to store configuration settings for applications or systems. This allows easy customization and adjustment without modifying the code itself:
# Application configuration settings
config = {
    "debug_mode": True,
    "max_connections": 10,
    "timeout": 30
}

# 4. Database-Like Operations
# In scenarios where data needs to be organized and accessed based on unique keys, dictionaries can mimic basic database operations:
# Storing user profiles with unique IDs
user_profiles = {
    1001: {"name": "Alice", "age": 30},
    1002: {"name": "Bob", "age": 25},
    1003: {"name": "Charlie", "age": 35}
}

# 5. Caching and Memoization
# Dictionaries are often used for caching computed results to improve performance by avoiding redundant calculations:
# Memoizing results of expensive computations
cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

# 6. Counting and Grouping
# Dictionaries are effective for counting occurrences or grouping items based on certain criteria:
# Counting occurrences of words in a text
text = "hello world hello python world"
word_count = {}
for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
# Output: {'hello': 2, 'world': 2, 'python': 1}

# 7. Handling Responses and API Data
# When working with APIs or receiving structured data, dictionaries are often used to handle responses and parse data:
# Processing JSON response from an API
import requests

response = requests.get("https://api.example.com/data")
data = response.json()  # Assume data is a dictionary

# 8. Flexibility in Data Representation
# Dictionaries provide flexibility in representing complex or nested data structures, allowing for easy navigation and manipulation:
# Representing a nested data structure
organization = {
    "name": "XYZ Corp",
    "departments": {
        "HR": ["Alice", "Bob"],
        "IT": ["Charlie", "David"]
    }
}

# Conclusion
# Dictionaries are versatile data structures that offer efficient key-value mappings, fast lookups, 
# and flexibility in data representation. They are essential in scenarios where data needs to be organized, accessed, 
# and manipulated based on unique keys or where attributes need to be associated with entities. 
# Understanding when and how to use dictionaries allows you to design more efficient and organized Python applications.
