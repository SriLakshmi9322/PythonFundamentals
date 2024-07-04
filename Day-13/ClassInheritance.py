# Class Inheritance :

""" Instead of starting from scratch, you can create a class by deriving it
from a pre-existing class by listing the parent class in parentheses after the
new class name.
The child class inherits the attributes of its parent class and you can use
those attributes as if they were defined in the child class. A child class can
also override data members and methods from the parent.
Syntax :
class SubClass(ParentClass1, ..., ParentClassn):
    'Optional class documentation string'
    class_suite
"""
# Example :


class Parent:
    parentAttr = 100

    def __init__(self):
        print("Calling Parent Constructor.!!")

    def parentMethod(self):
        print("Calling Parent Method.!!")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent Attribute :", Parent.parentAttr)


class Child(Parent):
    def __init__(self):
        print("Calling Child Constructor.!!")

    def childMethod(self):
        print("Calling Child Method.!!")


c = Child()             # Instance of Child
c.childMethod()         # Calling child class method
c.parentMethod()        # Calling parent class method
c.setAttr(200)          # Again calling parent class method
c.getAttr()             # Again calling parent class method

# Output :
# Calling Child Constructor.!!
# Calling Child Method.!!
# Calling Parent Method.!!
# Parent Attribute : 200
