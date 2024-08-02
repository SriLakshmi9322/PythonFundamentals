# Dictionaries - Dictionaries are used to store data values in key:value pairs.
""" A dictionary is a collection which is unordered, it means that the items
does not have a defined order, you cannot refer to an item by using an index.
It is changeable, means that we can change, add or remove items after the
dictionary has been created.
It does not allow duplicates means cannot have two items with the same key.
Dictionaries are written with curly brackets, and have keys and values.
It can be referred by using the key name.
The values in dictionary items can be of any data type. """
# Example-1 : Create and print a dictionary.
dict1 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(dict1)
# Output : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# Example-2 : Print the 'brand' value of the dictionary.
dict2 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(dict2['brand'])           # Ford


# Example-3 : Duplicate values will overwrite existing values.
# dict3 = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964,
#     'year': 2020
# }
# print(dict3)
# Output : {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


# Example-4 : String, int, boolean and list data types.
dict = {
    'brand': 'Ford',
    'electric': False,
    'year': 1964,
    'colors': ['red', 'white', 'blue']
}
print(dict)
# Output :
# {'brand': 'Ford', 'electric': False, 'year': 1964,
# 'colors': ['red', 'white', 'blue']}
