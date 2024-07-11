# Exceptions : Handling Errors in Python Program
"""
Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors
are problems in a program due to which the program will stop the execution. On
the other hand, exceptions are raised when some internal events occur which
change the normal flow of the program.

Different types of exceptions in python:
In Python, there are several built-in Python exceptions that can be raised
when an error occurs during the execution of a program.

1. SyntaxError
2. TypeError
3. NameError
4. IndexError
5. KeyError
6. ValueError
7. AttributeError
8. IOError
9. ZeroDivisionError: This exception is raised when an attempt is made to
   divide a number by zero.
10. ImportError: This exception is raised when an import statement fails to
    find or load a module.

Instead of Program crash we can handle the situation & Print proper Error
Message. To make this possible we use 'try' and 'except' blocks.

Try and except statements are used to catch and handle exceptions in Python.
Statements that can raise exceptions are kept inside the try clause and the
statements that handle the exception are written inside except clause.
"""

# Example-1 :
age = int(input("Enter your Age : "))

print(age)

# Output-1 :
# Enter your Age : 21
# 21

# Output-2 :
# Enter your Age : Twenty
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 44, in <module>
#     age = int(input("Enter your Age : "))
# ValueError: invalid literal for int() with base 10: 'Twenty'

# To Solve the above program crash we use 'try' & 'except' blocks
# Solution :
try:
    age = int(input("Enter Your Age : "))
    print(age)
except ValueError:
    print("Invalid Value...")

# Output :
# Enter Your Age : Twenty One
# Invalid Value...


# Example-2 :
try:
    age = int(input("Enter Your Age : "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid Value...")

# Output :
# Enter Your Age : 0
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 5, in <module>
#     risk = income / age
# ZeroDivisionError: division by zero

# To Solve above problem We can use the concept of 'Multiple Except Blocks'
try:
    sal_package = int(input("Enter your Salary package : "))
    experience = int(input("Enter the no. of months been in your new job : "))
    age = int(input("Enter Your Age : "))
    sal_earned = sal_package / experience
    print(sal_earned)
    print(f"You are {age} old! and you have earned {sal_earned} until now.!!")
except ValueError:
    print("Invalid Value...")
except ZeroDivisionError:
    print("Age Cannot be Zero...")

# Output-1 : Normal Execution
# Enter your Salary package : 1200000
# Enter the no. of months been in your new job : 3
# Enter Your Age : 21
# 400000.0
# You are 21 old! and you have earned 400000.0 until now.!!

# Output-2 : When ZeroDivisionError Occurs
# Enter your Salary package : 1200000
# Enter the no. of months been in your new job : 0
# Enter Your Age : 21
# Age Cannot be Zero...

# Output-3 : When ValueError Occurs
# Enter your Salary package : 1200000
# Enter the no. of months been in your new job : 2
# Enter Your Age : Twenty One
# Invalid Value...
