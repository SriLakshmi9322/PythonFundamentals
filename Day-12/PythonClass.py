# Python Class
"""
A class is a collection of objects. A class contains the Blueprints or the
prototype from which the object's are being created. It is a logical entity
that contains some attributes and methods.
1. Classes are created by keyword 'class'.
2. Attributes are the variables that belong to class.
3. Attributes are always public and can be accessed using the dot (.) operator.
   Example : MyClass.MyAttribute
"""


# Example : Creating an empty class.
class Dog:
    pass


# Python Objects
"""
In OOPs, The object is an entity that has a state and behaviour associated with
it. An object consists of :
1. state : It represented by the attributes of an object. It also reflects the
           properties of an object.
2. behaviour : It is represented by the methods of an object. It also reflects
               the response of an object to other objects.
3. Identity : It gives a unique name to an object and enables one object to
              interact within other objects.
"""
# Example :
obj = Dog()

# The Python 'self':
"""
1. Class methods must have an extra first parameter in the method definition.
   We do not give a value for this parameter when we call the method, Python
   provides it.
2. If we have a method that takes no arguements, then we still have to have
   one arguement.
        When we call a method of this object as 'myobject.method(arg1, arg2)',
this is automatically converted by Python into 'MyClass.method(myobject, arg1,
arg2)'.
"""

# The Python __init__ Method:
"""
The __init__ method is a constructor. It will be executed as soon as an object
of a class is instantiated. The method is useful to do any initialization you
want to do with your object.
"""


# Creating a class and objects with class & instance attributes.
class Dog:
    # Class Attribute
    attr = "mammal"

    # Instance Attribute
    def __init__(self, name):
        self.name = name


# Driver Code
# Object Instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing Class Attributes
print("Rodger is a {}".format(Rodger.__class__.attr))
print("Tommy is also a {}".format(Tommy.__class__.attr))

# Accessing class attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

# Output :
# Rodger is a mammal
# Tommy is also a mammal
# My name is Rodger
# My name is Tommy


# Creating class and objects with methods
class Dog:
    attr = "mammal"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing Class Methods
Rodger.speak()
Tommy.speak()

# Output :
# My name is Rodger
# My name is Tommy
