# DuckTyping in Python
"""
Duck Typing is a type system used in dynamic languages. For example, Python,
Perl, Ruby, PHP, Javascript, etc. where the type or the class of an object is
less important than the method it defines. Using Duck Typing, we do not check
types at all. Instead, we check for the presence of a given method or
attribute.
"""


# Program to demonstrate Duck Typing
class SpecialString:
    def __len__(self):
        return 21


# Driver Code
if __name__ == '__main__':
    string = SpecialString()
    print(len(string))

# Output : 21


# Program to demonstrate how an object be used in any other circumstances
# until it is not supported.
class Bird:
    def fly(self):
        print("Fly with Wings!")


class Airplane:
    def fly(self):
        print("Fly with Fuel!")


class Fish:
    def swim(self):
        print("Fish swims in Sea!")


# Attributes having same name are considered as DuckTyping
for obj in Bird(), Airplane(), Fish():
    obj.fly()


# Output :
# Fly with Wings!
# Fly with Fuel!
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-13\tempCodeRunnerFile.py",
#  line 20, in <module>
#     obj.fly()
# AttributeError: 'Fish' object has no attribute 'fly'
