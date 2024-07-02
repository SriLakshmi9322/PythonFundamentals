import math
import math as m
from statistics import *
from math import pi, e

# There are various ways to import modules.
""" They are :
1. Python import Statement
2. import with renaming
3. Python from...import statement
4. import all names """


# 1. Python import Statement :
""" We can import a module using the import statement and access the
definitions inside it using the dot (.) operator. """
# Example : using 'import math'
print("The value of PI is ", math.pi)
# Output : The value of PI is  3.141592653589793


# 2. import with renaming :
""" We can import a module by renaming it. We have renamed the math module as
m. This can save us typing time in some cases.
Note : That the name math is not recognized in our scope. Hence, math.pi is
invalid, and m.pi is the correct implementation. """
# Example-1 : using 'import math as m'
print("The value of PI is ", m.pi)
# Output : The value of PI is  3.141592653589793


# 3. Python from...import statement :
""" We can import specific names from a module without importing the module as
a whole. Here, we imported only the pi attribute from the math module. In such
cases, we don't use the dot (.) operator. """
# Example-1 : Using 'from math import pi'
print("The value of PI is ", pi)
# Output : The value of PI is  3.141592653589793

# Example-2 :We can also import multiple attributes as 'from math import pi, e'
print("The value of PI is ", pi)
print("The value of e is ", e)
# Output :
# The value of PI is  3.141592653589793
# The value of e is  2.718281828459045


# 4. import all names :
""" We can import all names (definitions) from a module. We can import all the
definitions from the math module. This includes all names visible in our scope
except those beginning with an underscore (private definitions).
Importing everything with the asterisk (*) symbol is not a good programming
practice. This can lead to duplicate definitions for an identifier. It also
hampers the readability of our code. """
# Example : Using 'from statistics import *'
data = [1, 2, 3, 4, 5]

mean_value = mean(data)
print(mean_value)
