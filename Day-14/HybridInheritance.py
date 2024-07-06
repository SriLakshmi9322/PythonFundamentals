# Hybrid Inheritance :
"""
Inheritance consisting of multiple types of Inheritance is called Hybrid
Inheritance.
"""
# Example : Program to demonstrate Hybrid Inheritance.


class School:

    def func1(self):
        print("This Function is in School Class.!!")


class Student1(School):

    def func2(self):
        print("This Function is in Student1 Class.!!")


class Student2(School):

    def func3(self):
        print("This Function is in Student2 Class.!!")


class Student3(Student1, School):

    def func4(self):
        print("This Function is in Student3 Class.!!")


# Driver's Code
obj = Student3()
obj.func1()
obj.func2()

# Output :
# This Function is in School Class.!!
# This Function is in Student1 Class.!!
