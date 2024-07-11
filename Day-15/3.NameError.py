# NameError
"""
NameError: This exception is raised when a variable or function name is not
           found in the current scope.
"""

# Example-1 : When Variable name is not defined.
name = "SriLakshmi Tiramsetti"

print(f"My name is {name} and I am {age} years old!")

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 3, in <module>
#     print(f"My name is {name} and I am {age} years old!")
# NameError: name 'age' is not defined

# Solution : To solve the above program from Crashing, We need to make sure the
# variable named 'age' exists.

name = "SriLakshmi Tiramsetti"
age = 21

print(f"My name is {name} and I am {age} years old!")

# Output :
# My name is SriLakshmi Tiramsetti and I am 21 years old!

# Similarly, the same error can be raised when we misspell a variable name.


# Example-2 : When Function name is not defined.
def sayHello():
    print("Hello World!!!")


sayHelloo()

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
#   line 6, in <module>
#     sayHelloo()
# NameError: name 'sayHelloo' is not defined

# Solution : Make sure to spell the function name properly and make sure the
# called function do exists.


def sayHello1():
    print("Hello World!!!")


sayHello1()                  # Hello World!!!


# Example-3 : Using a module without importing.
x = 5.5

print(math.ceil(x))

# Solution : We must first import the module first before using it.
import math

x = 5.5
print(math.ceil(x))                 # 6
