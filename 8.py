# Generators and iterators in Python are powerful tools that allow for efficient handling of data, especially in the context of large datasets or infinite sequences. 
# They enable lazy evaluation, meaning values are produced only when needed, saving memory and improving performance.

# 1. Iterators in Python
# An iterator is an object that represents a stream of data. 
# It provides a way to access elements of a collection (like lists, tuples, etc.) one at a time, without loading the entire collection into memory. 
# Iterators implement two methods:

# __iter__(): Returns the iterator object itself.
# __next__(): Returns the next element from the collection. 
# When there are no more elements to return, it raises a StopIteration exception.

# Example of an Iterator:
# You can create an iterator from any iterable using the iter() function.
my_list = [1, 2, 3, 4]
iterator = iter(my_list)
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # 4
# next(iterator)  # Raises StopIteration since no more items are left

# 2. Generators in Python
# A generator is a special kind of iterator that is defined using a function rather than a class. 
# Instead of returning all the values at once, a generator "yields" values one at a time as they are requested, allowing for efficient memory usage. 
# Generators are written using the yield keyword.

# Key Differences Between Generators and Iterators:
# Iterators are typically created through classes by implementing __iter__() and __next__() methods.
# Generators simplify the process, as Python automatically implements the iterator protocol for you when using the yield keyword.

# 3. Creating Generators
# Generators can be created in two ways:

# a) Generator Functions:
# A generator function looks like a normal function but uses yield instead of return. When the function is called, 
# it doesn’t execute immediately; instead, it returns a generator object that can be iterated over.

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
# The yield statement pauses the function, saving its state, and resumes from where it left off when the generator is called again.

# b) Generator Expressions:
# Generator expressions are similar to list comprehensions but use parentheses () instead of square brackets []. 
# This creates a generator instead of a list, meaning it doesn't compute all values at once.
gen = (x ** 2 for x in range(5))
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4

# 4. Advantages of Generators
# Memory Efficiency: Generators produce items one by one, so they don’t require the memory that a complete list or other collection does.
# A list comprehension
lst = [x**2 for x in range(1000000)]  # This holds 1 million elements in memory.
# A generator expression
gen = (x**2 for x in range(1000000))  # No memory issues as it produces values lazily.
# Infinite Sequences: You can create infinite sequences with generators since they don’t compute all values upfront.
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

infinite_gen = infinite_sequence()
print(next(infinite_gen))  # 0
print(next(infinite_gen))  # 1
print(next(infinite_gen))  # 2

# Pipelining Generators: Generators can be used in pipelines to process large datasets in a memory-efficient way.
def square(numbers):
    for n in numbers:
        yield n * n

def double(numbers):
    for n in numbers:
        yield n * 2

nums = range(10)
pipeline = double(square(nums))
print(list(pipeline))  # Output: [0, 2, 8, 18, 32, 50, 72, 98, 128, 162]

# 5. Using yield from in Generators
# The yield from statement allows a generator to delegate part of its operations to another generator. 
# This simplifies the code when you want to yield all values from another iterable or generator.
def generator1():
    yield from range(3)

def generator2():
    yield from generator1()
    yield "End"

for value in generator2():
    print(value)
# Output: 0, 1, 2, End

# 6. Generator Methods
# Generator objects have three methods:
# next(): Resumes the generator and retrieves the next value.
# send(value): Sends a value to the generator, resuming its execution and possibly influencing its behavior. The value becomes the result of the current yield expression.
# throw(exception): Raises an exception inside the generator at the point where it is currently paused.
# close(): Stops the generator by raising a GeneratorExit exception.

# 7. Example: Fibonacci Sequence Generator
# Here’s an example of a generator function to generate Fibonacci numbers:
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
print(next(fib_gen))  # 0
print(next(fib_gen))  # 1
print(next(fib_gen))  # 1
print(next(fib_gen))  # 2
print(next(fib_gen))  # 3

# 8. Example: Chaining Generators
# You can also chain multiple generators together for data processing:
def generate_numbers():
    for i in range(1, 6):
        yield i

def square_numbers(numbers):
    for n in numbers:
        yield n * n

def cube_numbers(numbers):
    for n in numbers:
        yield n * n * n

numbers = generate_numbers()
squared = square_numbers(numbers)
cubed = cube_numbers(squared)

for number in cubed:
    print(number)
# Output: 1, 64, 729, 4096, 15625 (cube of the squared numbers)

# 9. Differences Between Generators and Iterators


# Feature	Iterators	Generators => img
