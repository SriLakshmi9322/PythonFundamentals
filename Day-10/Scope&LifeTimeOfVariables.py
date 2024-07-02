# Scope & Lifetime of Variables :
""" Scope of a variable is the portion of a program where the variable is
recognized. Parameters and variables defined inside a function are not visible
from outside the function. Hence, they have a local scope.
The lifetime of a variable is the period throughout which the variable exists
in the memory. The lifetime of variables inside a function is as long as the
function executes.
They are destroyed once we return from the function. Hence, a function does not
remember the value of a variable from its previous calls. """
# Example :


def my_fun():
    x = 10
    print("Value inside function :", x)


x = 20
my_fun()
print("Variable outside function :", x)
# Output :
# Value inside function : 10
# Variable outside function : 20


# Python Global, Local & Nonlocal variables
""" 1. Global Variables : In Python, a variable declared outside of the
function or in global scope is known as a Global Scope. This means that a
global variable can be accessed inside or outside of the function. """
# Example-1 :

x = "global"


def my_function():
    print("x inside :", x)


my_function()
print("x outside :", x)
# Output :
# x inside : global
# x outside : global


# Example-2 : When we want to change the value of x inside a function
x = 'global'


def my_function1():
    x = x * 2
    print(x)


my_function1()
# Output :
# UnboundLocalError: local variable 'x' referenced before assignment


# Example-3 : Changing Global Variable from inside a Function using global.
c = 0               # global variable


def addition():
    global c
    c = c + 2       # increment by 2
    print("Inside addition() :", c)


print("Before In main :", c)
addition()
print("In main :", c)
# Output :
# Before In main : 0
# Inside addition() : 2
# In main : 2


""" 2. Local Variables : A variable declared inside the function's body or in
the local scope is known as a local variable. """
# Example-1 : Accessing local variable outside the scope.


def func():
    y = "local"


func()
print(y)
# Output :
# NameError: name 'y' is not defined


# Example-2 : Create a Local Variable.


def my_function2():
    y = "local"
    print(y)


my_function2()                  # local


# Example-3 : Global and local variables.
x = "global "


def my_function3():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)


my_function3()
# Output :
# global global
# local


# Example-4 : Global Variable & Local Variable with same name
x = 5


def my_function4():
    x = 10
    print("local x :", x)


my_function4()
print("global x :", x)
# Output :
# local x : 10
# global x : 5
