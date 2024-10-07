# A lambda expression in Python is essentially a way to define an anonymous function in a single line. 
# It is called a "lambda expression" because it uses the lambda keyword to create a small, inline function without a formal def statement.
# These expressions are typically used for short, simple operations and are often passed as arguments to higher-order functions like map(), filter(), and sorted().
# Syntax of a Lambda Expression:
# lambda arguments: expression
# lambda: The keyword that defines the anonymous function.
# arguments: A comma-separated list of arguments (like in a normal function).
# expression: A single expression that the lambda function evaluates and returns.
# Example:
# A lambda expression that adds 10 to a given number
lambda x: x + 10
# The equivalent of this lambda expression using a standard function definition would be:
def add_ten(x):
    return x + 10
# Usage Examples:
# 1. Using a Lambda Expression in map():
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
# 2. Using a Lambda Expression in filter():
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
# 3. Using a Lambda Expression in sorted() with custom sorting:
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
# Characteristics of Lambda Expressions:
# Anonymous: Lambda functions do not have a name.
# Single Expression: They can only contain a single expression (no complex statements like loops or multiple return values).
# Used for Short Functions: Commonly used where a small function is needed for a short duration, especially as arguments to other functions.
# Lambda expressions are useful when you need a simple function for a brief purpose and do not want the overhead of formally defining a function with def.