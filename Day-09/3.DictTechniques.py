# Checking if Key exists :
# To determine if a specified key is present in a dictionary use the
# 'in' keyword.
# Example : Check if 'model' is present in the dictionary.
carDict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

if 'model' in carDict:
    print("Yes, 'model' is one of the keys in the carDict dictionary.")

# Output : Yes, 'model' is one of the keys in the carDict dictionary.


# Dictionary Length :
# To determine how many items a dictionary has, use the len() function.
# Example : Print the number of items in the dictionary.
thisDict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964,
    'year': 2020
}
print(len(thisDict))                # 3


# Loop through a Dictionary :
""" You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return values are the keys of the
dictionary, but there are methods to return the values as well. """
# Example-1 : Print all key names in the dictionary, one by one.
carDict1 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

for x in carDict1:
    print(x)

# Output :
# brand
# model
# year

# Example-2 : Print all values in the dictionary, one by one.
carDict2 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

for x in carDict2:
    print(carDict2[x])

# Output :
# Ford
# Mustang
# 1964

# Example-3 : You can also use the values() method to return values of
# a dictionary.
carDict3 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

for x in carDict3.values():
    print(x)

# Output :
# Ford
# Mustang
# 1964

# Example-4 : You can use the keys() method to return the keys of
# a dictionary.
carDict4 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

for x in carDict4.keys():
    print(x)

# Output :
# brand
# model
# year

# Example-5 : Loop through both keys and values, by using the items() method.
carDict5 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

for x, y in carDict5.items():
    print(x, y)

# Output :
# brand Ford
# model Mustang
# year 1964
