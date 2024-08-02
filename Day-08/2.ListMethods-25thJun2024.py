# Python List/Array Methods - Python has a set of built-in methods that you
# can use on lists/arrys.
# Note : Python does not have built-in support for Arrays, but Python Lists
# can be used instead.


# 1. append() - Adds an element at the end of the list
""" The append() method appends an element at the end of the list.
Syntax : list.append(element)
element - Required. An element of any type (string, number, object etc.,) """
# Example-1 : Add an element to the fruits list.
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)           # ['apple', 'banana', 'cherry', 'orange']

# Example-2 : Add a list to a list.
fruits_list = ['apple', 'banana', 'cherry']
brand_list = ['Ford', 'BMW', 'Volvo']
fruits_list.append(brand_list)
print(fruits_list)
# ['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo']]


# 2. clear() - Removes all the elements from the list
""" The clear() method removes all the elements from a list.
Syntax : list.clear() """
# Example : Removes all elements from the fruit list.
fruit_list = ['apple', 'banana', 'cherry', 'orange']
fruit_list.clear()
print(fruit_list)           # []


# 3. copy() - Returns a copy of the list
""" The copy() method returns a copy of the specified list.
Syntax : list.copy() """
# Example : Copy the Fruits list.
fruits1 = ['apple', 'banana', 'cherry', 'orange']
fruits_copy = fruits1.copy()
print(fruits_copy)      # ['apple', 'banana', 'cherry', 'orange']


# 4. count() - Returns the number of elements with the specified value
""" The count() method returns the number of elements with the specified value.
Syntax : list.count(value)
value - Required. Any type (string, number, list, tuple, etc.,). The value to
search for. """
# Example-1 : Return the number of times the value "cherry" appears in
# the fruits list.
fruits2 = ['apple', 'banana', 'cherry']
print(fruits2.count('cherry'))              # 1

# Example-2 : Return the number of times the value 9 appears in the list.
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
print(points.count(9))                      # 2


# 5. extend() - Adds the elements of a list (or any iterable), to the end of
# the current list.
""" The extend() method adds the specified list elements (or any iterable) to
the end of the current list.
Syntax : list.extend(iterable)
iterable - Required. Any iterable (list, set, tuple, etc.,) """
# Example-1 : Adds the elements of cars to the fruits list.
fruits3 = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits3.extend(cars)
print(fruits3)      # ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# Example-2 : Add a tuple to the fruits list.
fruits4 = ['apple', 'banana', 'cherry']
points1 = (1, 4, 5, 9)
fruits4.extend(points1)
print(fruits4)  # ['apple', 'banana', 'cherry', 1, 4, 5, 9]


# 6. index() - Returns the index of the first element with the specified value
""" The index() method returns the position at the first occurrence of the
specified value.
Note : The index() method only returns the first occurrence of the value.
Syntax : list.index(element)
element - Required. Any type (string, number, list, etc.,). The element to
search for. """
# Example-1 : What is the position of the value "cherry".
fruits5 = ['apple', 'banana', 'cherry']
print(fruits5.index('cherry'))              # 2

# Example-2 : What is the position of the value 32.
nums = [4, 55, 64, 32, 16, 32]
print(nums.index(32))                       # 3


# 7. insert() - Adds an element at the specified position
""" The insert() method is to insert a new list item, without replacing any of
the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index.
Syntax : list.insert(position, element)
1. position - Required. A number specifying in which position to insert
the value.
2. element - Required. An element of any type (string, number, object etc.,)
"""
# Example : Insert "watermelon" as the third item.
x = ['apple', 'banana', 'cherry']
x.insert(2, 'watermelon')
print(x)            # ['apple', 'banana', 'watermelon', 'cherry']


# 8. pop() - Removes the element at the specified position
""" The pop() method removes the element at the specified position.
Note : The pop() method returns removed value.
Syntax : list.pop(position)
position - Optional. A number specifying the position of the element you want
to remove, default value is -1, which returns the last item. """
# Example-1 : Removes the second element of the fruit list.
fruits6 = ['apple', 'banana', 'cherry']
fruits6.pop(1)
print(fruits6)              # ['apple', 'cherry']

# Example-2 : Return the removed element.
fruits7 = ['apple', 'banana', 'cherry']
fruit = fruits7.pop(1)
print(fruit)                # banana


# 9. remove() - Removes the first item with the specified value
""" The remove() method removes the first occurrence of the element with the
specified value.
Syntax : list.remove(element)
element - Required. Any type (string, number, list, etc.,).
The element you want to remove. """
# Example : Remove the "banana" element of the fruit list.
fruits8 = ['apple', 'banana', 'cherry']
fruits8.remove("banana")
print(fruits8)          # ['apple', 'cherry']


# 10. reverse() - Reverses the order of list.
""" The reverse() method reverses the sorting order of the elements.
Syntax : list.reverse() """
# Example-1 : Reverses the order of the fruit list.
fruits9 = ['apple', 'banana', 'cherry']
fruits9.reverse()
print(fruits9)              # ['cherry', 'banana', 'apple']

# Example-2 :
lst = ['banana', 'Orange', 'Kiwi', 'cherry']
lst.reverse()
print(lst)                  # ['cherry', 'Kiwi', 'Orange', 'banana']


# 11. sort() - Sorts the list
""" The sort() method sorts List Alphanumerically. List Objects have a sort()
method that will sort the list alphanumerically, ascending, by default.
To sort descending, use the keyword arguement reverse = True.
Syntax : list.sort() - for ascending.
list.sort(reverse = True) - for descending. """
# Example-1 :
lst1 = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
lst1.sort()
print(lst1)         # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Example-2 :
lst2 = [100, 50, 65, 82, 23]
lst2.sort()
print(lst2)         # [23, 50, 65, 82, 100]

# Example-3 : To sort the list descending.
lst3 = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
lst3.sort(reverse=True)
print(lst3)         # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
