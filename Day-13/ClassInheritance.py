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


# Example-1 :
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


# Example-2 :
class Person(object):       # Parent class
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My Name is {}".format(self.name))
        print("Idnumber : {}".format(self.idnumber))


# Child Class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # Invoking the __init__ of the Parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My Name is {}".format(self.name))
        print("Idnumber : {}".format(self.idnumber))
        print("Post : {}".format(self.post))


a = Employee('Rahul', 886012, 200000, "Intern")

# Calling a function of the class Person using it's instance
a.display()
a.details()

# Output :
# Rahul
# 886012
# My Name is Rahul
# Idnumber : 886012
# Post : Intern
