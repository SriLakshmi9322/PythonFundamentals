# Method Overloading
"""
Two or more methods have the same name but different number of parameters or
different types of parameters or both. These methods are called overloaded
methods and this is called "method overloading".
The problem with method overloading in Python is that we may overload the
methods but can only use the latest defined method.
"""


# First product method that takes 2 arguements and prints their product.
def product(a, b):
    p = a * b
    print(p)

# Second product method that takes 3 arguements and prints their product.
def product(a, b, c):
    p = a * b * c
    print(p)


product(4, 5, 5)        # Calls second product method
product(4, 5)           # Raises Error

# Output :
# 100
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-13\tempCodeRunnerFile.py",
# line 13, in <module>
#     product(4, 5)           # Raises Error
# TypeError: product() missing 1 required positional argument: 'c'

# Note : Python does not supports Method Overloading
"""
To overcome the above problem we can use different ways to achieve the 'Method
Overloading'.
1. Method-1 : (Not the Most Efficient Method)
        We can use the arguements to make the same function work differently.
   i.e, as per the arguements.
2. Method-2 : (Not the Efficient One)
        We can achieve method overloading in python by user-defined function
   'None' keyword as default parameters.
   Using if-else statements, we can achieve method overloading, by checking
   each parameter as single statement.
        The Problem with this method is that it makes code more complex with
   multiple if-else statement and is not the desired way to achieve the method
   overloading.
3. Method-3 : (Efficient One)
        By using Multiple Dispatch Decorator. It can be installed by
   'pip3 install multipledispatch'.
   In Backend, Dispatcher creates an object which stores different
   implementations and on runtime, it selects the appropriate method as the
   type and number of parameters passed.
"""


# Method-1 : Function to take Multiple Arguements
def add(datatype, *args):
    # If datatype is 'int' initialize answer as '0'
    if datatype == 'int':
        answer = 0

    # If datatype is 'str' initialize answer as ""
    if datatype == 'str':
        answer = ""

    # To traverse through the arguements
    for x in args:
        # This will do addition if the arguements are int or concatenation if
        # the arguements are 'str'.
        answer = answer + x
    print(answer)

# Integer
add('int', 5, 6)
add('int', 4, 5, 5)

# String
add('str', 'Hi ', 'SriLakshmi')

# Output :
# 11
# 14
# Hi SriLakshmi


# Method-2 : Using 'None' Keyword
def add(a=None, b=None):
    # Checks if both parameters are available if statement will be
    # executed if only one parameter is available
    if a != None and b == None:
        print(a)
    # Else will be executed if both are available and returns addition of
    # 2 attributes.
    else:
        print(a + b)

# 2 args are passed, returns addition of 2
add(2, 3)

# only 1 arg is passed, returns a
add(2)

# Output :
# 5
# 2


# Method-3 : using 'multipledispatch' Decorator
from multipledispatch import dispatch


# Passing 1 parameter
@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)


# Passing 2 parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)


# You can also pass datatype of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


# Calling product method with 2 arguements
product(2, 3)

# Calling product method with 3 args of all 'int'
product(2, 3, 2)

# Calling product method with 3 args but all 'float'
product(2.2, 3.4, 2.3)

# Output :
# 6
# 12
# 17.204
