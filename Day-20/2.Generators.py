# Generators in Python
"""
A Generator in Python is a function that returns an iterator using the 'yield'
keyword.

Generator Function in Python : A generator function in Python is defined like a
normal function, but whenever it needs to generate a value, it does so with the
'yield keyword' rather than return. If the body of a def contains yield, the
function automatically becomes a Python generator function.
"""

# To create a Generator
"""
To create a Simple Generator in Python.
Syntax : def function_name():
             yield statement
"""


# Example :
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


for value in simpleGeneratorFun():
    print(value)

# Output :
# 1
# 2
# 3


# Generator Object
"""
Generator function return a generators object that is iterable, i.e, Generator
function can be used as an 'Iterator'. Generator objects are used either by
calling the next() method of the generator object or using the generator object
in a "for in" loop.
"""


# To create a simple generator function in Python to generate objects using the
# "next()" function.
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


x = simpleGeneratorFun()

print(next(x))
print(next(x))
print(next(x))

# Output :
# 1
# 2
# 3


# To create 2 generators for Fibonacci Numbers, first simple generator and
# second generator using a for loop.
# Example :
def fib(limit):
    a, b = 0, 1

    while a < limit:
        yield a

        a, b = b, a + b


x = fib(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print("Using for in loop :")
for i in fib(5):
    print(i)

# Output :
# 0
# 1
# 1
# 2
# 3
# Using for in loop :
# 0
# 1
# 1
# 2
# 3


# Generator Expression
"""
Python Generator Expression is another way of writing the generator function.
It uses the Python "list comprehension" technique but instead of storing the
elements in a list in memory. It creates generator object.
Syntax : (expression for item in iterable)
"""

# Example :
"""
To create a generator object that will print the multiple of 5 between the
range of 0 to 5. Which are also divisible by 2.
"""
# Generator Expression
generator_exp = (i*5 for i in range(5) if i % 2 == 0)

for i in generator_exp:
    print(i)

# Output :
# 0
# 10
# 20
