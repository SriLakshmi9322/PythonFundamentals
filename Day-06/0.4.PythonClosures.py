# Python Closures
"""
A Closure is a function object that remembers values in enclosing scopes even
if they are not present in memory.
1. It is a record that stores a function together with an environment: a
   mapping associating each free variable of the function (Variables that are
   used locally, but defined in an enclosing scope) with the value or reference
   to which the name was bound when the closure was created.
2. A closure (unlike a plain function) - allows the function to access those
   captured variables through the closure's copies of their values or
   reference, even when the function is invoked outside their scope.
"""


# Example :
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    # Note : We are returning function WITHOUT parenthesis
    return innerFunction


if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()

# Output : Hey!

"""
As observed, 'closures' help to invoke function outside their scope.
    The function innerFunction has its scope only inside the outerFunction. But
with the use of closures we can easily extend its scope to invoke a function
outside its scope.
"""


# To illustrate closures
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguements {}'.
            format(func.__name__, args))
        print(func(*args))
    # Necessary for closure to work (returning WITHOUT parenthesis)

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)
sub_logger(10, 5)
sub_logger(20, 10)

# Output :
# 6
# 9
# 5
# 10
