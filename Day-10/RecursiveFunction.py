# Recursive Functions :
""" A function that calls itself is known as Recursive Function.
A Physical world example would be to place two parallel mirrors facing each
other. Any object in between them would be reflected recursively.
The following image shows the working of a recursive function called recurse.
"""
# Example :
# Factorial of a number is the product of all the integers from 1 to that
# number.
# The factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720


def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))


num = 6
print("The factorial of", num, "is", factorial(num))
# Output : The factorial of 6 is 720
