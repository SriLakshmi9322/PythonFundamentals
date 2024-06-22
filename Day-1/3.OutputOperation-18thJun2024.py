"""
print() - It prints the given object to the standard output device
(screen) or to the text stream file.
"""
# Example - 1
print('This sentence is output to the screen')
# Output :- This sentence is output to the screen

# Example - 2
a = 5
print('The value of a is', a)
# Output :- The value of a is 5

# Example - 3
print('Python is fun.')
a = 5
# Two objects are passed
print('a =', a)
b = a
# Three objects are passed
print('a =', a, '= b')
# Output :-
# Python is fun.
# a = 5
# a = 5 = b

# Case 1: print without any arguements
print('Srilakshmi Tiramsetti')
print()         # By default it takes new line as an arguement
print('Computer Science & Engineering')
# Output :-
# Srilakshmi Tiramsetti

# Computer Science & Engineering

# Case 2: print() with String operations (without arguements)
print('HelloWorld')         # HelloWorld
print('Hello\nWorld')
# Output :-
# Hello
# World
print('Hello\tWorld')       # Hello   World
# String Concatenation both objects are strings only
print('tech' + 'cse')       # techcse
print('tech', 'cse')        # tech cse
# Repeat String into number of times
print(5 * 'SriLakshmi')
# Output :- SriLakshmiSriLakshmiSriLakshmiSriLakshmiSriLakshmi
print(5 * 'SriLakshmi\n')
# Output :-
# SriLakshmi
# SriLakshmi
# SriLakshmi
# SriLakshmi
# SriLakshmi
print(5 * 'SriLakshmi\t')
# Output :-
# SriLakshmi      SriLakshmi      SriLakshmi      SriLakshmi      SriLakshmi

# Case 3: print() with any number of arguements
print('Values are :', 10, 20, 30)   # Values are : 10 20 30

a, b, c = 10, 20, 30
print('Values are :', a, b, c)  # Values are : 10 20 30

# print() with "sep" attribute: To separate objects
# Default value of sep is empty space (sep='')
print('Values are ', 10, 20, 30, sep=':')
# Output :- Values are :10:20:30
print('Values are :', 10, 20, 30, sep='--')
# Output :- Values are :--10--20--30

# Case 4: print statement with end attribute
# end = '' - The end key of print() will set the string that needs to be
# appended when printing is done.
# default value for end is new line (end='\n')
# Example - 1
print('SriLakshmi')     # By default end='\n' is applied
print('Tiramsetti')
# Output :-
# SriLakshmi
# Tiramsetti

# Example - 2
print('SriLakshmi', end='$')
print('Tiramsetti', end='*')
print('CSE')
# Output :- SriLakshmi$Tiramsetti*CSE

# Case 5: print() with sep and end attribute
print(10, 20, 30, sep=':', end='$$$')
print(40, 50, sep=':')
print(70, 80, sep=':', end='&&&')
print(90, 100)
# Output :-
# 10:20:30$$$40:50
# 70:80&&&90 100

# Output Formatting - Sometimes user often wants more control on formatting of
# output than simply printing space-separated values.
# There are several ways to format output.

# 1. Formatting output using String modulo operator
# Syntax : print('Formatted String'%(variable_list))

# Example - 1
# To print integer and float value
print("RollNo:%2d, Portal:%5.2f" % (1, 05.333))    # RollNo: 1, Portal: 5.33

# To print integer value
print("Total Students :%3d, Boys :%2d" % (240, 120))
# Output :- Total Students :240, Boys :120

# To print octal value
print("%7.3o" % (25))       # 031

# To print Exponential value
print("%10.3E" % (356.08977))       # 3.561E+02


# Example - 2
a = 6
print('a value is = %i' % a)      # a value is = 6

a, b, c = 6, 7, 8
print('a value is = %i, b = %f, c = %i' % (a, b, c))
# Output :- a value is = 6, b = 7.000000, c = 8

# 2. print() with replacement operator - {} or format function
# str.format() - To concatenate elements within a string through
# positional formatting.

# Example - 1
name = 'SriLakshmi'
salary = '100000'
print('Hello my name is {} and my salary is {}'.format(name, salary))
# Output :- Hello my name is SriLakshmi and my salary is 100000

# Example - 2
name = 'SriLakshmi'
salary = '100000'
print('Hello my name is "{}" and my salary is "{}"'.format(name, salary))
# Output :- Hello my name is "SriLakshmi" and my salary is "100000"

# Example - 3
name = 'SriLakshmi'
salary = '100000'
# We can also use index values and print the output
print('Hello my name is "{0}" and my salary is "{1}"'.format(name, salary))
# Output :- Hello my name is "SriLakshmi" and my salary is "100000"

# Example - 4
name = 'SriLakshmi'
salary = '100000'
print('Hello my name is "{1}" and my salary is "{0}"'.format(salary, name))
# Output :- Hello my name is "SriLakshmi" and my salary is "100000"

# Example - 5
name = 'SriLakshmi'
salary = '100000'
print('Hello my name is "{n}" and my salary is "{s}"'.format(n=name, s=salary))
# Output :- Hello my name is "SriLakshmi" and my salary is "100000"

# Example - 6
name = 'SriLakshmi'
salary = '100000'
print('Hello my name is "{n}" and my salary is "{s}"'.format(s=salary, n=name))
# Output :- Hello my name is "SriLakshmi" and my salary is "100000"
