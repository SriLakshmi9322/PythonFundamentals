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
