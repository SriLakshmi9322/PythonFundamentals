# Multiple Inheritance :
"""
When a child class inherits from multiple parent classes, it is called Multiple
Inheritance. Unlike Java and C++, Python supports Multiple Inheritance. We
specify all parent classes as a comma-separated list in the bracket.
When a class can be derived from more than one base classes this type of
inheritance is called Multiple Inheritance. In Multiple Inheritance, all the
features of the base classes are inherited into the derived class.
"""
# Example : Program to demonstrate Multiple Inheritance.


# Base Class1
class Mother:
    mother_name = ""

    def mother(self):
        print(self.mother_name)


# Base Class2
class Father:
    father_name = ""

    def father(self):
        print(self.father_name)


# Derived Class
class Daughter(Mother, Father):
    def parents(self):
        print("Father Name :", self.father_name)
        print("Mother Name :", self.mother_name)


# Driver's Code
dtr = Daughter()
dtr.father_name = "Satya Narayana"
dtr.mother_name = "Ganga Bhavani"
dtr.parents()

# Output :
# Father Name : Satya Narayana
# Mother Name : Ganga Bhavani
