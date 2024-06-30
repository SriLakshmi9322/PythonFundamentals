# Python Dictionary Methods - Python has a set of built-in methods that you
# can use on dictionaries.


# 1. clear() - Removes all the elements from the dictionary
""" The clear() method removes all the elements from a dictionary.
Syntax : dictionary.clear() """
# Example : Remove all elements from the car list.
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
car.clear()
print(car)              # {}


# 2. copy() - Returns a copy of the dictionary
""" You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2
will only be a reference to dict1, and changes made in dict1 will automatically
also be made in dict2.
The copy() method returns a copy of the specified dictionary.
Syntax : dictionary.copy() """
# Example-1 : Copy the car dictionary.
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = car.copy()
print(x)                # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

""" Another way to make a copy is to use the built-in function dict(). """
# Example-2 : Make a copy of a dictionary with the dict() function.
thisDict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
myDict = dict(thisDict)
print(myDict)           # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# 3. fromkeys() - Returns a dictionary with the specified keys and value
""" The fromkeys() method returns a dictionary with the specified keys and the
specified value.
Syntax : dictionary.fromkeys(keys, value)
1. keys - Required. An iterable specifying the keys of the new dictionary.
2. value - Optional. The value for all keys. Default value is None. """
# Example-1 : Create a dictionary with 3 keys, all with the value 0.
a = ('key1', 'key2', 'key3')
b = 0
thisdict = dict.fromkeys(a, b)
print(thisdict)         # {'key1': 0, 'key2': 0, 'key3': 0}

# Example-2 : Same example as above, but without specifying the value.
c = ('key1', 'key2', 'key3')
thisdict1 = dict.fromkeys(c)
print(thisdict1)        # {'key1': None, 'key2': None, 'key3': None}


# 4. get() - Returns the value of the specified key
""" The get() method returns the value of the item with the specified key.
Syntax : dictionary.get(keyname, value)
1. keyname - Required. The keyname of the item you want to return the
 value from.
2. value - Optional. A value to return if the specified key does not exist.
 Default value None. """
# Example-1 : Get the value of the 'model' item.
carDict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
d = carDict.get('model')
print(d)                # Mustang

# Example-2 : Try to return the value of an item that do not exist.
carDict1 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
insertPrice = carDict1.get('price', 15000)
print(insertPrice)      # 15000


# 5. items() - Returns a list containing a tuple for each key-value pair
""" The items() method returns a view  object. The view object contains the
key-value pairs of the dictionary, as tuples in a list.
The view object will reflect any changes done to the dictionary.
Syntax : dictionary.items() """
# Example-1 : Return the dictionaries key-value pairs.
carDict2 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
car_items = carDict2.items()
print(car_items)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# Example-2 : When an item in the dictionary changes value, the view object
# also gets updated.
carDict3 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
new_items = carDict3.items()
carDict3['year'] = 2018
print(new_items)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])


# 6. keys() - Returns a list containing the dictionaries keys
""" The keys() method returns a view object. The view object contains the keys
of the dictionary, as a list.
The view object will reflect any changes done to the dictionary.
Syntax : dictionary.keys() """
# Example-1 : Return the keys.
carDict4 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
car_keys = carDict4.keys()
print(car_keys)         # dict_keys(['brand', 'model', 'year'])

# Example-2 : When an item is added in the dictionary, the view object also
# gets updated
carDict5 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
car_keys1 = carDict5.keys()
carDict5['color'] = 'white'
print(car_keys1)        # dict_keys(['brand', 'model', 'year', 'color'])


# 7. pop() - Removes the element with the specified key
""" The pop() method removes the specified item from the dictionary.
The value of the removed item is the return value of the pop() method.
Syntax : dictionary.pop(keyname, defaultValue)
1. keyname - Required. The keyname of the item you want to remove.
2. defaultValue - Optional. A value to return if the specified key do not
 exist. If this parameter is not specified, and the no item with the specified
 key is not found, an error is raised. """
# Example-1 : Remove 'model' from the dictionary.
carDict6 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
carDict6.pop('model')
print(carDict6)             # {'brand': 'Ford', 'year': 1964}

# Example-2 : The value of the removed item is the return value of the
# pop() method.
carDict7 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
y = carDict7.pop('model')
print(y)                    # Mustang


# 8. popitem() - Removes the last inserted key-value pair
""" The popitem() method removes the item that was last inserted into the
dictionary. In versions before 3.7, the popitem() method removes a random
item.
The removed item is the return value of the popitem() method, as a tuple.
Syntax : dictionary.popitem() """
# Example-1 : Remove the last item from the dictionary.
carDict8 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
carDict8.popitem()
print(carDict8)             # {'brand': 'Ford', 'model': 'Mustang'}

# Example-2 : The removed item is the return value of the pop() method.
carDict9 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
pop_item = carDict9.popitem()
print(pop_item)             # ('year', 1964)


# 9. setdefault() - Returns the value of the specified key. If the key does
# not exist: insert the key, with the specified value.
""" The setdefault() method returns the value of the item with the specified
key.
If the key does not exist, insert the key, with the specified value.
Syntax : dictionary.setdefault(keyname, value)
1. keyname - Required. The keyname of the item you want to return the value
 from.
2. value - Optional. If the key exists, this parameter has no effect. If the
 key does not exist, this value becomes the key's value. Default value None."""
#  Example-1 : Get the value of the 'model' item.
carDict10 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
z = carDict10.setdefault('model', 'Bronco')
print(z)                    # Mustang

# Example-2 : Get the value of the 'color' item, if the 'color' item does not
# exist, insert 'color' with the value 'white'.
carDict11 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
default_value = carDict11.setdefault('color', 'white')
print(default_value)        # white


# 10. update() - Updates the dictionary with the specified key-value pair
""" The update() method inserts the specified items to the dictionary.
The specified items can be a dictionary, or an iterable object with key-value
pairs.
Syntax : dictionary.update(iterable)
iterable - A dictionary or an iterable object with key-value pairs, that will
 be inserted to the dictionary. """
# Example : Insert an item to the dictionary.
carDict12 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
carDict12.update({'color': 'White'})
print(carDict12)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}


# 11. values() - Returns a list of all the values in the dictionary
""" The values() method returns a view object. The view object contains the
values of the dictionary as a list.
The view object will reflect any changes done to the dictionary.
Syntax : dictionary.values() """
# Example-1 : Return the values.
carDict13 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
car_values = carDict13.values()
print(car_values)           # dict_values(['Ford', 'Mustang', 1964])

# Example-2 : When a value is changed in the dictionary, the view object also
# gets updated.
carDict14 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
car_values1 = carDict14.values()
carDict14['year'] = 2018
print(car_values1)          # dict_values(['Ford', 'Mustang', 2018])


# 12. del
""" The del keyword removes the item with the specified key name. """
# Example-1 :
carDict15 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
del carDict15['model']
print(carDict15)            # {'brand': 'Ford', 'year': 1964}

# Example-2 : The del keyword can also delete the dictionary completely.
carDict16 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
del carDict16
print(carDict16)
# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-9\tempCodeRunnerFile.py", line 7, in <module>
#     print(carDict16)
# NameError: name 'carDict16' is not defined
