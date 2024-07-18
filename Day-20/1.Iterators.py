# Iterators in Python
"""
An iterator in Python is an object that is used to iterate over iterable
objects like lists, tuples, dicts & sets.
    The Python iterators object is initialized using the iter() method. It uses
the next() method for iteration.
1. __iter__() : The iter() method is called for the initialization of an
                iterator.
2. __next__() : The next() method returns the next value for the  iterable.
                When we use a for loop to traverse any iterable object,
                internally it uses the iter() method to get an iterator object,
                which further uses the next() method to iterate over. This
                method raises a 'StopIteration' to signal the end of the
                iteration.
"""

# Example :
string = "SriLakshmi"
ch_iterator = iter(string)

print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))

# Output :
# S
# r
# i
# L


# Creating and Looping over an iterator using iter() and next()
class Test:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x

        if x > self.limit:
            raise StopIteration

        self.x = x + 1
        return x


for i in Test(15):
    print(i)

for i in Test(5):
    print(i)

# Output :
# 10
# 11
# 12
# 13
# 14
# 15


# Iterating over built-in iterable using iter() method :
# To traverse over the built-in iterable like list, tuple, dict etc.,

# 1. Iterating over a list :
print("List Iteration :")
lst = ["SriLakshmi", 99, 12000]

for i in lst:
    print(i)

# Output :
# List Iteration :
# SriLakshmi
# 99
# 12000

# 2. Iterating over a tuple (immutable) :
print("Tuple Iteration :")
tup = ("SriLakshmi", 99, 12000)

for i in tup:
    print(i)

# Output :
# Tuple Iteration :
# SriLakshmi
# 99
# 12000

# 3. Iterating over a String :
print("String Iteration :")
st = "SriLakshmi"

for i in st:
    print(i)

# Output :
# String Iteration :
# S
# r
# i
# L
# a
# k
# s
# h
# m
# i

# 4. Itertor over Dictionary :
print("Dictionary Iteration :")
d = dict()

d['xyz'] = 123
d['abc'] = 345

for i in d:
    print("%s  %d " % (i, d[i]))

# Output :
# Dictionary Iteration :
# xyz  123
# abc  345


# Iterables Vs Iterators :
"""
Iterables and Iterators are different. Main difference between them is,
iterable cannot save the state of the iteration, whereas in iterators the state
of the current iteration gets saved.

Note : Every iterator is also an iterable, but not every iterable is an
       iterator.
"""

# 1. Iterating on an Iterable : Iterating on each item of the iterable.
tup = ('a', 'b', 'c', 'd', 'e')

for item in tup:
    print(item)

# Output :
# a
# b
# c
# d
# e

# 2. Iterating on an Iterator :
tup = ('a', 'b', 'c', 'd', 'e')

tup_iter = iter(tup)
print("Inside Loop :")

for index, item in enumerate(tup_iter):
    print(item)

    if index == 2:
        break

print("Outside Loop :")
print(next(tup_iter))
print(next(tup_iter))

# Output :
# Inside Loop :
# a
# b
# c
# Outside Loop :
# d
# e


# Getting StopIteration Error while using iterator
"""
Iterable in Python can be iterated over multiple times, but iterators raise
'StopIteration' Error when all items are already iterated. Here, we are trying
to get the next element from the iterator after the completion of the for loop.
Since the iterator is already exhausted, it raises a 'StopIteration' Exception.
Whereas, using an iterable, we can iterate on multiple times using for loop or
can get items using indexing.
"""
# Example :
iterable = (1, 2, 3, 4)
iterator_obj = iter(iterable)

# Iterating on iterable
print("Iterable Loop1 :")
for item in iterable:
    print(item, end=',')

print("\nIterable Loop2 :")
for item in iterable:
    print(item, end=',')

print("\nIterating on an Iterator :")
for item in iterator_obj:
    print(item, end=',')

print("\nIterator: Outside Loop")
print(next(iterator_obj))

# Output :
# Iterable Loop1 :
# 1,2,3,4,
# Iterable Loop2 :
# 1,2,3,4,
# Iterating on an Iterator :
# 1,2,3,4,
# Iterator: Outside Loop
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-20\tempCodeRunnerFile.py",
# line 19, in <module>
#     print(next(iterator_obj))
# StopIteration
