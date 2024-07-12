# TypeError
"""
TypeError: This exception is raised when an operation or function is applied
           to an object of the wrong type, such as adding a string to an
           integer.
"""

# Example-1 :
x = 99
y = "Hello"

z = x + y

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
#   line 12, in <module>
#     z = x + y
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Solution : To Avoid Above Program Crash.
try:
    x = 99
    y = "Hello"

    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")

# Output :
# Error: cannot add an int and a str

# Example-2 :
x1 = "Hi"
y1 = "Hello"

z1 = x1 * y1

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
#   line 5, in <module>
#     z1 = x1 * y1
# TypeError: can't multiply sequence by non-int of type 'str'

# Solution :
try:
    x1 = "Hi"
    y1 = "Hello"

    z1 = x1 * y1
except TypeError:
    print("Error: cannot multiply str and str")

# Output :
# Error: cannot multiply str and str

# Example-3 : Calling a non-callable object/function.
value = 12

value()

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
#   line 4, in <module>
#     value()
# TypeError: 'int' object is not callable

# Solution :
try:
    value = 12

    value()
except TypeError:
    print("Error: 'int' object is not callable")

# Output :
# Error: 'int' object is not callable

# Example-4 : Incorrect type of list index.
lst = [10, 20, 30]

print(lst['1'])

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
#   line 4, in <module>
#     print(lst['1'])
# TypeError: list indices must be integers or slices, not str

# Solution :
try:
    lst = [10, 20, 30]
    print(lst['1'])
except TypeError:
    print("Error: Invalid Index Value...")

# Output :
# Error: Invalid Index Value...


# Example-5 : missing arguement while calling.
def sayHello(name):
    print("Hello {}".format(name))


sayHello()

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
#   line 6, in <module>
#     sayHello()
# TypeError: sayHello() missing 1 required positional argument: 'name'

# Solution :
try:
    def sayHello(name):
        print("Hello {}".format(name))

    sayHello()
except TypeError:
    print("Error: You did not pass any arguement while calling the function")

# Output :
# Error: You did not pass any arguement while calling the function

# Example : Handling TypeErrors.
list = ["SriLakshmi", "Tiramsetti", "SriLakshmi Tiramsetti"]
indices = [0, 1, "2"]
for i in range(len(indices)):
    try:
        print(list[indices[i]])
    except TypeError:
        print("TypeError: Check list of indices")

# Output :
# SriLakshmi
# Tiramsetti
# TypeError: Check list of indices
