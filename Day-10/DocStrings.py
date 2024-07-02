import pickle

# Docstrings :
""" The first string after the function header is called the docstring and is
short for documentation string. It is briefly used to explain what a function
does.
Python docstrings are the string literals that appear after the definition of a
method, class, or module also.
We can access these docstrings using the __doc__ attribute. """
# Example -1 :


def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter.
    """
    print("Hello, " + name + ". Good Morning!")


print(greet.__doc__)
# Output :
"""
    This function greets to
    the person passed in as
    a parameter.
"""


# Example-2 :
def square(num):
    '''Takes in a number num, returns the square of num'''
    return num ** 2


print(square.__doc__)
# Output : Takes in a number num, returns the square of num

# Example-3 : Docstrings for the built-in print() function.
print(print.__doc__)
# Output :
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# Prints the values to a stream, or to sys.stdout by default.
# Optional keyword arguments:
# file:  a file-like object (stream); defaults to the current sys.stdout.
# sep:   string inserted between values, default a space.
# end:   string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.


# Docstrings for Python Modules :
""" The docstrings for Python Modules should list all the available classes,
functions, objects and expectations that are imported when the module is
imported.
They should also have a one-line summary for each item.
They are written at the beginning of the Python file. """
# Example-4 : docstrings for the built-in module in Python called pickle.
print(pickle.__doc__)

# Ouput :
"""
Create portable serialized representations of Python objects.

See module copyreg for a mechanism for registering custom picklers.
See module pickletools source for extensive comments.

Classes:

    Pickler
    Unpickler

Functions:

    dump(object, file)
    dumps(object) -> string
    load(file) -> object
    loads(string) -> object

Misc variables:

    __version__
    format_version
    compatible_formats


"""

# Docstrings for Python Classes :
""" The docstrings for classes should summarize its behavior and list the
public methods and instance variables.
The subclasses, constructs and methods should each have their own docstrings.
"""
# Example-5 : Docstrings for Python class.


class Person:
    """
    A class to represent a person.
    ...
    Attributes
    ----------
    name : str
      first name of the function
    age : int
      age of the person
    """
    """
    Methods
    -------
    info(additional=""):
        prints the person\'s name and age.
    """
    # def info(self, additional="info"):


print(Person.__doc__)
# Output :
"""

    A class to represent a person.
    ...
    Attributes
    ----------
    name : str
      first name of the function
    age : int
      age of the person

"""

# Using the help() Function for Docstrings :
""" We can also use the help() function to read the docstrings associated with
various objects.
Here, we can see that the help() functtion retrieves the docstrings of the
Person class along with the methods associated with that class. """
# Example-6 : Read Docstrings with the help() function.
print(help(Person))

# Output :
"""
Help on class Person in module __main__:

class Person(builtins.object)
 |  A class to represent a person.
 |  ...
 |  Attributes
 |  ----------
 |  name : str
 |    first name of the function
 |  age : int
 |    age of the person
 |
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
-- More  --
"""
