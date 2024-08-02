# Abstract Class
"""
        An Abstract Class can be considered as a Blueprint for other classes.
It allows you to create set of methods that must be created within any child
classes built from the abstract class.
        A class that contains one or more abstract methods is called an
'abstract class' is a method that has a declaration but does not have an
implementation.
        We use an abstract class while we are designing large functional units
or when we want to provide a common interface for different implementations of
a component.

    By default, Python does not provide abstract classes. Python comes with a
module that provides the base for defining 'Abstract Base Class (ABC)' and that
module name is ABC.
        ABC works by decorating methods of the base class as an abstract and
then registering concrete classes as implementations of the abstract base. A
method becomes abstract when decorated with the keyword '@abstractmethod'.
"""

# Example-1: To illustrate the working of Abstract Base Class
from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):
    # Overriding Abstract method
    def noofsides(self):
        print("I am Triangle and I have 3 sides.")


class Pentagon(Polygon):
    # Overriding Abstract method
    def noofsides(self):
        print("I am Pentagon and I have 5 sides.")


class Hexagon(Polygon):
    # Overriding Abstract method
    def noofsides(self):
        print("I am Hexagon and I have 6 sides.")


class Quadrilateral(Polygon):
    # Overriding Abstract method
    def noofsides(self):
        print("I am Quadrilateral and I have 4 sides.")


# Driver Code
T = Triangle()
T.noofsides()

Q = Quadrilateral()
Q.noofsides()

P = Pentagon()
P.noofsides()

H = Hexagon()
H.noofsides()

# Output :
# I am Triangle and I have 3 sides.
# I am Quadrilateral and I have 4 sides.
# I am Pentagon and I have 5 sides.
# I am Hexagon and I have 6 sides.

# Example-2: Animal class with non-abstract method
from abc import ABC


class Animal(ABC):
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can Walk and Run.")


class Snake(Animal):
    def move(self):
        print("I can crawl.")


class Dog(Animal):
    def move(self):
        print("I can Bark.")


class Lion(Animal):
    def move(self):
        print("I can Roar.")


# Driver Code
H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()

# Output :
# I can Walk and Run.
# I can crawl.
# I can Bark.
# I can Roar.


# Implementing of Abstract through Sub_class
"""
    By Sub_classing directly from the base, we can avoid the need to register
the class explicitly. In this case, the Python class management is used to
recognize 'Plugin Implementation' as implementing the 'abstract PluginBase'.
"""


class Parent:
    def display(self):
        pass


class Child(Parent):
    def display(self):
        print("Child Class")


# Driver Code
print(issubclass(Child, Parent))        # True
print(isinstance(Child(), Parent))      # True


# Concrete Methods in Abstract Base Classes
"""
    Concrete classes contains only concrete (Normal) methods whereas abstract
classes may contain both concrete methods and abstract methods.
        The concrete class provides an implementation of abstract methods, the
abstract base class can also provide an implementaion by invoking the methods
via 'super()'.
"""
# Program invoking a method using 'super()'
from abc import ABC


class R(ABC):
    def rk(self):
        print("Abstract Base Class.")


class K(R):
    def rk(self):
        super().rk()
        print("Sub Class")


# Driver Code
r = K()
r.rk()

# Output :
# Abstract Base Class.
# Sub Class


# Abstract Properties in Python
"""
    Abstract classes include attributes in addition to methods, you can
require the attributes in concrete classes by defining them with
@abstractproperty.
"""
# Program to show abstract properties
import abc
from abc import ABC, abstractmethod


class Parent(ABC):
    @abc.abstractproperty
    def show(self):
        return "Parent Class"


class Child(Parent):
    @property
    def show(self):
        return "Child Class"


try:
    p = Parent()
    print(p.show)
except Exception as err:
    print(err)

c = Child()
print(c.show)

# Output :
# Can't instantiate abstract class Parent with abstract methods show
# Child Class

"""
In the above example, the base class cannot be instantiated because it has only
an abstract version of the property-getter method.

    An abstract class is not a concrete class, it cannot be instantiated. When
we create an object for the abstract class it raises an Error.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


c=Animal()

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-13\tempCodeRunnerFile.py",
# line 30, in <module>
#     c=Animal()
# TypeError: Can't instantiate abstract class Animal with abstract methods move
