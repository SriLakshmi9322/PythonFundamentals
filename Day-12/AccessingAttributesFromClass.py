# To add, modify and remove attributes from a class using functions.
""" Instead of using the normal statements to access attributes from the class
We can use functions given below :
1. getattr() - To access the attribute of object.
2. hasattr() - To check if an attribute exists or not.
3. setattr() - To set an attribute. If attribute does not exist, then it would
   be created.
4. delattr() - To delete an attribute. """

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


# This would create first object of Employee class.
emp1 = Employee('SriLakshmi', 15000)

# Using getattr() method : Returns value of 'name' attribute.
print(getattr(emp1, 'name'))                # SriLakshmi

# Using hasattr() method : Returns True if 'name' attribute exists.
print(hasattr(emp1, 'name'))                # True
print(hasattr(emp1, 'age'))                 # False

# Using setattr() method : Sets attribute 'age' with the value 8.
setattr(emp1, 'age', 21)
print(getattr(emp1, 'age'))                 # 21

# Using delattr() method : Deletes attribute 'age'.
delattr(emp1, 'age')
