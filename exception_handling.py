# Exception Handling in Python
# In Python, exception handling allows you to gracefully manage errors that occur during the execution of a program. 
# Instead of crashing your program, you can catch exceptions, handle them appropriately, 
# and continue execution. Python uses try, except, else, finally, and raise for this purpose.

# a) Understanding Exceptions
# An exception is an error that occurs during the execution of a program. When such an error occurs,
# Python stops executing the program and raises an exception. If not handled properly, it results in a traceback and the termination of the program.

# Common Exceptions:
# ZeroDivisionError: Raised when a division by zero is attempted.
# TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# ValueError: Raised when a function receives an argument of the correct type but inappropriate value.
# IndexError: Raised when accessing a list with an out-of-range index.
# KeyError: Raised when trying to access a dictionary with a non-existent key.

# b) Using try, except, finally, and else Blocks
# The most common structure for exception handling is the try-except block. 
# You can catch specific exceptions or all exceptions, handle them accordingly, and use finally for cleanup.

# 1. try and except Blocks
# The try block contains code that might raise an exception, and the except block defines how to handle the exception.
try:
    x = 10 / 0  # Division by zero will raise an exception
except ZeroDivisionError:
    print("Cannot divide by zero!")
# If the code inside the try block raises a ZeroDivisionError, the program will not crash. Instead, the except block will be executed.

# 2. Catching Specific Exceptions
# You can catch specific exceptions by specifying the type of exception.
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
# In this case:

# If the user inputs something that cannot be converted to an integer, a ValueError is caught.
# If the user enters 0, a ZeroDivisionError is caught.

# 3. Catching Multiple Exceptions
# You can handle multiple exceptions in one except block by using a tuple.
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
# Here, both ValueError and ZeroDivisionError are caught by a single except block, and the actual error message is printed using as e.

# 4. else Block
# The else block is executed if no exceptions are raised in the try block.
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("That's not a valid number!")
else:
    print(f"The result is {result}")
# The else block runs only when no exception occurs, ensuring that clean, normal execution follows after the try.

# 5. finally Block
# The finally block is executed no matter what happens, whether an exception is raised or not. It is often used for cleanup actions, like closing files or releasing resources.
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # Ensures the file is closed, even if an exception is raised
# In this example, the file will be closed whether an exception occurs or not.

# c) Raising Exceptions
# You can manually raise an exception using the raise keyword. This is useful when you want to trigger an exception based on certain conditions.

# 1. Raising a Basic Exception
x = -5
if x < 0:
    raise ValueError("x cannot be negative!")
# In this case, if x is negative, a ValueError is raised with a custom message.

# 2. Raising Specific Exceptions
# You can raise any specific exception, including custom ones (more on this below).
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You cannot divide by zero!")
    return a / b
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)
# 3. Creating and Raising Custom Exceptions
# You can define your own exception classes by inheriting from Python’s built-in Exception class.
class CustomError(Exception):
    pass

def check_value(x):
    if x < 0:
        raise CustomError("Negative value is not allowed!")

try:
    check_value(-10)
except CustomError as e:
    print(e)
# Here, CustomError is a user-defined exception, and it behaves just like other Python exceptions.

# Summary of Exception Handling Components

# Example: Full Exception Handling Flow

def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except TypeError:
        print("Both values must be numbers.")
    else:
        print(f"The result is {result}")
    finally:
        print("Execution complete.")

safe_division(10, 2)  # The result is 5.0, Execution complete.
safe_division(10, 0)  # Division by zero is not allowed., Execution complete.
safe_division(10, "a")  # Both values must be numbers., Execution complete.
# In this example:

# try block executes the division.
# except blocks handle specific errors (ZeroDivisionError, TypeError).
# else runs if no exception occurs.
# finally always runs at the end, cleaning up or finishing the execution.
# Best Practices for Exception Handling:
# Catch Specific Exceptions: It’s a good idea to catch specific exceptions instead of using a generic except.
# Avoid Swallowing Exceptions: Do not leave except blocks empty, as it suppresses exceptions without handling them.
# Use finally for Cleanup: Always use finally for cleanup actions like closing files or releasing resources.
# Don’t Overuse Exceptions: Use exceptions for exceptional cases (i.e., errors), not for regular flow control.
# By using exception handling effectively, you can make your Python code more robust and handle unexpected conditions gracefully.