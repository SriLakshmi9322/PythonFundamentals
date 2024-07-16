# Nested Dictionaries :
""" A dictionary can contain dictionaries, this is called nested dictionaries.
"""
# Example-1 : Create a dictionary that contain three dictionaries.
myfamily = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'Tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    }
}
print(myfamily)
# Output :
# {'child1': {'name': 'Emil', 'year': 2004},
# 'child2': {'name': 'Tobias', 'year': 2007},
# 'child3': {'name': 'Linus', 'year': 2011}}

# Example-2 : Create three dictionaries, then create one dictionary that will
# contain the other three dictionaries.
child1 = {
    'name': 'Emil',
    'year': 2004
}
child2 = {
    'name': 'Tobias',
    'year': 2007
}
child3 = {
    'name': 'Linus',
    'year': 2011
}
mydict = {
    'child1': child1,
    'child2': child2,
    'child3': child3
}
print(mydict)
# Output:
# {'child1': {'name': 'Emil', 'year': 2004},
#  'child2': {'name': 'Tobias', 'year': 2007},
#  'child3': {'name': 'Linus', 'year': 2011}}
