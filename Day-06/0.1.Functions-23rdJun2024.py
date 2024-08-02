# User Defined Functions - They are reusable code blocks, they only need to be
# written once, then they can be used multiple times.
# These functions are very useful, from writing common utilities to specific
# business logic. The code is usually well organized, easy to maintain and
# developer-friendly. The function can have diff types of arguements &
# return value. To declare a function we need to use the keyword 'def'

# There are two types of functions :
# 1. Built-in Functions - Pre-defined functions
# 2. User-defined Functions - defined by the users themselves

# Example-1 :
def display():
    print('Hello World.!!')


display()           # Hello World.!!
display()           # Hello World.!!


# Example-2 :
# To declare an empty function we can use pass statement
def display1():
    pass


display1()


# Example-3
def wish(name):
    print('Happy Birthday dear', name)


wish('SriLakshmi')          # Happy Birthday dear SriLakshmi
wish('John')                # Happy Birthday dear John

# Inner Function - A function can be created as an inner function in order to
# protect it from everything that is happening outside of the function.
# In that case, the function will be hidden from the global scope.


# Example :
def Outer_function():
    print('Hello, I am from Outer Function...')

    def Inner_function():
        print('Hello, I am from Inner Function...')
    Inner_function()


Outer_function()
# Output :
# Hello, I am from Outer Function...
# Hello, I am from Inner Function...

# To access Inner_function() we must first call Outer_function()
# If the Outer_function is not called, the Inner_function will never execute

# To represent Outer function variable inside the inner function
# use 'nonlocal keyword'
# Example :


def Outer():
    var_outer = 'outer variable'
    print(var_outer)

    def inner():
        nonlocal var_outer
        var_outer = 'inner variable'
    inner()
    print(var_outer)


Outer()
# Output :
# outer variable
# inner variable

# To represent the global value inside the function use global keyword
name = 'SriLakshmi'


def Outer():
    var_outer1 = 'Outer variable'

    def inner():
        nonlocal var_outer1
        var_outer1 = 'Inner variable'
    global name
    print(name)
    name = 'SriLakshmi Tiramsetti'
    print(name)

    print(var_outer1)
    inner()
    print(var_outer1)


Outer()
# Output :
# SriLakshmi
# SriLakshmi Tiramsetti
# Outer variable
# Inner variable

# Function Arguements :
# 1. Default Arguements
# 2. Required Arguements
# 3. Keyword Arguements
# 4. Variable Arguements
