# Tuple - Group of heterogeneous objects in sequence
# This is immutable (modifications are not allowed)
# Declared within the paranthesis - ()
# Insertion order is preserved, it means in which order we inderted
# the objects, the same order output is printed
# The Tuple contains both Forward indexing & Backward Indexing

# Forward Indexing
# |
# -->  0   1   2   3   4
#    ____________________
#   |_1_|_2_|_3_|_4_|_5_|
#    -5  -4  -3  -2  -1 <--
#                         |
#         Backward Indexing


# Tuple Data
tup1 = ('Sri', 'Manzoo', 'Pani')
tup2 = (1, 2, 3, 4, 5)
tup3 = 'a', 'b', 'c', 'd'               # Valid, But not Recommended
tup4 = ()
tup5 = (10)
tup6 = (10,)
tup7 = (1, 2, 3, 'Sri', 10.5)

print(tup1)                             # ('Sri', 'Manzoo', 'Pani')
print(tup2)                             # (1, 2, 3, 4, 5)
print(tup3)                             # ('a', 'b', 'c', 'd')
print(tup4)                             # ()
print(type(tup5))                       # <class 'int'>
print(type(tup6))                       # <class 'tuple'>
print(tup7)                             # (1, 2, 3, 'Sri', 10.5)


# Tuple Methods : There are 2 methods.
# 1. count() - Returns the number of occurrences of a specified element.
tupl = (1, 2, 3, 1, 1, 2, 3, 5, 4, 1)
print(tupl.count(1))                    # 4

# 2. index() - Returns the index value of specified element in the tuple.
tupl1 = ('SriLakshmi', 99, 5.4, 10+5j, 99)
print(tupl1.index('SriLakshmi'))        # 0
print(tupl1.index(99, 3))               # 4


# Tuple Unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print("Unpacked Elements : ", end="")
print(x, y, z, sep=", ")
