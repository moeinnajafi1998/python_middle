# Modules and packages in Python are a way to structure code, promote code reusability, 
# and maintainability by organizing Python code into separate files and directories. 
# This enables better management of larger programs by breaking them down into smaller, logical pieces.

# a) Importing Modules
# A module is simply a Python file that contains Python definitions and statements, such as functions, variables, or classes. 
# You can use any Python module in another program by importing it.

# 1. Importing Entire Modules
# To import a module, use the import statement. This makes the entire module available in your script.
import math
print(math.sqrt(16))  # 4.0

# 2. Importing Specific Components from a Module
# You can import specific functions, classes, or variables from a module using the from keyword.
from math import sqrt, pi
print(sqrt(9))  # 3.0
print(pi)       # 3.141592653589793

# 3. Importing with Aliases
# You can also use as to give an imported module or component an alias, which can shorten names or avoid conflicts.
import math as m
print(m.sqrt(25))  # 5.0

# 4. Importing All Components from a Module
# Using from module import * imports all functions, variables, and classes from a module. 
# This is generally discouraged because it can lead to namespace collisions (i.e., two variables/functions having the same name).
from math import *
print(sqrt(49))  # 7.0

# b) Standard Library Modules
# Python has a rich set of standard library modules, which come pre-installed and 
# provide various functionalities like math operations, date manipulations, random number generation, etc.
# 1. math Module
# The math module provides access to many mathematical functions and constants.
# Common Functions:
import math
print(math.sqrt(16))  # 4.0
print(math.factorial(5))  # 120
print(math.pow(2, 3))  # 8.0
print(math.pi)  # 3.141592653589793

# 2. random Module
# The random module is used to generate pseudo-random numbers.
# Common Functions:
import random
print(random.random())  # Random float: 0.0 <= x < 1.0
print(random.randint(1, 10))  # Random integer between 1 and 10 (inclusive)
print(random.choice(['apple', 'banana', 'cherry']))  # Randomly selects from list

# 3. datetime Module
# The datetime module allows you to work with dates and times in Python.
# Common Functions:
import datetime
now = datetime.datetime.now()
print(now)  # e.g., 2024-10-06 14:35:10.123456
today = datetime.date.today()
print(today)  # e.g., 2024-10-06
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Formatted date and time

# c) Creating and Using Custom Modules
# You can create your own modules by saving Python code into a file and then importing that file into other Python scripts.
# 1. Creating a Custom Module
# Example:
# Create a Python file named my_module.py.
# 2. Using the Custom Module
# Now you can import and use this module in another script:
# main.py
import my_module
print(my_module.greet("Alice"))  # Hello, Alice!
print(my_module.add(3, 5))  # 8

# 3. Module Search Path
# When importing a module, Python searches in the following locations:
# The current directory.
# The directories listed in the PYTHONPATH environment variable.
# The installation-dependent default directories (like the standard library).
# You can check the search path with:
import sys
print(sys.path)

# 4. Using if __name__ == "__main__"
# When a Python file is run directly, the __name__ variable is set to "__main__". 
# You can use this to define behavior that only runs when the file is executed directly, and not when it’s imported as a module.

# my_module.py

# def greet(name):
#     return f"Hello, {name}!"

# if __name__ == "__main__":
#     print(greet("John"))  # This will only run if the file is executed directly.


# d) Packages
# A package is a way of organizing related modules into a directory hierarchy. 
# A package is simply a directory that contains an __init__.py file (which can be empty), and one or more module files.

# 1. Creating a Package
# For example, if you want to create a package called mypackage with two modules, module1.py and module2.py, the structure would look like this:

# mypackage/
#     __init__.py  # This makes 'mypackage' a package
#     module1.py
#     module2.py

# 2. Using a Package
# To use a module from the package, you can import it using dot notation:

# from mypackage import module1
# import mypackage.module2 as m2
# module1.some_function()
# m2.another_function()

# 3. __init__.py
# The __init__.py file can be empty, or it can initialize the package by defining what should be imported when import mypackage is called.
# For example:

# mypackage/__init__.py
# from .module1 import some_function
# from .module2 import another_function
# Now you can import the package like this:
# import mypackage
# mypackage.some_function()
# mypackage.another_function()

# Summary:
# Modules: Single Python files that contain functions, variables, classes, etc. They can be imported into other Python scripts.
# Standard Library Modules: Python comes with built-in modules like math, random, and datetime that provide a variety of functionalities.
# Custom Modules: You can create your own modules by saving Python code in .py files and importing them into other scripts.
# Packages: A collection of modules organized into directories. A package must contain an __init__.py file.
# By organizing your Python code into modules and packages, you promote code reuse, make it easier to manage larger projects, and keep your codebase clean and efficient.