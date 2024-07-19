# Decorators in Python
"""
Decorator is a Higher Order Function that takes another function as an
arguement, adds some functionality & returns a new function. It allows
modifying/extending bahaviour of functions/methods.
    Decorators are very powerful and useful tool in Python. Since it allows
programmers to modify the behaviour of a function or class. Decorators allows
us to wrap another function in order to extend the behaviour of the wrapped
function, without permanently modifying it. But
1. Decorators are used to modify the behaviour of function/class.
2. Functions are taken as arguement into another function and then called
   inside the wrapper function.

Syntax for decorators:
@decorator
def hello_decorator():
    print("Hello!")
''' Above Code is equivalent to -
def hello_decorator():
    print("Hello!")

hello_decorator = decorator(hello_decorator) '''
In the above code, decorator is a callable function, that will add some code
on the top of some another callable function, decorator function & return
the wrapper function.
"""


# Decorator can modify the behaviour
# Defining a Decorator
def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution.")
        func()
        print("This is after function execution.")
    return inner1


def function_to_be_used():
    print("This is inside the function!!!")


function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()

# Output :
# Hello, this is before function execution.
# This is inside the function!!!
# This is after function execution.


# To easily find out the execution time of a function using decorator
import time
import math


def calculate_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in :", func.__name__, end - begin)
    return inner1


@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))


factorial(10)

# Output :
# 3628800
# Total time taken in : factorial 2.0015602111816406


# If function returns something or an arguement is passed to the function.
# (One may need the return value).
def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("Before execution")
        returned_value = func(*args, **kwargs)
        print("After execution")
        return returned_value
    return inner1


@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2
print("Sum =", sum_two_numbers(a, b))

# Output :
# Before execution
# Inside the function
# After execution
# Sum = 3


# Chaining Decorators : Decorating a function with multiple decorators.
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner


@decor1
@decor
def num():
    return 10


@decor
@decor1
def num2():
    return 10


print(num())
print(num2())

# Output :
# 400
# 200

"""
The above example is similar to calling the function as -
decor1(decor(num))
decor(decor1(num2))
"""
