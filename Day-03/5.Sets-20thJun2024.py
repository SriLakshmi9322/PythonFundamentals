# Sets - A set is an  unordered collection with no duplicate elements
# It consists membership testing to eliminate duplicate entries
# Sets are declared using - {}
# If we want to create an empty set we need to use set method
# {} - do not create empty set
# Set objects also supports mathematical operations like union, intersection,
# difference & symmetric difference

# Set of integers
my_set = {1, 2, 3}
print(my_set)                       # {1, 2, 3}
print(type(my_set))                 # <class 'set'>

# To create an empty set
# s = {}                            # Default it creates dictionary
s = set()
print(s)                            # set()
print(type(s))                      # <class 'set'>

# Set of mixed data types
my_set1 = {1.0, 'Sri', (1, 2, 3)}
print(my_set1)                      # {1.0, (1, 2, 3), 'Sri'}
# When we run this file again - {1.0, 'Sri', (1, 2, 3)}

# It does not allow duplicate values
my_set2 = {1, 2, 3, 4, 3, 2}
print(my_set2)                      # {1, 2, 3, 4}

# To add elements to the set
my_set3 = {1, 2, 3, 4}
my_set3.add(99)
print(my_set3)                      # {1, 2, 99, 3, 4}

# To add more than one element to the set
my_set4 = {1, 2, 3, 4}
my_set4.update([99, 100])
print(my_set4)                      # {1, 2, 99, 3, 4, 100}

# To remove element from the set we have 2 methods : 1. discard() 2. remove()
# The difference between these function, using discard() function if the
# item does not exist in the set then the set remain unchanged whereas
# remove() method will through an error.
my_set5 = {1, 2, 3, 4, 5, 6}
my_set5.discard(5)
my_set5.discard(3)
my_set5.discard(8)                  # Remains unchanged
print(my_set5)                      # {1, 2, 4, 6}

my_set6 = {1, 2, 3, 4, 5, 6}
my_set6.remove(7)
my_set6.remove(1)
# my_set6.remove(8)                 # KeyError - element is not present
print(my_set6)                      # {2, 3, 5, 6}

# We can also use pop method, it removes the last item from the set
my_set7 = {1, 2, 3, 4}
my_set7.pop()
my_set7.pop()
my_set7.pop()
print(my_set7)                      # {4}

# We can delete the entire set once using clear method
my_st = {1, 2, 3}
my_st.clear()
print(my_st)                        # set()

# Python Set Operations
# 1. Union of two sets
# Using union '|' Operator
days1 = {'Mon', 'Tue', 'Wed', 'Thu'}
days2 = {'Fri', 'Sat', 'Sun'}
print(days1 | days2)        # {'Sun', 'Thu', 'Wed', 'Fri', 'Tue', 'Mon', 'Sat'}
# Using union method
print(days1.union(days2))   # {'Sun', 'Thu', 'Wed', 'Fri', 'Tue', 'Mon', 'Sat'}

# 2. The intersection of two numbers
# Using '&' Operator
days3 = {'Mon', 'Tue', 'Wed', 'Fri', 'Sat', 'Sun'}
days4 = {'Tue', 'Thu', 'Sun'}
print(days3 & days4)                # {'Tue', 'Sun'}
# Using intersection method
print(days3.intersection(days4))    # {'Tue', 'Sun'}

# 3. Difference between two sets
# Using '-' Operator
days5 = {'Mon', 'Tue', 'Wed', 'Thu'}
days6 = {'Mon', 'Tue', 'Sun'}
print(days5 - days6)                # {'Thu', 'Wed'}
# Using difference method
print(days5.difference(days6))      # {'Thu', 'Wed'}

# 4. Symmetric Difference between two sets
# Using '^' Operator
days7 = {1, 2, 3, 4, 5, 6}
days8 = {1, 2, 9, 8, 10}
print(days7 ^ days8)                        # {3, 4, 5, 6, 8, 9, 10}
# Using symmetric_difference method
print(days7.symmetric_difference(days8))    # {3, 4, 5, 6, 8, 9, 10}

# FrozenSet - It is a new class that has the characteristics of a set,
# But it's elements cannot be changed once assigned.
# While Tuples are immutable Lists, frozensets are immutable sets.
# They can be created using the function frozenset()

frozen_set = frozenset([1, 2, 3, 4, 5])
print(type(frozen_set))                 # <class 'frozenset'>
print(frozen_set)                       # frozenset({1, 2, 3, 4, 5})

# As it is immutable, we cannot use add or remove methods
# This datatype supports methods like copy(), difference(), intersection(),
# union(), symmetric_difference(), isdisjoint(), issubset(), issuperset()
