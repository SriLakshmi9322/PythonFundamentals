# Python Arrays
"""
An array is a collection of items stored in a contiguous memory locations.
Stores multiple items of same type together.
In order to create arrays in python, we need to import array module & with
the help of this module we can use the array method to create an array of
a specified type (integer, float...).
Synax :
import array
array_name = array.array(data_type, value_list)
"""

# Example-1 : Creating an array
import array

a = array.array('i', [1, 2, 3])     # 'i' - Integer type
print("The new created array is :", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")

print()
b = array.array('d', [2.5, 3.2, 3.3])       # 'd' - Double type
print("\nThe new created array is :", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")

# Output :
# The new created array is : 1 2 3

# The new created array is : 2.5 3.2 3.3


# Example-2 : Adding elements to an array
"""
We have 2 methods to add elements to an existing array.
1. insert() - To insert element at any index of an array
2. append() - To append value at the end of an array
"""
import array

a = array.array('i', [1, 2, 3])     # 'i' - Integer type
print("The new created array is :", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")

a.insert(1, 4)              # 1 - index, 4 - element
print("\nArray after insertion :", end=" ")
for element in a:
    print(element, end=" ")

print()
b = array.array('d', [2.5, 3.2, 3.3])       # 'd' - Double type
print("\nThe new created array is :", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")

b.append(4.4)           # Adds element at the end of the array
print("\nArray after append function :", end=" ")
for element in b:
    print(element, end=" ")

# Output :
# The new created array is : 1 2 3
# Array after insertion : 1 4 2 3

# The new created array is : 2.5 3.2 3.3
# Array after append function : 2.5 3.2 3.3 4.4


# Example-3 : Accessing elements from an array
import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])
print("Element at index 3 is :", a[0])
print("Element at index 4 is :", a[4])

# Output :
# Element at index 3 is : 1
# Element at index 4 is : 5


# Example - 4 : Removing elements from an array
"""
To remove an element from the array we have 2 methods :
1. remove() - Removes the first occured  specified element.
              (Error: If element does not exists in the array).
2. pop() - Removes an element of specified index value, by default it removes
           the last item from the array.
"""
import array as arr

a = arr.array('i', [1, 2, 3, 1, 5])
print("The popped element is :", end=" ")
print(a.pop(2))         # 2 - index value
print("The array after popping :", end=" ")
for ele in a:
    print(ele, end=" ")

a.remove(1)             # 1 - element
print("\nAfter removing element from the array :", end=" ")
for ele in a:
    print(ele, end=" ")

# Output :
# The popped element is : 3
# The array after popping : 1 2 1 5
# After removing element from the array : 2 1 5


# Example - 5: Slicing of an array
"""
To take a specific part of an array from an existing array we can use slice
operation. Slice operation is performed on an array using colon (:).
"""
import array as arr

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = arr.array('i', l)
sliced_array = a[3:8]
print(sliced_array)
sliced_array = a[5:]
print(sliced_array)
sliced_array = a[:]
print(sliced_array)

# Output :
# array('i', [4, 5, 6, 7, 8])
# array('i', [6, 7, 8, 9, 10])
# array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Example - 6: Searching for an element
# index() - Returns the index value of first occured specified element
import array as arr

a = arr.array('i', [1, 2, 3, 1, 2, 5])
print("Index of element 2 is :", a.index(2))           # 2 - element
print("Index of element 1 is :", a.index(1))

# Output :
# Index of element 2 is : 1
# Index of element 1 is : 0


# Example - 7 : Updating elements
import array as arr

a = arr.array('d', [1.5, 6.98, 3.65])
print("Array is :", end=" ")
for i in a:
    print(i, end=" ")

a[2] = 96.7
a[0] = 23.07
print("\nArray after updation :", end=" ")
for i in a:
    print(i, end=" ")

# Output :
# Array is : 1.5 6.98 3.65
# Array after updation : 23.07 6.98 96.7

# Different operations we can perform on an array
# 1. counting no. of occurrences of a specified element.
# Example :
import array as arr

a = arr.array('i', [1, 2, 3, 4, 2, 5, 2])
count = a.count(2)
print("Count of 2 is :", count)

# Output : Count of 2 is : 3

# 2. Reversing elements in an array
# Example :
import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])
print("The array is :", end=" ")
for i in a:
    print(i, end=" ")

a.reverse()
print("\nArray after reversing :", end=" ")
for i in a:
    print(i, end=" ")

# Output :
# The array is : 1 2 3 4 5
# Array after reversing : 5 4 3 2 1

# 3. Extending an array
# Example :
import array

a = array.array('i', [1, 2, 3, 4, 5])
a.extend([6, 7, 8, 9, 10])      # [6, 7, 8, 9, 10] - list
print("Array after extending with a list :", end=" ")
for i in a:
    print(i, end=" ")

# Output : Array after extending with a list : 1 2 3 4 5 6 7 8 9 10


# Other functions
import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])
print("Size of the array is :", a.itemsize)     # Size in Bytes
print("Address and length of the array is :", a.buffer_info())
a.fromlist([6, 7, 8])
print("Appending list[6, 7, 8] to the array :", end=" ")
for i in a:
    print(i, end=" ")

print("\nTranforming array into a list :", a.tolist())

# Output :
# Size of the array is : 4
# Address and length of the array is : (2699818858608, 5)
# Appending list[6, 7, 8] to the array : 1 2 3 4 5 6 7 8
# Tranforming array into a list : [1, 2, 3, 4, 5, 6, 7, 8]
