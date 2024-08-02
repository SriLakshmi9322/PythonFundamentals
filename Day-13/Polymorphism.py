# Python Polymorphism
"""
This code demonstrates the concept of Python OOPs Inheritance and method
Overriding in Python Classes. It shows how subclasses can override methods
defined in their parent class to provide specific behaviour while still
inheriting other methods from the parent class.
"""


# Example :
class Bird:
    def intro(self):
        print("There are many types of Birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

# Output :
# There are many types of Birds.
# Most of the birds can fly but some cannot.
# There are many types of Birds.
# Sparrows can fly.
# There are many types of Birds.
# Ostriches cannot fly.
