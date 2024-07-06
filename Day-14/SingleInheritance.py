# Single Inheritance :
"""
Single Inheritance enables a derived class to inherit properties from a single
parent class, thus enabling code reusability and addition of new features to
existing code.
When a child class inherits properties from only one parent class, it is called
Single Inheritance.
"""
# Example : Program to demonstrate Single Inheritance.


# Base Class
class Parent:
    def func1(self):
        print("This function is in Parent Class.!!")


# Derived Class
class Child(Parent):
    def func2(self):
        print("This function is in Child Class.!!")


# Driver's Code
object = Child()
object.func1()
object.func2()

# Output :
# This function is in Parent Class.!!
# This function is in Child Class.!!
