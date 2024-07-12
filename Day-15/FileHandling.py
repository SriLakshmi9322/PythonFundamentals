# File Handling
"""
Python supports File Handling by allowing users to handle files. i.e, To read &
write a file.
Using python built-in method called open() we can open a specific file we want.
open() - It takes 2 arguements : 1. file name 2. File Mode (Optional)
File Modes : By Default Python considers 'r' which is of read mode.
1. 'r' - for reading an existing file.
2. 'w' - for writing into an existing file if file not exists it will create a
         new one.
3. 'a' - for appending new information into an existing file.  It won't
         override existing data.
4. 'r+' -  To read and write data into the file. This mode does not override
           the existing data, but you can modify the data starting from the
           beginning of the file.
5. 'w+' - To write and read data. It overwrites the previous file if one
          exists, it will truncate the file to zero length or create a file if
          it does not exist.
6. 'a+' - To append and read data from the file. It won't override existing
          data.
"""

# 1. Python File Open
# Working in Read mode
# Working of open() function :
file = open('demo.txt')             # Default 'r' mode

# To print each line one by one from the file.
for each_line in file:
    print(each_line)

# Output :
# Hello

# Welcome to Python Programming World

# This is my first File Handling demo file

# Example-2 :
"""
To extract a string that contains all characters in the Python file we can
use file.read().
"""
file = open("demo.txt", 'r')

print(file.read())

# Output :
# Hello
# Welcome to Python Programming World
# This is my first File Handling demo file

# Example-3 : Reading a file using 'with statement'.
with open("demo.txt", 'r') as f:
    data = f.read()

print(data)

# Output :
# Hello
# Welcome to Python Programming World
# This is my first File Handling demo file

# Example-4 :
"""
Another way to read a file is to call a certain number of characters.
To read the first five characters of stored data and return it as a string.
"""
file = open("demo.txt", 'r')
print(file.read(5))

# Output : Hello

# Example-5 :
"""
We can also split lines while reading files in Python. The split() function
splits the variable when space is encountered. You can also split using any
characters as you wish.
"""
with open("demo.txt", 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

# Output :
# ['Hello']
# ['Welcome', 'to', 'Python', 'Programming', 'World']
# ['This', 'is', 'my', 'first', 'File', 'Handling', 'demo', 'file']


# 2. Creating a File using the write() Function.
# Working in Write mode
# Example-1 :
"""
the write() function is used to write in a file. The close() command
terminates all the resources in use and frees the system of this particular
program.
"""
file = open("NewFile.txt", 'w')
file.write("File Created\n")
file.write("File Currently in Write mode\n")
file.write("To stop write mode we can use close() function")
file.close()

# Example-2 : Using 'with statement'.
with open('AnotherNewFile.py', 'w') as fl:
    fl.write("print('Hello World!!!')\n")


# 3. Working of Append mode
file = open("NewFile.txt", 'a')
file.write("\n\nNew Information Appended to the File")
position = file.tell()
print(position)
file.close()


"""
There are also various other commands in Python file handling that are used to
handle various tasks:

1. rstrip(): This function strips each line of a file off spaces from the
             right-hand side.
2. lstrip(): This function strips each line of a file off spaces from the
             left-hand side.
It is designed to provide much cleaner syntax and exception handling when you
are working with code.

In Python, files can broadly be categorized into two types based on their mode
of operation:

1. Text Files: These store data in plain text format. Examples include .txt
   files.
2. Binary Files: These store data in binary format, which is not
   human-readable. Examples include images, videos, and executable files.


The four primary functions used for file handling in Python are:

1. open(): Opens a file and returns a file object.
2. read(): Reads data from a file.
3. write(): Writes data to a file.
4. close(): Closes the file, releasing its resources.
5. tell(): returns the current position of the file pointer (cursor) within
   the file.
"""
