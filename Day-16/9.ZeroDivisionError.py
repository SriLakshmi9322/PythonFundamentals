# ZeroDivisionError
"""
ZeroDivisionError: This exception is raised when an attempt is made to
                   divide a number by zero.
"""


# Example :
def divisionOperation(numerator, denominator):
    result = numerator / denominator
    return f"Result is {result}"


numerator = int(input("Enter the numerator : "))
denominator = int(input("Enter the denominator : "))

print(divisionOperation(numerator, denominator))

# Output-1 :
# Enter the numerator : 100
# Enter the denominator : 10
# Result is 10.0

# Output-2 :
# Enter the numerator : 100
# Enter the denominator : 0
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-16\tempCodeRunnerFile.py",
# line 9, in <module>
#     print(divisionOperation(numerator, denominator))
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-16\tempCodeRunnerFile.py",
# line 2, in divisionOperation
#     result = numerator / denominator
# ZeroDivisionError: division by zero


"""
We can solve this problem in 3 ways :
1. Using if-else Block
2. Using try-except Block
3. Using Conditional Expression
"""


# Solution-1 : Using if-else Block.
def divisionOperation(numerator, denominator):
    if denominator != 0:
        result = numerator / denominator
    else:
        return "Denominator cannot be zero.!"
    return f"Result is {result}"


numerator = int(input("Enter the numerator : "))
denominator = int(input("Enter the denominator : "))

print(divisionOperation(numerator, denominator))

# Output :
# Enter the numerator : 100
# Enter the denominator : 0
# Denominator cannot be zero.!


# Solution-2 : Using try-except block.
def divisionOperation(numerator, denominator):
    result = numerator / denominator
    return f"Result is {result}"


numerator = int(input("Enter the numerator : "))
denominator = int(input("Enter the denominator : "))

try:
    print(divisionOperation(numerator, denominator))
except ZeroDivisionError:
    print("Error: Denominator cannot be Zero.!!")

# Output :
# Enter the numerator : 100
# Enter the denominator : 0
# Error: Denominator cannot be Zero.!!


# Solution-3 : Using Conditional Expression.
def divisionOperation(num, den):
    result = num / den if den != 0 else "Error: Denominator cannot be zero"
    return f"Result is {result}"


numerator = int(input("Enter the numerator : "))
denominator = int(input("Enter the denominator : "))

print(divisionOperation(numerator, denominator))

# Output :
# Enter the numerator : 100
# Enter the denominator : 0
# Result is Error: Denominator cannot be zero
