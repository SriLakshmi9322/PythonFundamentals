# Inheritance :
"""
Inheritance is a powerful feature in object-oriented programming. It refer to
defining a new class with little or no modification to an existing class. The
new class is called derived (or child) class and the one from which it inherits
is called the base (or parent) class.
Inheritance is the capacity of one class that inherits all the methods and
properties from another class.
1. Parent class : is the class being inherited from, also called Base class.
2. Child class : is the class that inherits from another class, also called
   Derived class.
"""
# Example-1 : A program to demonstrate inheritance.


class Person(object):
    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if the person is an Employee
    def isEmployee(self):
        return False


# Inherited or Sub class
class Employee(Person):
    # Here we return True
    def isEmployee(self):
        return True


# Driver Code
per = Person("SriLakshmi")      # An object of 'Person' class
print(per.getName(), per.isEmployee())

emp = Employee("Bhavani")       # An object of 'Employee' class
print(emp.getName(), emp.isEmployee())

# Output :
# SriLakshmi False
# Bhavani True

# Example-2 : Program to demonstrate how parent class constructor is called.


class Person(object):
    # __init__ is known as the constructor.
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


# Child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # Invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)


# Creation of an object variable or an instance.
a = Employee('Rahul', 886012, 50000, 'Manager')

# Calling a function of the class Person using its instance.
a.display()

# Output :
# Rahul
# 886012

"""
Different forms of Inheritance :
Types of Inheritance depends upon the number of child and parent classes
involved. There are five types of Inheritance in Python.
1. Single Inheritance
2. Multiple Inheritance
3. Multi-level Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
"""
