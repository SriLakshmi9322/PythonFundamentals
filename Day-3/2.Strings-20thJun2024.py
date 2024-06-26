# Strings - Sequence of characters
# There are 3 ways to create a string

# 1. Using single quotes (' ')
str1 = 'SriLakshmi Tiramsetti'
print(str1)                     # SriLakshmi Tiramsetti
print(type(str1))               # <class 'str'>

# 2. Using double quotes (" ")
str2 = "SriLakshmi Tiramsetti"
print(str2)                     # SriLakshmi Tiramsetti
print(type(str2))               # <class 'str'>

# 3. Using triple quotes (''' ''')
str3 = '''SriLakshmi Tiramsetti'''
print(str3)                     # SriLakshmi Tiramsetti
print(type(str3))               # <class 'str'>


# String method - We can convert another type of values into string type

i = 99
str4 = str(i)
print(str4)                     # 99
print(type(str4))               # <class 'str'>

f = 49.5
str5 = str(f)
print(str5)                     # 49.5
print(type(str5))               # <class 'str'>

c = 3 + 6j
str6 = str(c)
print(str6)                     # (3+6j)
print(type(str6))               # <class 'str'>

bn = True
str7 = str(bn)
print(str7)                     # True
print(type(str7))               # <class 'str'>


# We can use whitespace characters(\n, \t) in strings

print('SriLakshmi\nTiramsetti')
# Output:
# SriLakshmi
# Tiramsetti

print('SriLakshmi\tTiramsetti')         # SriLakshmi      Tiramsetti


# Indexing and Slicing
# String index starts from 0,
# trying to access character out of index range will generate "IndexError"
# negative indexing also allowed
# H    e    l    l    o
# 0    1    2    3    4 : Positive Indexing
# -5  -4   -3   -2   -1 : Negative Indexing

# Slice Notation
st = 'Hello'
print(st[0:5])                  # Hello - (0 - Start Index, 5 - End Index)

# Start & End Index is optional, by default it takes the 0 as a Start index &
# length of the string as a End Index
st = 'Hello'
print(st[:])                    # Hello
# We can give index range to get substring from the original string
print(st[1:4])                  # ell
# If we give end index more than the length of the string,
# it will consider it's length
print(st[1:100])                # ello
print(st[-4])                   # e
print(st[:-3])                  # He
print(st[-3:])                  # llo


# Most Important String Methods
name = "        My name is SriLakshmi      "

# To remove Whitespaces
print(name.strip())                     # My name is SriLakshmi

# To convert the string into Lower Case
print("SriLakshmi Tiramsetti".lower())  # srilakshmi tiramsetti

# To convert the string into Upper Case
print("SriLakshmi Tiramsetti".upper())  # SRILAKSHMI TIRAMSETTI

# To check whether the string starts with the specified substring or not
print("SriLakshmi Tiramsetti".startswith('Sri'))    # True

# To check whether the string ends with the specified substring or not
print("SriLakshmi Tiramsetti".endswith('tti'))      # True

# To find a specified substring in the current string
# This method returns the specified sub string's index value from the original
# If the substring is not present it will return -1
print("SriLakshmi Tiramsetti".find('ram'))          # 13

# To replace a sub string or a character in the current string
print("cheat".replace('ch', 'm'))                   # meat

# To combine a list of values by separating specified special symbol
print(','.join(['S', 'R', 'I']))                    # S,R,I

# To calculate the length of the string
print(len("SriLakshmi"))                            # 10

# To check the specified sub strings existance in the original string
print('Sri' in 'SriLakshmi')                        # True
