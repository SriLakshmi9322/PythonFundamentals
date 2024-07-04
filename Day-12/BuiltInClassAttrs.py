# Built-in Class Attributes :
""" Every Python class keeps following built-in attributes and they can be
accessed using dot (.) operator like any other attribute-
1. __dict__ : Dictionary containing the class's namespace.
2. __doc__ : Class Documentation String or none, if undefined.
3. __name__ : Class name.
4. __module__ : Module name in which the class is defined. This attribute is
   '__main__' in interactive mode.
5. __bases__ : A possibly empty tuple containing the base classes in the order
   of their occurrence in the base class list. """
# Creating a class


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print(f"Total no. of Employee {Employee.empCount}")

    def displayEmployee(self):
        print("Name :", self.name, ", Salary :", self.salary)


print("Employee.__doc__:", Employee.__doc__)
print("\nEmployee.__name__:", Employee.__name__)
print("\nEmployee.__module__:", Employee.__module__)
print("\nEmployee.__bases__:", Employee.__bases__)
print("\nEmployee.__dict__:", Employee.__dict__)


# Output :
"""
Employee.__doc__: Common base class for all employees

Employee.__name__: Employee

Employee.__module__: __main__

Employee.__bases__: (<class 'object'>,)

Employee.__dict__: {'__module__': '__main__',
'__doc__': 'Common base class for all employees',
'empCount': 0,
'__init__': <function Employee.__init__ at 0x0000021AEACDC160>,
'displayCount': <function Employee.displayCount at 0x0000021AEACDC1F0>,
'displayEmployee': <function Employee.displayEmployee at 0x0000021AEACDC280>,
'__dict__': <attribute '__dict__' of 'Employee' objects>,
'__weakref__': <attribute '__weakref__' of 'Employee' objects>}
"""
