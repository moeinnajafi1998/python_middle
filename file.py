# file handling in Python is a fundamental aspect of working with data and storing information persistently. 
# Python provides built-in functions and methods to create, read, write, update, and delete files. 

# Here’s a basic overview:
# Opening a File
# To open a file, you use the open() function, which returns a file object. The basic syntax is:

# file_object = open(filename, mode)

# •	filename is the name of the file you want to open (including the path if it's not in the current directory).
# •	mode specifies how you want to open the file ('r' for reading, 'w' for writing, 'a' for appending, 'r+' for both reading and writing, etc.).
# Reading from a File
# To read the contents of a file, you can use methods like read(), readline(), or readlines() on the file object:

file_object = open('filename.txt', 'r')
content = file_object.read()  # reads the entire file
file_object.close()  # always close the file when done

# Writing to a File
# To write to a file, use the write() method on a file object opened in write or append mode ('w' or 'a'):
file_object = open('filename.txt', 'w')
file_object.write('Hello, world!\n')
file_object.close()

# Closing a File
# It’s important to close the file after you’ve finished working with it to release resources:

# file_object.close()
# Alternatively, you can use a file object within a with statement, which automatically closes the file for you:

with open('filename.txt', 'r') as file_object:
    content = file_object.read()
    # File automatically closed here

# Error Handling
# Always handle potential errors when working with files, especially when opening or writing to them. This can be done using try-except blocks.
# Example: Reading a File Line by Line

try:
    with open('filename.txt', 'r') as file_object:
        for line in file_object:
            print(line.strip())  # strip removes the newline character
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading the file.")

# File Operations and Context Management
# Python’s with statement simplifies the process of opening and closing files, ensuring that resources are properly managed and errors are handled gracefully.
# Is there a specific aspect of file handling you're interested in exploring further?
# ****
# other source

# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.
# ________________________________________
# File Handling
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
# ________________________________________
# Syntax
# To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")
# The code above is the same as:
f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
# Note: Make sure the file exists, or else you will get an error.
# Open a File on the Server
# Assume we have the following file, located in the same folder as Python:
# demofile.txt
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!
# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:
# ExampleGet your own Python Server
f = open("demofile.txt", "r")
print(f.read())
# Run Example »
# If the file is located in a different location, you will have to specify the file path, like this:
# Example
# Open a file on a different location:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
# Run Example »
# ________________________________________
# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# Example
# Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))

# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
# ExampleGet your own Python Server
# Open the file "demofile2.txt" and append content to the file:
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
# Run Example »
# Example
# Open the file "demofile3.txt" and overwrite the content:
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
# Run Example »
# Note: the "w" method will overwrite the entire file.
# ________________________________________
# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist
# Example
# Create a file called "myfile.txt":
f = open("myfile.txt", "x")
# Result: a new empty file is created!
# Example
# Create a new file if it does not exist:
f = open("myfile.txt", "w")
# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
# ExampleGet your own Python Server
# Remove the file "demofile.txt":
import os
os.remove("demofile.txt")
# ________________________________________
# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
# Example
# Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
# ________________________________________
# Delete Folder
# To delete an entire folder, use the os.rmdir() method:
# Example
# Remove the folder "myfolder":
import os
os.rmdir("myfolder")
# Note: You can only remove empty folders.