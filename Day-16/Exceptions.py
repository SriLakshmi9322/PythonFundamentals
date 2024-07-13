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
8. FileNotFoundError
9. ZeroDivisionError
10. ImportError

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
except:
    print("Invalid Value...")

# Output :
# Enter Your Age : Twenty One
# Invalid Value...


# Example-2 :
try:
    result = 100 / 0
except ValueError:
    print("Invalid Value...")

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-16\tempCodeRunnerFile.py",
# line 3, in <module>
#     result = 100 / 0
# ZeroDivisionError: division by zero

# To Solve above problem We can use the concept of 'Multiple Except Blocks'
try:
    numerator = int(input("Enter Numerator : "))
    denominator = int(input("Enter Denominator : "))
    age = int(input("Enter Age : "))
    result = numerator / denominator
    print(f"You are {age} old!\nThe result of the division is {result}")
except ValueError:
    print("Invalid Value...")
except ZeroDivisionError:
    print("Denominator Cannot be Zero...")

# Output-1 : Normal Execution
# Enter Numerator : 100
# Enter Denominator : 10
# Enter Age : 21
# You are 21 old!
# The result of the division is 10.0

# Output-2 : When ZeroDivisionError Occurs
# Enter Numerator : 100
# Enter Denominator : 0
# Enter Age : 21
# Denominator Cannot be Zero...

# Output-3 : When ValueError Occurs
# Enter Numerator : 100
# Enter Denominator : 10
# Enter Age : Twenty One
# Invalid Value...


# We can simply catch all the Exceptions using single except block.
# Example :
try:
    numerator = int(input("Enter Numerator : "))
    denominator = int(input("Enter Denominator : "))
    age = int(input("Enter Age : "))
    result = numerator / denominator
    print(f"You are {age} old!\nThe result of the division is {result}")
except Exception:           # It catches all kind of Exceptions.
    print("Error: Some Exception occured.!")

# Output-1 : When 'ZeroDivisionError' occurs.
# Enter Numerator : 100
# Enter Denominator : 0
# Enter Age : 21
# Error: Some Exception occured.!

# Output-2 : When 'ValueError' occurs.
# Enter Numerator : 1000
# Enter Denominator : 10
# Enter Age : Twenty One
# Error: Some Exception occured.!

# We can also display the error message directly without writing any kind of
# user-defined error messages.
try:
    result = 100 / 0
except ZeroDivisionError as zde:
    print(zde)

# Output : division by zero

# try with else clause.
# Example :
try:
    numerator = int(input("Enter Numerator : "))
    denominator = int(input("Enter Denominator : "))
    result = numerator / denominator
    print(f"The result of the division is {result}")
except ZeroDivisionError:
    print("Error: Denominator can not be zero.!")
else:       # Executes after try block if no exception occurs
    print("No Exception Occured.")

# Output :
# Enter Numerator : 25
# Enter Denominator : 5
# The result of the division is 5.0
# No Exception Occured.

# try with finally keyword.
# Example :
try:
    numerator = int(input("Enter Numerator : "))
    denominator = int(input("Enter Denominator : "))
    result = numerator / denominator
    print(f"The result of the division is {result}")
except ZeroDivisionError:
    print("Error: Denominator can not be zero.!")
else:       # Executes after try block if no exception occurs
    print("No Exception Occured.")
finally:
    print("This block will always be executed...")

# Output-1 : When Exception Occurs.
# Enter Numerator : 36
# Enter Denominator : 0
# Error: Denominator can not be zero.!
# This block will always be executed...

# Output-2 : Normal Execution.
# Enter Numerator : 49
# Enter Denominator : 7
# The result of the division is 7.0
# No Exception Occured.
# This block will always be executed...

# Raising Exception : The raise statement allows the programmer to force a
# specific exception to occur.
# Example-1 :
try:
    raise ZeroDivisionError("Raising an Exception...")
except ZeroDivisionError:
    print("Error: An Exception occured.")

# Output : Error: An Exception occured.

# Example-2 : rasing the actual bult-in Exception.
try:
    raise NameError("Raising an Exception")
except NameError:
    print("Exception Block...")
    raise
# Raises the Exception that causes program crash with the message passed in
# the try block raise statement.

# Output :
# Exception Block...
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-16\tempCodeRunnerFile.py",
# line 3, in <module>
#     raise NameError("Raising an Exception")
# NameError: Raising an Exception


# Python Built-in Keywords, Exceptions, methods list.
print(dir(locals()['__builtins__']))
"""
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning',
'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError',
'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError',
'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning',
'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration',
'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__',
'__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__',
'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray',
'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright',
'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec',
'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals',
'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance',
'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max',
'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print',
'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr',
'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type',
'vars', 'zip']
"""
