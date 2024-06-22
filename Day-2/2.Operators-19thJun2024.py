# Operators are used to perform operations on variables & values.
# Python provides the operators in the following  groups :
# 1. Python Arithmetic Operators
# 2. Python Comparison/Relational Operators
# 3. Python Logical Operators
# 4. Python Assignment Operators
# 5. Python Identity Operators
# 6. Python Membership Operators
# 7. Python Bitwise Operators


# 1. Arithmetic operators - Basic operators
x, y = 15, 4

print('x + y =', x + y)         # x + y = 19 - Addition
print('x - y =', x - y)         # x - y = 11 - Subtraction
print('x * y =', x * y)         # x * y = 60 - Multiplication
print('x / y =', x / y)         # x / y = 3.75 - Division
print('x // y =', x // y)       # x // y = 3 - Floor Division
print('x ** y =', x ** y)       # x ** y = 50625 - Exponentiation
print('x modulo y is', x % y)   # x modulo y is 3 - Modulo (for remainder)


# 2. Comparision/Relational Operators - To compare two values,
# returns True/False according to condition
x, y = 5, 2

print('x > y is', x > y)        # x > y is True - Greater than
print('x >= y is', x >= y)      # x >= y is True - Greater than or Equal to
print('x < y is', x < y)        # x < y is False - Less than
print('x <= y is', x <= y)      # x <= y is False - Less than or Equal to
print('x == y is', x == y)      # x == y is False - Equal to
print('x != y is', x != y)      # x != y is True - Not Equal to


# 3. Logical Operators -  evaluate Boolean expressions and determine whether
# the entire expression is True or False based on the operator used.
x, y = True, False

# AND (Both values should be True to get True)
print('x and y is', x and y)        # x and y is False
# OR (Atleast on value should be True to get True)
print('x or y is', x or y)          # x or y is True
print('not x is', not x)            # not x is False - NOT (Opposite value)


# 4. Assignment Operator - To assign a new value to the variable
# by performing operations in an easy way

x = 5           # Assignment Operator
print('x value is', x)      # x value is 5
x += 5          # Addition Assignment Operator
print('x += 5 is', x)       # x += 5 is 10
y = 5
y -= 5          # Subtraction Assignment operator
print('y -= 5 is', y)       # y -= 5 is 0
z = 5
z *= 5          # Multiplication Assignment Operator
print('z *= 5 is', z)       # z *= 5 is 25
m = 5
m /= 2          # Division Assignment Operator
print('m /= 5 is', m)       # m /= 5 is 2.5
n = 5
n //= 2          # Floor Division Assignment Operator
print('n //= 5 is', n)       # n //= 5 is 2
p = 5
p %= 2          # Modulo Assignment Operator
print('p modulo= 5 is', p)       # p modulo= 5 is 1
q = 5
q **= 2          # Exponentiation Assignment Operator
print('q **= 5 is', q)       # q **= 5 is 25


# 5. Identity Operators - To check whether two operands are identical or not
# is - returns True if the operands are identical
# is not - returns True if the operands are not identical

x1, y1 = 5, 5           # Python creates same object for same integer values
print(id(x1))           # 140723072718624
print(id(y1))           # 140723072718624
print(x1 is y1)         # True
print(x1 is not y1)     # False

x2, y2 = 'sri', 'sri'   # Python creates same object for small strings
print(id(x2))           # 1640374397488
print(id(y2))           # 1640374397488
print(x2 is y2)         # True
print(x2 is not y2)     # False

x3, y3 = [1, 2, 3], [1, 2, 3]
# Python creates differect a new object to each list (mutable)
print(id(x3))           # 1640374357440
print(id(y3))           # 1640374357952
print(x3 is y3)         # False
print(x3 is not y3)     # True
