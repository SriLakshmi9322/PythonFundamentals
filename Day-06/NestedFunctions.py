# Python Inner Functions
"""
A Function which is defined inside another function is known as 'Inner
Functions' or 'Nested Functions'.
Nested Functions are able to access variables of the enclosing scope. Inner
functions are used so that they can be protected from everything happening
outside the function. This process is also known as Encapsulation.
"""


# Example :
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()


if __name__ == '__main__':
    outerFunction('Hey!')

# Output : Hey!


# Scope of Variable in Nested Function :
"""
The location where we can find a variable and also access it if required is
called the scope of a variable. It is known how to access a "global variable"
inside a function.
"""


# Accessing of variables of Nested Functions.
def fun1():
    s = "I Love Programming."

    def fun2():
        print(s)

    fun2()


fun1()

# Output : I Love Programming.


# Changing the variable of the Outer Function.
def fun1():
    s = "I Love Programming."

    def fun2():
        s = "Me too."
        print(s)

    fun2()
    print(s)


fun1()

# Output :
# Me too.
# I Love Programming.

"""
In the above program, Variable of the outer function is not changed. It can be
changed. There are many ways to change the value of the variable of the outer
Function.
"""


# 1. Using an Iterable :
def fun1():
    s = ["I Love Programming."]

    def fun2():
        s[0] = "Me too."
        print(s)

    fun2()
    print(s)


fun1()

# Output :
# ['Me too.']
# ['Me too.']


# 2. Using nonlocal Keyword :
def fun1():
    s = "I Love Programming."

    def fun2():
        nonlocal s
        s = "Me too"
        print(s)

    fun2()
    print(s)


fun1()

# Output :
# Me too
# Me too


# 3. Also can be done like this :
def fun1():
    fun1.s = "I Love Programming."

    def fun2():
        fun1.s = "Me too."
        print(fun1.s)

    fun2()
    print(fun1.s)


fun1()

# Output :
# Me too.
# Me too.
