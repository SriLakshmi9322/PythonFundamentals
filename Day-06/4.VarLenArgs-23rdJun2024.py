# Function with Variable length Arguements
"""
This is very useful when we do not know the exact number of arguements
that will be passed to a function.
Or we can have a design where any number of arguements can be passed
based on the requirement.
"""

# Example :


def display_arguements(*var):
    for i in var:
        print('Variable Arguement :', i)


display_arguements()
display_arguements(10, 20, 30)
display_arguements(10, 20.3, 'Bhavani')

# Output :
# Variable Arguement : 10
# Variable Arguement : 20
# Variable Arguement : 30
# Variable Arguement : 10
# Variable Arguement : 20.3
# Variable Arguement : Bhavani


# Arbitrary Keyword Arguements :
"""
In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable
number of arguments to a function using special symbols. There are two special
symbols:
1. *args in Python (Non-Keyword Arguements)
2. **kwargs in Python (Keyword Arguements)
"""


# Example-1 : Variable length non-keyword arguements.
def myFun(*args):
    for arg in args:
        print(arg, end=" ")


myFun("Hello,", "Welcome", "to", "Programming.")

# Output : Hello, Welcome to Programming.


# Example-2 : Variable length Keyword Arguements.
def myFunc(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFunc(fname="SriLakshmi", lname="Tiramsetti", age=21)

# Output :
# fname == SriLakshmi
# lname == Tiramsetti
# age == 21
