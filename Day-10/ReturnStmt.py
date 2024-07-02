# The return statement :
""" The return statement is used to exit a function and go back to the place
from where it was called.
This statement can contain an expression that gets evaluated and the value is
returned.
If there is no expression in the statement or the return statement itself is
not present inside a function, then the function will return the None object.
Syntax of return : return [expression_list] """
# Example-1 :


def greet(name):
    print("Hello, " + name + ". Good Morning!")


print(greet("SriLakshmi"))
# Output :
# Hello, SriLakshmi. Good Morning!
# None


# Example-2 :


def absolute_value(num):
    """This function returns the absolute value of the entered number"""
    if num > 0:
        return num
    else:
        return -num


print(absolute_value(2))                # 2
print(absolute_value(-4))               # 4
