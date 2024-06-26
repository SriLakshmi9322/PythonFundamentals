# Dictionaries - The dictionary is a useful data structure for
# storing (key, value) pairs.
# To store the group of objects as key-value pairs instead of indexes
# Each value stored in a dictionary can be accessed using key
# Keys must be unique but Values can be Duplicated

# Creating a Dictionary
phone_dict = {}             # Empty Dictionary
# Adding elements to the dictionary using keys
phone_dict['ramu'] = 935577566
phone_dict['anu'] = 936677884
phone_dict['devi'] = 9476655551
print(phone_dict)
print(type(phone_dict))

# Output :
# {'ramu': 935577566, 'anu': 936677884, 'devi': 9476655551}
# <class 'dict'>

# To Read and write elements by specifying the key within the brackets.
# We can Use the keys() and values() functions to access all keys and
# values of the dictionary.
calories = {'apple': 52, 'banana': 89, 'choco': 546}
print(calories)                     # {'apple': 52, 'banana': 89, 'choco': 546}
print(calories.keys())              # dict_keys(['apple', 'banana', 'choco'])
print(calories.values())            # dict_values([52, 89, 546])

# Adding elements into the list using indexes
my_dict = {}
my_dict[0] = 'Anu'
my_dict[3] = 'John'
my_dict[5] = 'Ricky'
print(my_dict)          # {0: 'Anu', 3: 'John', 5: 'Ricky'}

# Deleting Elements using del Keyword
my_details = {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}
print(my_details)
# {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}
del my_details['Salary']
print(my_details)           # {'Name': 'SriLakshmi', 'Age': 21}

# Deleting Elements using pop method
my_details1 = {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}
my_details1.pop('Age')
print(my_details1)          # {'Name': 'SriLakshmi', 'Salary': 45000}

# To Calculate the length of the dictionary
my_details2 = {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}
print(len(my_details2))     # 3

# To delete the entire dictionary
details = {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}
details.clear()
print(details)              # {}

# To copy into another dictionary
details1 = {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}
details2 = details1.copy()
print(details2)     # {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}

# To remove the most recent key-value pair entered
details3 = {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}
details3['Company'] = 'Google'
print(details3)
# {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000, 'Company': 'Google'}
details3.popitem()
print(details3)     # {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}

# To return key-value pairs as a tuple
det = {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}
print(det.items())
# dict_items([('Name', 'SriLakshmi'), ('Age', 21), ('Salary', 45000)])

# To get a specific value by using it's key
det1 = {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}
print(det1.get('Name'))     # SriLakshmi

# To update an existing key's value
det2 = {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 45000}
det2.update({'Salary': 50000})
print(det2)
# {'Name': 'SriLakshmi', 'Age': 21, 'Salary': 50000}
