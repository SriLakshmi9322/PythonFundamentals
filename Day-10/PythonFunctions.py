# Python Functions :
""" In Python, a function is a group of related statements that performs
a specific task.
Functions help break our program into smaller and modular chuncks. As our
program grows larger and larger, functions make it more organized and
manageable.
It avoids repetition and makes the code reusable.
Syntax :
def function_name(parameter):
    '''docstring'''
    statement(s)
    return
1. def - def is a keyword that marks the start of the function header.
2. function_name - to uniquely identify the function. Function naming follows
   the same rules of writing identifiers in Python.
3. parameters (arguements) - through which we pass values to a function. They
   are Optional.
4. colon (:) - to mark the end of the function header.
5. docstring - Documentation String to describe what the function does which
   is Optional.
6. statement(s) - One or more valid python statements that make up the function
   body. Statements must have the same indentation level (usually 4 spaces).
7. return - return statement to return a value from the function which is
   Optional. """
# Example :


def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter.
    """
    print("Hello, " + name + ". Good Morning!")


""" To call a function in python :
Once we have defined a function, we can call it from another function, program
or even the Python prompt. To call a function we simply type the function name
with appropriate parameters. """
greet('SriLakshmi')
# Output : Hello, SriLakshmi. Good Morning!

# Note : Try running the above code in the Python program with the function
# definition to see the output.
