# Hierarchical Inheritance :
"""
When more than one derived classes are created from a single Base Class, this
type of inheritance is called Hierarchical Inheritance. In this Program, we
have a parent (base) class and two child (derived) classes.
"""
# Example : Program to demonstrate Hierarchical Inheritance.


# Base Class
class Parent:

    def func1(self):
        print("This Function is in Parent Class.!!")


# Derived Class1
class Child1(Parent):

    def func2(self):
        print("This Function is in Child1 Class.!!")


# Derived Class2
class Child2(Parent):

    def func3(self):
        print("This Function is in Child2 Class.!!")


# Driver's Code
obj1 = Child1()
obj2 = Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()

# Output :
# This Function is in Parent Class.!!
# This Function is in Child1 Class.!!
# This Function is in Parent Class.!!
# This Function is in Child2 Class.!!
