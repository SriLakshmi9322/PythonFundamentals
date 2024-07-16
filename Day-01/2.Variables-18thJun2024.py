"""
Variables -Variables are nothing but reserved memory locations to store values.
Python do not need explicit declaration to reserve memory space.
The declaration happens automatically when you assign a value to the variables.
The equal sign (=) is used to assign values to variables.
The operand to the left of the = operator is the name of the variable and the
operand to the right of the = operator is the value stored in the variable.
"""

# Example
counter = 100           # An integer assignment
miles = 1000.0          # A floating point
name = "John"           # A string

print(counter)          # 100
print(miles)            # 1000.0
print(name)             # John

# Multiple Assignment
a = b = c = 10
print(a, b, c)            # 10 10 10

x, y, z = 10, 20, "John"
print(x, y, z)            # 10 20 John

"""
Python Comments - Comments are descriptions that help programmers better
understand the intent and functionality of the Program.
It is Completely ignored by the Python Interpreter."""
# 1. # - for Single-Line Comments
print("Hello World.!!")             # Printing a String

'''
2. ''' ''' - for Multi-Line Comments.
I am a
Multi-Line Comment
'''
print("Hello World.!!")
