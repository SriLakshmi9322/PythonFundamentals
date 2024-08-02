# Overriding Methods :
""" We can always override parent class methods. One reason for overriding
parent's methods is because you may want special or different functionality
in our subclass. """
# Example : Program to illustrate method overriding.


class Parent:
    def myMethod(self):
        print("Calling Parent Class Method.!!")


class Child(Parent):
    def myMethod(self):
        print("Calling Child Class Method.!!")


c = Child()                 # Instance of Child Class
c.myMethod()                # Calling Overridden Method

# Output :
# Calling Child Class Method.!!


# Method Overriding in Python
"""
Method Overriding is an ability of any Object-Oriented Programming language
that allows a sub_class or child_class to provide a specific implementation
of a method that is already provided by one of its super_classes or
parent_classes. When a method in a sub_class has the same name, same parameters
or signature and same return type (or sub_type) as a method in its
super_class, then the method in the sub_class is said to override the method
in the super_class.
Example :
Super_Class => Animal : 1. data1
                        2. move()   # Overridden Method
                        3. eat()    # Inherited Method
Sub_Class => Dog : 1. data2
                   2. move()        # Overriding Method
                   3.bark()
"""


class Parent:
    def __init__(self):
        self.value = "Inside Parent"

    def show(self):
        print(self.value)


class Child(Parent):
    def __init__(self):
        self.value = "Inside Child"

    def show(self):
        print(self.value)


# Driver Code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

# Output :
# Inside Parent
# Inside Child

# 1. Method Overriding with Multiple Inheritance
"""
When a class is derived from more than one base class it is called Multiple
Inheritance.
"""


# Example
class Parent1():
    def show(self):
        print("Inside Parent1")


class Parent2():
    def display(self):
        print("Inside Parent2")


class Child(Parent1, Parent2):
    def show(self):
        print("Inside Child")


obj = Child()
obj.show()
obj.display()

# Output :
# Inside Child
# Inside Parent2


# 2. Method Overriding with Multilevel Inheritance
# When we have a child and grandchild relationship.
# Example
class Parent():
    def display(self):
        print("Inside Parent")


class Child(Parent):
    def show(self):
        print("Inside Child")


class GrandChild(Child):
    def show(self):
        print("Inside GrandChild")


g = GrandChild()
g.show()
g.display()

# Output :
# Inside GrandChild
# Inside Parent


# Calling the Parent's method within the Overridden method
"""
Parent Class methods can also be called within the overridden methods. This can
generally be achieved by two ways.

1. using ClassName : Parent's class methods can be called by using the Parent
   'ClassName.method' inside the overridden method.
2. using super() : Python super() function provides us the facility to refer
   to the parent class explicitly. It is basically useful where we have to call
   super_class functions. It returns the proxy object that allows us to refer
   parent class by 'super'.
"""


# 1. Using ClassName Example
class Parent():
    def show(self):
        print("Inside Parent")


class Child(Parent):
    def show(self):
        Parent.show(self)
        print("Inside Child")


obj = Child()
obj.show()

# Output :
# Inside Parent
# Inside Child


# 2.  Example-1: using super()
class Parent():
    def show(self):
        print("Inside Parent")


class Child(Parent):
    def show(self):
        # Calling the Parent's class method
        super().show()
        print("Inside Child")


obj = Child()
obj.show()

# Output :
# Inside Parent
# Inside Child


# Example-2
class Parent:
    def __init__(self):
        print("Hey!!! I am initialized (class Parent)")

    def display(self, b):
        print("Printing from class Parent:", b)


class Child(Parent):
    def __init__(self):
        print("Hey!!! I am initialized (class Child)")
        super().__init__()

    def display(self, b):
        print("Printing from class Child:", b)
        super().display(b+1)


class GrandChild(Child):
    def __init__(self):
        print("Hey!!! I am initialized (class GrandChild)")
        super().__init__()

    def display(self, b):
        print("Printing from class GrandChild", b)
        super().display(b+1)


# Main Function
if __name__ == "__main__":
    # Creating Object
    gc = GrandChild()

    # Calling the function display() from class GrandChild which inherits both
    # Parent and Child classes
    gc.display(10)

# Output :
# Hey!!! I am initialized (class GrandChild)
# Hey!!! I am initialized (class Child)
# Hey!!! I am initialized (class Parent)
# Printing from class GrandChild 10
# Printing from class Child: 11
# Printing from class Parent: 12
