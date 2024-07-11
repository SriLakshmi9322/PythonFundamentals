# IndexError
"""
IndexError: This exception is raised when an index is out of range for a
            list, tuple, or other sequence types.
"""

# Example-1 : In sequence type - Lists.
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The list is:", myList)
index = 10
element = myList[index]
print("Element at index {} is {}".format(index, element))

# Output :
# The list is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
#   line 5, in <module>
#     element = myList[index]
# IndexError: list index out of range

# Solution-1 : Using if-else Block.
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The list is:", myList)
index = 10
if index < len(myList):
    element = myList[index]
    print("Element at index {} is {}".format(index, element))
else:
    print("Index Shold be Smaller...")

# Output :
# The list is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Index Shold be Smaller...

# Solution-2 : Using try-except Block.
try:
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("The list is:", myList)
    index = 10
    element = myList[index]
    print("Element at index {} is {}".format(index, element))
except IndexError:
    print("Error: List Index Out of Range...")

# Output :
# The list is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Error: List Index Out of Range...


# Example-2 : In sequence type - Tuple.
myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("The Tuple is:", myTuple)
index = 10
element = myTuple[index]
print("Element at index {} is {}".format(index, element))

# Output :
# The Tuple is: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
#   line 5, in <module>
#     element = myTuple[index]
# IndexError: tuple index out of range

# Solution-1 : Using if-else Block.
myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("The Tuple is:", myTuple)
index = 10
if index < len(myTuple):
    element = myTuple[index]
    print("Element at index {} is {}".format(index, element))
else:
    print("Index Should be Smaller...")

# Output :
# The Tuple is: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Index Should be Smaller...

# Solution-2 : Using try-except Block.
try:
    myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("The Tuple is:", myTuple)
    index = 10
    element = myTuple[index]
    print("Element at index {} is {}".format(index, element))
except IndexError:
    print("Error: Index Out of Range...")

# Output :
# The Tuple is: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Error: Index Out of Range...
