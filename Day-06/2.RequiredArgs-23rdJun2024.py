# Function with Required Arguements
# Required Arguements are the mandatory arguements of a function.
# These arguement values must be passed in correct number and order
# during function call.

# Example :


def add_function(a, b):
    print(a + b)


add_function(10, 20)
add_function(10.5, 20.4)
add_function('SriLakshmi', 'Tiramsetti')
add_function(10, 10.5)
# add_function('Bhavani', 10)
# TypeError: can only concatenate str (not "int") to str

# Output :
# 30.9
# SriLakshmiTiramsetti
# 20.5
