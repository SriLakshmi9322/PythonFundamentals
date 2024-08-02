# Python Encapsulation
"""
Encapsulation is one of the fundamental concepts in Object-Oriented Programming
(OOP). It describes the idea of wrapping data and the methods that work on data
within one unit. This puts restrictions on accessing variables and methods
directly and can prevent the accidental modification of data. To prevent
accidental changes an object's variable can only be changed by an object's
method. Those types of variables are known as private variables.
    A class is an example of encapsulation as it encapsulates all the data
that is member functions, variables etc.,

Note : Double-Underscore(__) represents private attributes.
Private Attributes starts with '__'.
"""


# Example
class Base:
    def __init__(self):
        self.fname = "SriLakshmi"
        self.__lname = "Tiramsetti"


# Creating a Derived Class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base Class
        Base.__init__(self)
        print("Calling Private member of base class:")
        print(self.__lname)


# Driver Code
obj = Base()
print(obj.fname)
print(obj.lname)

# Output :
# SriLakshmi
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-13\tempCodeRunnerFile.py",
# line 36, in <module>
#     print(obj.lname)
# AttributeError: 'Base' object has no attribute 'lname'
