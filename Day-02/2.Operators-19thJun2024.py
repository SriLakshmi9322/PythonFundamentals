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

# Example :
temp = 35

if temp >= 30:
    print("It's a Hot Day!")
elif temp <= 10:
    print("It's a Cold Day!")
else:
    print("It's neither Hot nor Cold!!")

# Output : It's a Hot Day!


# 3. Logical Operators -  evaluate Boolean expressions and determine whether
# the entire expression is True or False based on the operator used.
x, y = True, False

# AND (Both values should be True to get True)
print('x and y is', x and y)        # x and y is False
# OR (Atleast on value should be True to get True)
print('x or y is', x or y)          # x or y is True
print('not x is', not x)            # not x is False - NOT (Opposite value)

# Example-1 : To Build an application for processing loans based on 2 condition
# Loan can be applicable when the user has both high income and good credit.
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for Loan!")

# Output : Eligible for Loan!

# Example-2 :
# Loan can be applicable when the user has either high income or good credit.
has_high_income1 = True
has_good_credit1 = False

if has_high_income1 or has_good_credit1:
    print("Eligible for Loan!")

# Output : Eligible for Loan!

# Example-3 : If applicant has good credit and doesn't have a criminal record
has_good_credit2 = True
has_criminal_record = False

if has_good_credit2 and not has_criminal_record:
    print("Eligible for Loan!")

# Output : Eligible for Loan!


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

a = 10
b = 5
x = a
y = b
z = a
print(x is y)           # False
print(x is a)           # True
print(y is b)           # True
print(x is not y)       # True
print(x is not a)       # False
print(x is z)           # True


# 6. Membership Operators - To test whether a value or variable is a
# member of a sequence, such as a string, list, or tuple.
# in - returns True if a character or the entire substring is present in the
#      specifies string, otherwise False
# not in - returns True if a character or entire substring does not exist in
#          the specified string, otherwise False

str1 = 'ramuIT'
str2 = 'tirumalaCSE'
str3 = 'ramu'
str4 = 'tirumala'

print(str3 in str1)                 # True
print(str4 in str2)                 # True
print(str3 in str2)                 # False
print('ratan' in 'ratanIT')         # True
print('ratan' in 'durgaSOFT')       # False
print(str3 not in str1)             # False
print(str4 not in str2)             # False
print(str3 not in str2)             # True
print('ratan' not in 'ratanIT')     # False
print('ratan' not in 'anu')         # True


# 7. Bitwise Operators - To perform bitwise calculations on integers.
# The integers will be converted into binary format later
# operations are performed bit by bit.

print(3 & 7)        # 3 - Bitwise AND
print(9 & 6)        # 0
print(15 & 15)      # 15
print(0 & 0)        # 0
print(3 | 7)        # 7 - Bitwise OR
print(9 | 6)        # 15
print(15 | 15)      # 15
print(0 | 0)        # 0
print(~ 7)          # -8 - Bitwise NOT
print(3 ^ 7)        # 4 - Bitwise XOR
print(3 >> 1)       # 1 - Bitwise RightShift
print(3 << 1)       # 6 - Bitwise LeftShift
