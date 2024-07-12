# ValueError
"""
ValueError: This exception is raised when a function or method is called with
            an invalid argument or input, such as trying to convert a string
            to an integer when the string does not represent a valid integer.
"""


# Example-1 :
def printAge(age):
    print(int(age))


age = "Twenty One"
printAge(age)

# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 13, in <module>
#     printAge("Twenty One")
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 11, in printAge
#     print(int(age))
# ValueError: invalid literal for int() with base 10: 'Twenty One'

# Solution :
try:
    def printAge(age):
        print(int(age))

    age = "Twenty One"
    printAge(age)
except ValueError:
    print("Error: Invalid Arguement cannot convert str to int")

# Output :
# Error: Invalid Arguement cannot convert str to int

# Example-2 :
import math

x = int(input("Enter a Positive Number : "))
print(f"Square root of {x} is {math.sqrt(x)}")

# Output :
# Enter a Positive Number : -100
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 4, in <module>
#     print(math.sqrt(x))
# ValueError: math domain error

# Solution :
import math

x = int(input("Enter a Positive Number : "))
try:
    print(f"Square root of {x} is {math.sqrt(x)}")
except ValueError:
    print(f"You entered {x}, Which is not a positive number...")

# Output :
# Enter a Positive Number : -100
# You entered -100, Which is not a positive number...
