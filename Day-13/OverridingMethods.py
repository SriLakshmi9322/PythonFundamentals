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
