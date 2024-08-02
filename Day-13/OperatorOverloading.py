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

# Operator Overloading
"""
Operator Overloading means giving extended meaning beyond their predefined
operational meaning. For Example operator '+' is used to add two integers as
well as joins two strings and to merge two lists. It is achievable because
'+' operator is overloaded by int class and str class. You might have noticed
that the same built-in operator or function shows different behaviour for
objects of different classes, this is called 'Operator Overloading'.
"""

# Program to show use of '+' operator for different purposes.
print(1 + 2)                           # 3

# To concatenate 2 strings
print('SriLakshmi' + 'Tiramsetti')     # SriLakshmiTiramsetti

# Product of 2 numbers
print(3 * 4)                           # 12

print("SriLakshmi" * 5)
# Output : SriLakshmiSriLakshmiSriLakshmiSriLakshmiSriLakshmi

"""
      We can overload our operators : If we have to add 2 objects using binary
'+' operator it throws an error because compiler do not know how to add
2 objects. So, here we can define a method for an operator and this process
is called Operator Overloading. We can overload all existing operators but
can't create a new operator.
      To make this possible Python provides some special functions or magic
functions that is automatically invoked when it is associated with that
particular operators. For Example, When we use '+' operator, the magic method
'__add__' is automatically invoked in which the operation for '+' operator is
defined.
"""


# To illustrate how to overload a binary '+' operator and how it actually works
class A:
    def __init__(self, a):
        self.a = a

    # Adding two objects
    def __add__(self, other):
        return self.a + other.a


obj1 = A(1)
obj2 = A(2)
obj3 = A("SriLakshmi")
obj4 = A("Tiramsetti")

print(obj1 + obj2)            # 3
print(obj3 + obj4)            # SriLakshmiTiramsetti

# Actual working when Binary Operator is used.
print(A.__add__(obj1, obj2))  # 3
print(A.__add__(obj3, obj4))  # SriLakshmiTiramsetti

# And can also be Understand as:
print(obj1.__add__(obj2))     # 3
print(obj3.__add__(obj4))     # SriLakshmiTiramsetti


# To perform addition of 2 complex numbers using binary '+' Operator
# Overloading
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Adding 2 Objects
    def __add__(self, other):
        return self.a + other.a, self.b + self.b


obj1 = Complex(1, 2)
obj2 = Complex(2, 3)
obj3 = obj1 + obj2
print(obj3)             # (3, 5)


# Overloading Comparison Operators
class A:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if (self.a > other.a):
            return True
        else:
            return False


obj1 = A(2)
obj2 = A(3)
if (obj1 > obj2):
    print("Obj1 is Greater than Obj2")
else:
    print("Obj2 is Greater than Obj1")

# Output : Obj2 is Greater than Obj1


# Overloading Equality and Less than Operators
class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return "Obj1 is less than Obj2."
        else:
            return "Obj2 is less than Obj1."

    def __eq__(self, other):
        if self.a == other.a:
            return "Both are Equal."
        else:
            return "Not Equal."


obj1 = A(2)
obj2 = A(3)
print(obj1 < obj2)

obj3 = A(4)
obj4 = A(4)
print(obj3 == obj4)

# Output :
# Obj1 is less than Obj2.
# Both are Equal.

"""
Python Magic Methods or Special Functions for Operator Overloading:
Binary Operators:
        Operator        Magic Method
        --------        ------------
            +           __add__(self, other)
            -           __sub__(self, other)
            *           __mul__(self, other)
            /           __div__(self, other)
           //           __floordiv__(self, other)
            %           __mod__(self, other)
           **           __pow__(self, other)
           >>           __rshift__(self, other)
           <<           __lshift__(self, other)
            &           __and__(self, other)
            |           __or__(self, other)
            ^           __xor__(self, other)

Comparison Operators:
        Operator        Magic Method
        --------        ------------
            <           __lt__(self, other)
            >           __gt__(self, other)
           <=           __le__(self, other)
           >=           __ge__(self, other)
           ==           __eq__(self, other)
           !=           __ne__(self, other)

Assignment Operators:
        Operator        Magic Method
        --------        ------------
           -=           __isub__(self, other)
           +=           __iadd__(self, other)
           *=           __imul__(self, other)
           /=           __idiv__(self, other)
          //=           __ifloordiv__(self, other)
           %=           __imod__(self, other)
          **=           __ipow__(self, other)
          >>=           __irshift__(self, other)
          <<=           __ilshift__(self, other)
           &=           __iand__(self, other)
           |=           __ior__(self, other)
           ^=           __ixor__(self, other)

Unary Operators:
        Operator        Magic Method
        --------        ------------
            -           __neg__(self)
            +           __pos__(self)
            ~           __invert__(self)

Note : It is not possible to change the number of operands of an operator. For
Example, aif we cannot overload a unary operator as a Binary Operator, the
following code will throw a syntax error.
"""


# Program which attempts to overload '~' operator as Unary Operator.
class A:
    def __init__(self, a):
        self.a = a

    # Overloading '~' operator, but with 2 operands
    def __invert__(self):
        return "This is the ~ operator, overloaded as Unary Operator."


obj1 = A(1)
print(~obj1)

# Output :
# This is the ~ operator, overloaded as Unary Operator.


# Operator Overloading on Boolean Values E.g for 'and' operator
class MyClass:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return MyClass(self.value and other.value)

    def __repr__(self):
        return f'{self.value}'


a = MyClass(True)
b = MyClass(False)
c = a & b
print(c)                # False
