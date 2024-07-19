# First Class Functions in Python
"""
A programming language is said to support First Class functions if it treats
functions as first-class objects. Python supports the concept of First class
functions.
Properties of First Class Functions :
1. A function is an instance of the Object type.
2. You can store the function in a variable.
3. You can pass the function as a parameter to another function.
4. You can return the function from a function.
5. You can store them in data structures such as hash tables, lists, ... etc.,
"""

# 1. Functions are Objects :
"""
Python functions are first class objects. In the example below, we are
assigning function to a variable. This assignment doesn't call the function.
It takes the function object referenced by shout and creates a second name
pointing to it, yell.
"""


# Example :
def shout(text):
    return text.upper()


print(shout("Hello"))
yell = shout
print(yell("Hello"))

# Output :
# HELLO
# HELLO

# 2. Functions can be Passed as arguements to other Functions :
"""
Because functions are Objects. We can pass them an arguements to other
functions. Functions that can accept other functions as arguements are also
called "Higher-order Functions". In the below example, we have created a
function "greet" which takes a function as an arguement.
"""


# Example :
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # Storing the Function in a Variable.
    greeting = func("""Hi, I am created by a function \
passed as an arguement.""")
    print(greeting)


greet(shout)
greet(whisper)

# Output :
# HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUEMENT.
# hi, i am created by a function passed as an arguement.

# 3. Functions can return another Function :
"""
Because functions are Objects. We can return a function from another function.
In the below example, the 'create_adder' function returns 'adder' function.
"""


# Example :
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)
print(add_15(10))

# Output : 25
