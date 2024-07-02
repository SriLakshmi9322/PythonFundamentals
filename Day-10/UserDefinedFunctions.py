# User-defined Functions :
""" Functions that we define ourselves to do a certain specific task are
referred as user-defined functions.
If we use functions written by others in the form of library, it can be termed
as library functions.
All the other functions that we write on our own fail under user-defined
functions. So, our user-defined function could be a library function to someone
else. """
# Example :


def add_numbers(x, y):
    sum = x + y
    return sum


num1 = 5
num2 = 6
print("The sum is", add_numbers(num1, num2))        # The sum is 11


""" Python Function Arguements :
In python, you can define a function that takes variable number of
arguements. """
# Example :


def greet(name, msg):
    """ This function greets to
    the person with the provided message"""
    print("Hello", name + ',' + msg)


greet("SriLakshmi", " Good Morning!")       # Hello SriLakshmi, Good Morning!
# greet("Monica")           # only one arguement
# TypeError: greet() missing 1 required positional argument: 'msg'
# greet()                   # no arguements
# TypeError: greet() missing 2 required positional arguments: 'name' and 'msg'


""" There are three different forms of Function arguements. They are :
1. Default Arguements.
2. Keyword Arguements.
3. Arbitrary/Variable Length Arguements."""

# 1. Default Arguements :
""" Function Arguements can have default values. We can provide a default
value to an arguement by using the assigned operator. """


def greet(name, msg=" Good Morning!"):
    print("Hello", name + ',' + msg)


greet("SriLakshmi")             # Hello SriLakshmi, Good Morning!
greet("Bhavani", " Welcome to Technical World!")
# Hello Bhavani, Welcome to Technical World!


# 2. Keyword Arguements :
""" Python allows functions to be called using keyword arguements. When we
call functions in this way, the order (position) of the arguements can be
changed.
Following calls to the above function are all valid and produce the same
result. """


def greet(name, msg=" Good Morning!"):
    print("Hello", name + ',' + msg)


# 2 keyword arguements
greet(name="Manju", msg=" Good Morning!!")      # Hello Manju, Good Morning!!

# 2 keyword arguements (out of order)
greet(msg=" Welcome to my world!", name="Pavani")
# Hello Pavani, Welcome to my world!

# 1 positional, 1 keyword arguement
greet("Shivani", msg=" Good Morning!!!")    # Hello Shivani, Good Morning!!!


# Having a positional arguement after after keyword arguements will result in
# errors.
# greet(name="Radha", " Good Morning!!!")
# SyntaxError: positional argument follows keyword argument


# 3. Arbitrary Arguements / Variable length Arguements :
""" Sometimes, We do not know in advance the number of arguements that will be
passed into a function.
Python allows us to handle this kind of situation through function calls with
an arbitrary number of arguements.
In the function definition, we use an asterisk (*) before the parameter name to
denote this kind of arguement. """
# Example :


def greet(*names):
    # Names is a tuple with arguements
    for name in names:
        print("Hello", name)


greet("SriLakshmi", "Manju", "Shivani", "Radha")
# Output :
# Hello SriLakshmi
# Hello Manju
# Hello Shivani
# Hello Radha
