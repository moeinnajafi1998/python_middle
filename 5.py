# String operations in Python are powerful and flexible, allowing you to manipulate text data in various ways. Here’s a summary of the most common string operations:

# 1. String Creation and Basic Operations
# Creating a string:
my_string = "Hello, World!"

# Accessing characters: You can access individual characters using indexing, with indices starting at 0.
first_char = my_string[0]  # 'H'
last_char = my_string[-1]  # '!'

# String length: Use len() to get the length of a string.
length = len(my_string)  # 13

# 2. Slicing Strings
# Slicing allows you to extract parts of a string.
substring = my_string[0:5]  # 'Hello'
substring = my_string[:5]   # 'Hello'
substring = my_string[7:]   # 'World!'
substring = my_string[-6:]  # 'World!'

# 3. String Concatenation and Repetition
# Concatenation: Combine strings using the + operator.
greeting = "Hello" + ", " + "World!"
# Repetition: Repeat strings using the * operator.
repeat = "Hi! " * 3  # 'Hi! Hi! Hi! '

# 4. String Methods
# Python strings come with many useful methods. Here are a few:
# upper() / lower(): Converts all characters to uppercase/lowercase.
"hello".upper()  # 'HELLO'
"HELLO".lower()  # 'hello'

# strip(): Removes leading and trailing whitespace (or specific characters).
"  hello  ".strip()  # 'hello'

# replace(): Replace occurrences of a substring.
"hello world".replace("world", "Python")  # 'hello Python'

# split(): Splits a string into a list based on a delimiter.
"a,b,c".split(",")  # ['a', 'b', 'c']

# join(): Joins a list of strings into a single string.
",".join(["a", "b", "c"])  # 'a,b,c'

# startswith() / endswith(): Checks if a string starts/ends with a certain substring.
"hello".startswith("he")  # True
"hello".endswith("lo")    # True

# 5. String Formatting
# Python provides several ways to format strings:
# Old-style formatting (using %):
"Hello, %s!" % "World"  # 'Hello, World!'

# str.format() method:
"Hello, {}!".format("World")  # 'Hello, World!'

# f-strings (Python 3.6+):
name = "World"
f"Hello, {name}!"  # 'Hello, World!'

# 6. Escape Characters
# Special characters can be included in strings using backslashes:
# \n: New line
# \t: Tab
# \' or \"**: Single or double quote
# Example:
print("Line 1\nLine 2")

# 7. String Searching
# find(): Returns the index of the first occurrence of a substring, or -1 if not found.
"hello world".find("world")  # 6

# in: Checks if a substring exists in the string.
"world" in "hello world"  # True

# 8. Case Conversion
# capitalize(): Capitalizes the first letter.
"hello".capitalize()  # 'Hello'

# title(): Capitalizes the first letter of each word.
"hello world".title()  # 'Hello World'

# swapcase(): Swaps the case of all characters.
"Hello".swapcase()  # 'hELLO'

# 9. String Immutability
# Strings in Python are immutable, which means once created, they cannot be changed. Any operation that modifies a string will return a new string.
my_string = "Hello"
new_string = my_string.replace("H", "J")  # 'Jello'