# FileNotFoundError
"""
FileNotFoundError: FileNotFoundError is an exception in Python that is raised
                   when a program tries to access a file that doesn't exist.
                   This error typically occurs when you attempt to perform file
                   operations like opening, reading, writing, or deleting a
                   file. Python cannot find the specified file at the provided
                   path or location.
"""

# Example-1 :
file = open("NonExistingFile.txt")  # 'NonExistingFile.txt' does not exists.

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-16\tempCodeRunnerFile.py",
# line 12, in <module>
#     file = open("NonExistingFile.txt")
# FileNotFoundError: [Errno 2] No such file or directory: 'NonExistingFile.txt'

# Solution-1 : We need to make sure that the file on which we are performing
# Operations exists or the path we are giving is correct.

file = open("demo.txt")         # 'demo.txt' file exists

# Solution-2 : We can use 'try-except' blocks.
try:
    file = open("NonExistingFile.txt")
except FileNotFoundError:
    print("Error: File you specified does not exists...")

# Output :
# Error: File you specified does not exists...

# Example-2 :
file = open("path/to/directory")

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-16\tempCodeRunnerFile.py",
# line 2, in <module>
#     file = open("path/to/directory")
# FileNotFoundError: [Errno 2] No such file or directory: 'path/to/directory'

# Solution : It accepts files only so we need to make sure to specify file
# name instead of giving them a directory or wrong path.
