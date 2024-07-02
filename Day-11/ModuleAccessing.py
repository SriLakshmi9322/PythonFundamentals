import example

""" This does not import the names of the functions defined in example directly
in the current symbol table. It only imports the module name example there.
Using the module name we can access the function using the dot (.) operator.
"""
sum = example.add(1, 2)
print(sum)                  # 3

sum1 = example.add(4, 5.5)
print(sum1)                 # 9.5
