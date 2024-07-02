# Python Modules : User-defined
""" Modules refer to a file containing Python statements and definitions. We
use modules to break down large programs into small manageable and organized
files. Furthermore, modules provide reusability of code.
We can define our most used functions in a module and import it, instead of
copying their definitions into different programs. """
# Example : Creating a module containg add function with the name 'example.py'


def add(a, b):
    result = a + b
    return result


""" To import this module we can use 'import' keyword.
Syntax : import example"""
