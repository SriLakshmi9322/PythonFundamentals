# List - A container data type that stores a sequence of elements.
# Unlike strings, lists are mutable: modification possible.
# A Python List is enclosed between square brackets
# In list insertion order is preserved, It means in which order we
# inserted element the same order output is printed
# A list can be composed by storing a sequence of different type of
# values separated by commas
# <list_name> = [value1,value2,...,valuen]
# List have both forward indexing & backward indexing

# Forward Indexing
# |
# -->  0   1   2   3   4
#    ____________________
#   |_1_|_2_|_3_|_4_|_5_|
#    -5  -4  -3  -2  -1 <--
#                         |
#         Backward Indexing

# List Data
data1 = [1, 2, 3, 4]                    # List of Integers
data2 = ['abc', 'xyz', 'jkl']           # List of Strings
data3 = [12.5, 11.6]                    # List of Floats
data4 = []                              # Empty List
data5 = ['Sri', 99, 56.4, 'a']          # List with mixed data types

# Accessing List data
dt1 = [1, 2, 3, 4]
dt2 = ['Sri', 'Manzoo', 'Pani']

print(dt1[0])
print(dt1[0:3])
print(dt2[-3:-1])
print(dt1[0:])
print(dt2[:2])
print(dt2[:])

# Output :
# 1
# [1, 2, 3]
# ['Sri', 'Manzoo']
# [1, 2, 3, 4]
# ['Sri', 'Manzoo']
# ['Sri', 'Manzoo', 'Pani']

# List methods
# To add elements into the list we've 3 ways

# 1. Using append method - it is very fast
lt = [1, 2, 3, 4]
lt.append(99)
print(lt)                               # [1, 2, 3, 4, 99]

# 2. Using insert method
lt1 = [1, 2, 3, 4]
lt1.insert(2, 5)                        # 2 - index, 5 - value
print(lt1)                              # [1, 2, 5, 3, 4]

# 3. Using list concatenation
lt2 = [1, 2, 2] + [4]
print(lt2)                              # [1, 2, 2, 4]


# To Remove element from the list
lt3 = [1, 2, 3, 4, 5]
lt3.remove(3)
print(lt3)                              # [1, 2, 4, 5]


# To reverse the order of list elements
lt4 = [1, 2, 3, 4, 5]
lt4.reverse()
print(lt4)                              # [5, 4, 3, 2, 1]


# To sort a list
lt5 = [5, 6, 2, 99, 16]
lt5.sort()
print(lt5)                              # [2, 5, 6, 16, 99]


# To Search element by using index values
lt6 = [2, 2, 4]
print(lt6.index(2))                     # 0

lt7 = [2, 2, 4]
# To search from the list after a specific index value
print(lt7.index(2, 1))                  # 1


# Stack - Python lists can be used intuitively as
# stacks via the two list operations append() and pop().
# append method adds element at the end of the list
# pop method removes element from the end of the list
# Which follows the "LIFO"-"Last In First Out" operation
stack = [3, 99, 12]
print(stack)                            # [3, 99, 12]
stack.append(42)
print(stack)                            # [3, 99, 12, 42]
stack.pop()
print(stack)                            # [3, 99, 12]
stack.pop()
print(stack)                            # [3, 99]
