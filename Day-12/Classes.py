# Creating Classes :
""" The class statement creates a new class definition. The name of the class
immediately follows the keyword 'class' followed by a colon as follows :
class ClassName:
    'Optional class documentation string'
    class_suite
1. The class has a documentation string, which can be accessed via
   'ClassName.__doc__'.
2. The 'class_suite' consists of all the component statements defining class
   members, data members and functions. """

# Example : Creating a simple Python class.


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


"""
1. empCount - It is a class variable. We can access this variables as
   'Employee.empCount'.
2. __init__() - Special method also called class Constructor or initialization
   method. Python calls when we create a new instance of this class.
3. displayCount() and displayEmployee() - Normal methods with the exception
   that the first arguement to each method is 'self'. You do not need to
   include it when you call the methods.
"""


# Creating Instance Objects :
""" To create instance of a class, you call the class using class_name and
pass in whatever arguements it's __init__ method accepts. """

# This would create first object of Employee class.
emp1 = Employee('SriLakshmi', 15000)

# This would create second object of Employee class.
emp2 = Employee('Zara', 5000)


# Accessing Attributes :
"""
You access the object's attributes using the dot (.) operator with object.
1. emp1.displayEmployee()
2. emp2.displayEmployee()
Class Variable would be accessed using class name as follows :
Syntax : Employee.empCount
"""
# Accessing the methods through object's using the dot (.) operator.
emp1.displayEmployee()              # Name : SriLakshmi , Salary : 15000
emp2.displayEmployee()              # Name : Zara , Salary : 5000

# Accessing class variable using class_name.
print("Total no. of Employees", Employee.empCount)  # Total no. of Employees 2


# We can add, modify and remove attributes of classes and objects at any time
emp1.age = 20           # Adds an 'age' attribute.
print("Age attribute is added.!!\nValue of age is", emp1.age)
# Output :
# Age attribute is added.!!
# Value of age is 20

emp1.age = 21           # Modifying 'age' attribute.
print("After Modifying the age attribute the value is", emp1.age)
# Output : After Modifying the age attribute the value is 21

del emp1.age            # Deleting 'age' attribute.
# print(emp1.age)   # AttributeError: 'Employee' object has no attribute 'age'
