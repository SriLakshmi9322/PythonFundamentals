# Multi-level Inheritance :
"""
In Multi-level Inheritance, features of the base class and the derived class
are further inherited into the new derived class. This is similar to a
relationship representing a child and grandfather.
"""
# Example : Program to demonstrate Multi-level Inheritance.


# Base Class
class GrandFather:
    grandfather_name = ""

    def grandfather(self):
        print(self.grandfather_name)


# Intermediate Class
class Father(GrandFather):
    father_name = ""

    def father(self):
        print(self.father_name)


# Derived Class
class Son(Father):
    def parent(self):
        print("Grand Father Name :", self.grandfather_name)
        print("Father Name :", self.father_name)


# Driver's Code
son = Son()
son.grandfather_name = "Srinivas"
son.father_name = "Ankush"
son.parent()

# Output :
# Grand Father Name : Srinivas
# Father Name : Ankush
