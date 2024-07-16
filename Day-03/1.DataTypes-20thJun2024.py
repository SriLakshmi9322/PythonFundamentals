# Data Type - Python Data Types are used to define the type of a variable.
# It defines what type of data we are going to store in a variable.
# In Python, We have 8 Data Types
# 1. Numbers
# 2. Boolean
# 3. String
# 4. Binary
# 5. Lists
# 6. Tuples
# 7. Sets
# 8. Dictionaries


# 1. Numbers - Describes the numeric value & decimal value
# These are immutable (modifications are not allowed)
# types : int, float, complex

a = 5               # int type
print(type(a))      # <class 'int'>

b = 7.3             # float type
print(type(b))      # <class 'float'>

c = 2 + 3j          # complex type
print(type(c))      # <class 'complex'>


# 2. Boolean - Represents True/False values
# 0 - False & 1 - True
# type : bool
# Logical Operators AND, OR & NOT returns values of Boolean

bn = True
bl = False

print(bn)                       # True
print(bl)                       # False
print(type(bn))                 # <class 'bool'>
print(type(bl))                 # <class 'bool'>


# 3. Strings - Represent group/sequence of characters
# Strings can be declared within single(' ')/double(" ")/triple(''' ''') quotes
# type : str
# It is immutable (modifications are not allowed)

s = 'This is a string'          # using single quotes
t = "This is a string"          # using double quotes
r = '''This is a string'''      # using triple quotes

print(type(s))                  # <class 'str'>
print(type(t))                  # <class 'str'>
print(type(r))                  # <class 'str'>


# 4. Binary - Binary in Python includes bytes, bytearray, and memoryview
# These are used to work with binary data and memory views of binary data.
# types : bytes, bytearray, memoryview

b = bytes([65, 66, 67])
print(b)                        # b'ABC'
print(b[0])                     # 65
print(type(b))                  # <class 'bytes'>

ba = bytearray([65, 66, 67])
print(ba)                        # bytearray(b'ABC')
ba[0] = 68
print(ba)                        # bytearray(b'DBC')
print(type(ba))                  # <class 'bytearray'>

mv = memoryview(bytes([65, 66, 67]))
print(mv)                        # <memory at 0x000001BA01C43B80>
print(type(mv))                  # <class 'memoryview'>


# 5. Lists - Group of heterogeneous objects in sequence
# They are mutable (modifications are allowed)
# type : list
# Lists are declared within the square brackets - []

ls = [99, 'SriLakshmi', 2 + 3j, True]
print(ls)                        # [99, 'SriLakshmi', (2+3j), True]
print(type(ls))                  # <class 'list'>


# 6. Tuples - Group of heterogeneous objects in sequence
# This is immutable (modifications are not allowed)
# type : list
# Tuples are declared within the paranthesis - ()

tp = (99, 'SriLakshmi', 2 + 3j, False)
print(tp)                       # (99, 'SriLakshmi', (2+3j), False)
print(type(tp))                 # <class 'tuple'>


# 7. Sets - Group of heterogeneous objects in unordered
# This is mutable (modifications are allowed)
# type : set
# Sets are declared within curly braces - {}

week = {'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'}
print(week)                 # {'Thu', 'Sat', 'Tue', 'Wed', 'Sun', 'Fri', 'Mon'}
print(type(week))           # <class 'set'>


# 8. Dictionaries - It stores the data in key-value pairs format
# Keys must be unique
# It is mutable (modifications are allowed)
# type : dict
# Dictionaries are declared within the curly braces - {key:value}

dt = {1: 'One', 2: 'Two', 3: 'Three'}
print(dt)                       # {1: 'One', 2: 'Two', 3: 'Three'}
print(type(dt))                 # <class 'dict'>
