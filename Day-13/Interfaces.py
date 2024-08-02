# Interface
"""
    In object-oriented languages like Python, the interface is a collection of
method signatures that should be provided by the implementing class.
Implementing an interface is a way of writing an organized code and achieve
abstraction.

The package zope.interface provides an implementation of "object interfaces"
for Python. It is maintained by the Zope Toolkit project. The package exports
two objects, 'Interface' and 'Attribute' directly. It also exports several
helper methods. It aims to provide stricter semantics and better error
messages than Python's built-in abc module.

Declaring Interface :
    An Interface is defined using Python class statements and is a sub_class of
'interface.Interface' which is the Parent interface for all interfaces.
Syntax :
class IMyInterface(zope.interface.Interface):
    # Methods & Attributes
"""
import zope.interface


class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute('foo')

    def method1(self, x):
        pass

    def method2(self):
        pass


print(type(MyInterface))
print(MyInterface.__module__)
print(MyInterface.__name__)

# Get Attribute
x = MyInterface['x']
print(x)
print(type(x))

# Output :
# <class 'zope.interface.interface.InterfaceClass'>
# __main__
# MyInterface
# __main__.MyInterface.foo
# <class 'zope.interface.interface.Attribute'>


"""
Implementing Interface :
    The interface acts as a Blueprint for designing classes, so interfaces are
implemented using the implementer decorator on the class. If a class implements
an interface, then the instance of the class provide the interface. Objects can
provide interfaces directly, in addition to what their classes implement.
Syntax :
@zope.interface.implementer(*interfaces)
class Class_Name:
    # Methods
"""
import zope.interface


class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute('value')

    def method1(self, x):
        pass

    def method2(self):
        pass


@zope.interface.implementer(MyInterface)
class MyClass:
    def method1(self, x):
        return x**2

    def method2(self):
        return "value"


obj1 = MyClass()
print(obj1.method1(5))
print(obj1.method2())
# We declared that 'MyClass' implements 'MyInterface'. This means that
# instances of 'MyClass' provide 'MyInterface'.

# Output :
# 25
# value


# Program that demonstrates Interface Methods
import zope.interface


class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute("Value")

    def method1(self, x, y, z):
        pass

    def method2(self):
        pass


@zope.interface.implementer(MyInterface)
class MyClass:
    def method1(self, x):
        return x ** 2

    def method2(self):
        return "Value"


obj = MyClass()

# To ask an interface whether it is implemented by a class
print(MyInterface.implementedBy(MyClass))

# MyClass does not provide MyInterface but implements it
print(MyInterface.providedBy(MyClass))

# To ask whether an interface is provided by an object
print(MyInterface.providedBy(obj))

# To ask what interfaces are implemented by a class
print(list(zope.interface.implementedBy(MyClass)))

# To ask what interfaces are provided by an object
print(list(zope.interface.providedBy(obj)))

# Class does not provide interface
print(list(zope.interface.providedBy(MyClass)))

# Output :
# True
# False
# True
# [<InterfaceClass __main__.MyInterface>]
# [<InterfaceClass __main__.MyInterface>]
# []


# Interface Inheritance
"""
Interfaces can extend other interfaces by listing the other interfaces as base
interfaces.
Functions:
1. extends(interface) : Returns Boolean value, whether one interface extends
   another.
2. isOrExtends(interface) : Returns Boolean value, whether interfaces are same
   or one extends another.
3. isEqualOrExtendedBy(interface) : Returns Boolean value, whether interfaces
   are same or one is extended by another.
"""
import zope.interface


class BaseI(zope.interface.Interface):
    def m1(self, x):
        pass

    def m2(self):
        pass


class DerivedI(BaseI):
    def m3(self, x, y):
        pass


@zope.interface.implementer(DerivedI)
class Cls:
    def m1(self, z):
        return z ** 3

    def m2(self):
        return "Value"

    def m3(self, x, y):
        return x ^ y


# To get Base Interfaces
print(DerivedI.__bases__)

# To ask whether BaseI extends DerivedI
print(BaseI.extends(DerivedI))

# To ask whether BaseI is equal to or extended by DerivedI
print(BaseI.isEqualOrExtendedBy(DerivedI))

# To ask whether BaseI is equal to or extends DerivedI
print(BaseI.isOrExtends(DerivedI))

# To ask whether DerivedI is equal to or extends BaseI
print(DerivedI.isOrExtends(DerivedI))

# Output :
# (<InterfaceClass __main__.BaseI>,)
# False
# True
# False
# True
