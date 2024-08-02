# Data Abstraction
"""
It hides unnecessary code details from the user. Also, when we do not want to
give out sensitive parts of our code implementation and this is where data
abstraction came.
"""

# Data Hiding & Printing Objects
# 1. Data Hiding
"""
In Python, we use double underscore (__) before the attributes name and those
attributes will not be directly visible outside.
"""


class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 0

    # A member method that changes __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)


# Driver Code
myObject = MyClass()
myObject.add(2)
myObject.add(5)

# This line cause Error
print(myObject.__hiddenVariable)

# Output :
# 2
# 7
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-13\tempCodeRunnerFile.py",
# line 30, in <module>
#     print(myObject.__hiddenVariable)
# AttributeError: 'MyClass' object has no attribute '__hiddenVariable'


# To Access the hidden attribute value
class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = "Hidden Value"


# Driver Code
myObject = MyClass()
print(myObject._MyClass__hiddenVariable)

# Output : Hidden Value

# 2. Printing Objects
"""
Printing Objects give us information about objects we are working with. In
Python, this can be achieved by using __repr__ or __str__ methods.
"""


class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a: %s b: %s" % (self.a, self.b)

    def __str__(self):
        return "From str method of Test: a is %s" \
            " b is %s" % (self.a, self.b)


# Driver Code
t = Test(1234, 5678)
print(t)        # This calls __str__()
print([t])      # This calls __repr__()

# Output :
# From str method of Test: a is 1234 b is 5678
# [Test a: 1234 b: 5678]

# Important Points about printing
"""
If no __str__ method is defined, print t (or print str(t)) uses __repr__.
"""


class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a: %s b: %s" % (self.a, self.b)


# Driver Code
t = Test(1234, 5678)
print(t)

# Output : Test a: 1234 b: 5678


# If no __repr__ method is defined then the default is used.
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Driver Code
t = Test(1234, 5678)
print(t)

# Output : <__main__.Test object at 0x00000247DFDDCC40>
