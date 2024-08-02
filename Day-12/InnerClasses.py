# Python Inner Classes
"""
Inner Classes in Python are classes defined within another class. They are used
to logically group classes that are only used in one place, which can help in
organizing code and improving readability.
"""


# Example
class OuterClass:
    def __init__(self, outer_value):
        self.outer_value = outer_value

    def show_outer_value(self):
        print(f"Outer Value: {self.outer_value}")

    class InnerClass:
        def __init__(self, inner_value):
            self.inner_value = inner_value

        def show_inner_value(self):
            print(f"Inner Value: {self.inner_value}")


# Creating an instance of the Outer Class
outer = OuterClass("Outer Value")

# Creating an instance of the Inner Class
inner = outer.InnerClass("Inner Value")

# Using the methods of both classes
outer.show_outer_value()
inner.show_inner_value()

# Output :
# Outer Value: Outer Value
# Inner Value: Inner Value

"""
In the example,
1. 'Outer Class' is the outer class containing an inner class named
   'InnerClass'.
2. You can create instances of both the outer and inner classes and use their
   methods.
"""

# Example with Access to Outer Class
"""
To allow the inner class to access members of the outer class, you might need
to pass an instance of the outer class to the inner class.
"""


class OuterClass:
    def __init__(self, outer_value):
        self.outer_value = outer_value

    def show_outer_value(self):
        print(f"Outer Value: {self.outer_value}")

    class InnerClass:
        def __init__(self, outer_instance, inner_value):
            self.outer_instance = outer_instance
            self.inner_value = inner_value

        def show_inner_value(self):
            print(f"Inner Value: {self.inner_value}")
            print(f"Accessing Outer Value: {self.outer_instance.outer_value}")


# Creating an instance of the Outer Class
outer = OuterClass("Outer Value")

# Creating an instance of the inner class, passing the outer instance
inner = outer.InnerClass(outer, "Inner Value")

# Using the methods of both classes
outer.show_outer_value()
inner.show_inner_value()

# Output :
# Outer Value: Outer Value
# Inner Value: Inner Value
# Accessing Outer Value: Outer Value


class Color:
    # Constructor Method
    def __init__(self):
        # Object Attribute
        self.name = "Green"
        self.lg = self.LightGreen()

    def show(self):
        print("Name:", self.name)

    class LightGreen:
        def __init__(self):
            self.name = "Light Green"
            self.code = "024avc"

        def display(self):
            print("Name:", self.name)
            print("Code:", self.code)


# Creating Color class Object
outer = Color()

# Method Calling
outer.show()

# Create a Lightgreen inner class Object
g = outer.lg

# Inner class Method Calling
g.display()

# Output :
# Name: Green
# Name: Light Green
# Code: 024avc


# Types of Inner Classes : 1. Multiple Inner Class
#                          2. Multilevel Inner Class

# 1. Multiple Inner Class
"""
The class contains one or more inner classes known as multiple inner classes.
We can have multiple inner classes in a class. It is easy to implement
multiple inner classes.
"""


# Example
class Doctor:
    def __init__(self):
        self.name = 'Doctor'
        self.den = self.Dentist()
        self.car = self.Cardiologist()

    def show(self):
        print("In Outer Class")
        print("Name:", self.name)

    # First Inner Class
    class Dentist:
        def __init__(self):
            self.name = "Dr. Savita"
            self.degree = "BDS"

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)

    class Cardiologist:
        def __init__(self):
            self.name = "Dr. Amit"
            self.degree = "DM"

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)


# Object of Outer Class
outer = Doctor()
outer.show()

# Object of First Inner Class
d1 = outer.den

# Object of Second Inner Class
d2 = outer.car
print()
d1.display()
print()
d2.display()

# Output :
# In Outer Class
# Name: Doctor

# Name: Dr. Savita
# Degree: BDS

# Name: Dr. Amit
# Degree: DM

# 2. Multilevel Inner Class
"""
The class contains an inner class and that inner class again contains another
inner class, this hierarchy is known as the multilevel inner class.
"""


# Example
class Outer:
    def __init__(self):
        # Creating an inner class Object
        self.inner = self.Inner()

    def show(self):
        print("This is an Outer Class")

    class Inner:
        def __init__(self):
            # Creating an inner class of Inner class Object
            self.innerclassofinner = self.Innerclassofinner

        def show(self):
            print("This is the Inner class.")

        # Creating an inner class of inner
        class Innerclassofinner:
            def show():
                print("This is an Inner class of Inner class.")


# Creating an Outer class Object i.e, 'Outer' class object
outer = Outer()
outer.show()
print()

# Creating an inner class Object
obj1 = outer.inner
obj1.show()
print()

# Creating an inner class of inner class object
obj2 = outer.inner.innerclassofinner
obj2.show()

# Output :
# This is an Outer Class

# This is the Inner class.

# This is an Inner class of Inner class.
