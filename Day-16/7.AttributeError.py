# AttributeError
"""
AttributeError: This exception is raised when an attribute or method is not
                found on an object, such as trying to access a non-existent
                attribute of a class instance.
"""

# Example-1 : When we apply a function on a different datatype.
a = 99

a.append("SriLakshmi")

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 4, in <module>
#     a.append("SriLakshmi")
# AttributeError: 'int' object has no attribute 'append'

# Solution :
try:
    a = 99

    a.append("SriLakshmi")
except AttributeError:
    print("Error: This method is not applicable on different datatype...")

# Output :
# Error: This method is not applicable on different datatype...

# Example-2 : There are chances of AttributeError in the wrong spelling of the
# attribute.
my_name = "My Name is {}".fst("SriLakshmi")

print(my_name)

# # Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 3, in <module>
#     my_name = "My Name is {}".fst("SriLakshmi")
# AttributeError: 'str' object has no attribute 'fst'

# Solution :
try:
    my_name = "My name is {}".fst("SriLakshmi")

    print(my_name)
except AttributeError:
    print("Error: fst Attribute does not exist for the variable...")

# Output :
# Error: fst Attribute does not exist for the variable...


# Example-3 : When we try to make a wrong reference for any class variable.
class Person:
    def __init__(self):
        self.name = "SriLakshmi"


person = Person()
print("Name of the Person is '{}'".format(person.name))
print("Age of the Person is {}".format(person.age))

# Output :
# Name of the Person is 'SriLakshmi'
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 9, in <module>
#     print("Age of the Person is {}".format(person.age))
# AttributeError: 'Person' object has no attribute 'age'


# Solution :
class Person1:
    def __init__(self):
        self.name = "SriLakshmi"


person1 = Person1()
try:
    print(f"Name : {person1.name}")
    print(f"Age : {person1.age}")
except AttributeError:
    print("Error: Attribute is not available in the Class...")

# Output :
# Name : SriLakshmi
# Error: Attribute is not available in the Class...
