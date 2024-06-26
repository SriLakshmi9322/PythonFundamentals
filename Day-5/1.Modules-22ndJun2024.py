# Importing math module
import math

# Built-in Functions and Modules in Python
"""
The Python interpreter has a number of built-in functions.
They are loaded automatically as interpreter starts and are always available.
For Example : print() and input() for I/O, number conversion functions int(),
float() & complex(), data type conversions list(), tuple(), set() etc.,
In addition to built-in functions, a large number of pre-defined functions are
also available as a part of libraries bundled with Python distributions.
These functions are defined as 'modules'.
A 'Module' is a file containing definitions of functions, classes, variables,
constants or any other Python Objects. Contents of this file can be made for
the availability to any other Program. The standard library also contains many
Python scripts(with the '.py' extention) containing useful utilities.
To check the bult-in modules open python command prompt and type
>>> help('modules')
"""

# (i) Python - Math Module :
"""
Some of the most popular mathematical functions are defined in the 'math'
module.
This module includes trigonometric functions, representation functions,
logarithmic functions, angle conversion functions, etc.,
In addition, two mathematical constants are also defined in this module
1. Pie (𝜋) - defined as the ratio of the circumference to the diameter of a
circle and it's value is 3.141592653589793
2. e (Euler's number) - It is a base of the natural logarithm and it's
value is 2.718281828459045

"""

print(math.pi)          # 3.141592653589793
print(math.e)           # 2.718281828459045

# Angle Conversion functions : degrees() and radians()
print(math.radians(30))         # 0.5235987755982988
print(math.degrees(math.pi/6))  # 29.999999999999996

# Trigonometric functions for 30 degrees(0.5235987755982988 radians) :
# sin(), cos() & tan()
print(math.sin(0.5235987755982988))     # 0.49999999999999994
print(math.cos(0.5235987755982988))     # 0.8660254037844387
print(math.tan(0.5235987755982988))     # 0.5773502691896257

# Logarithmic functions : log(), log10(), exp(), pow(), sqrt()
# math.log() - returns the natural logarithm of a gicen number (to the base e)
print(math.log(10))                     # 2.302585092994046

# math.log10() - returns the base-10 logarithm of the given number.
# It is called the Standard logarithm.
print(math.log10(10))                   # 1.0

# math.exp() - returns a float number after raising e (math.e) to given number.
# In other words, exp(x) fives e**x.
print(math.exp(10))                     # 22026.465794806718
print(math.e ** 10)                     # 22026.465794806718

# math.pow() - returns the exponential value of two numbers in float type
print(math.pow(2, 4))                   # 16.0
print(2 ** 4)                           # 16

# math.sqrt() - returns the square root of a given number.
print(math.sqrt(100))                   # 10.0
print(math.sqrt(3))                     # 1.7320508075688772

# Representation functions : ceil(), floor()
# math.ceil() - approaximates the ggiven number to the smallest number,
# greater than or equal to the given floating point number.
print(math.ceil(4.5867))                # 5

# math.floor() - returns the largest integer less than or equal to the
# given number.
print(math.floor(4.5687))               # 4
