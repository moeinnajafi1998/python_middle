# what are *args and **kargs in python
# In Python, *args and **kwargs are used to pass a variable number of arguments to a function. They allow you to write more flexible and reusable code.
# *args
# •	*args allows you to pass a variable number of non-keyword arguments to a function.
# •	It collects the additional positional arguments passed to the function and stores them in a tuple.
# Here’s an example:
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3, "hello")
# In this example, args will be a tuple containing (1, 2, 3, "hello"), and the function will print each of these values.

# **kwargs
# •	**kwargs allows you to pass a variable number of keyword arguments to a function.
# •	It collects the additional keyword arguments passed to the function and stores them in a dictionary.
# Here’s an example:
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30, job="Engineer")
# In this example, kwargs will be a dictionary containing {'name': 'Alice', 'age': 30, 'job': 'Engineer'}, and the function will print each key-value pair.

# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function definition to accept both positional and keyword arguments:
def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_function(1, 2, 3, name="Alice", age=30)
# In this example:
# •	args will be (1, 2, 3)
# •	kwargs will be {'name': 'Alice', 'age': 30}
# Order of Parameters
# When defining a function with *args and **kwargs, the order of parameters should be:
# 1.	Standard arguments
# 2.	*args
# 3.	**kwargs
# Here’s an example:
def my_function(arg1, arg2, *args, **kwargs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
my_function(1, 2, 3, 4, 5, name="Alice", age=30)
# In this example:
# •	arg1 will be 1
# •	arg2 will be 2
# •	args will be (3, 4, 5)
# •	kwargs will be {'name': 'Alice', 'age': 30}
# Using *args and **kwargs makes your functions very flexible and able to handle a wide range of input arguments.