# Base Overloading Methods :
"""
Some generic functionalities that we can override in our own classes :
1. __init__(self, [args]): - Constructor (with any optional arguements).
   Sample call : obj = className(args)

2. __del__(self): - Destructor, Deletes an object.
   Sample call : del obj

3. __repr__(self): - Evaluating String representation.
   Sample call : repr(obj)

4. __str__(self): - Printable String representation.
   Sample call : str(obj)

5. __cmp__(self, x): - Object Comparison.
   Sample call : cmp(obj, x)
"""

# Overloading Operators :
"""
When we have created a Vector class to represent two-dimensional vectors and
want to perform addition operation using plus (+) operation will results some
exceptions.
We can define the __add__() methodin our class to perform vector addition and
then the plus (+) operator would behave as per expectation. """
# Example : Program that illustrates Vector class.


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Vector({self.a}, {self.b})"

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

# Output :
# Vector(7, 8)
