# Looping Statements - Looping Statements are used for iterate a block of
# code as many times as we want.
# Used to print the data n number of times based on a condition
# Looping statements: Used to execute code repeatedly
# until a condition is met (for, while).

# 1. for loop
# To iterate over a sequence of number, we have a built-in function
# called range().
# range method - This method can have 3 parameters
# 1. Start value            (Optional)
# 2. Stop value
# 3. Increment/Skip value   (Optional)

for i in range(10):     # Default start value is 0 and end value is exclusive
    print(i)

# Output :
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(5, 10):  # 5- start value & 10 is end value
    print(i)

# Output :
# 5
# 6
# 7
# 8
# 9

for i in range(3, 10, 3):   # Here 3-start, 10-stop & 3-incerement/skip
    print(i)

# Output :
# 3
# 6
# 9

for x in range(-20, -10):
    print(x)

# Output :
# -20
# -19
# -18
# -17
# -16
# -15
# -14
# -13
# -12
# -11

for x in range(-20, -10, 3):
    print(x)

# Output :
# -20
# -17
# -14
# -11


# Loops with else block
# Note : else is always executed if the loop executed with normal termination
for i in range(1, 5):
    print(i)
else:
    print('The for loop is Over')

# Output :
# 1
# 2
# 3
# 4
# The for loop is Over

# else block will not be executed in two cases
# case-1 :
for i in range(10):
    print(i)
    print(10 / 0)
else:
    print('Else block')

# Output :
# ZeroDivisionError: division by zero

# case-2 :
for i in range(10):
    print(i)
    if (i == 4):
        break
else:
    print('else block')

# Output :
# 0
# 1
# 2
# 3
# 4


# Example-1 :
words = ['cat', 'apple', 'rat', 'four']
for w in words[1:3]:
    print(w, len(w))

# Output :
# apple 5
# rat 3

# Example-2 :
words = ['cat', 'apple', 'rat', 'four']
for w in words:
    print(w, len(w))

# Output :
# cat 3
# apple 5
# rat 3
# four 4

# Example-3 :
numbers = [5, 2, 5, 2, 2]
for item in numbers:
    for i in range(item):
        print("X", end="")
    print()

# Output :
# XXXXX
# XX
# XXXXX
# XX
# XX

# Example-4 :
num_list = [5, 2, 5, 2, 2]
for x_count in num_list:
    output = ""
    for count in range(x_count):
        output += 'X'
    print(output)

# Output :
# XXXXX
# XX
# XXXXX
# XX
# XX

# Example-5 :
numbers = [2, 2, 2, 6]
for item in numbers:
    for i in range(item):
        print("X", end="")
    print()

# Output :
# XX
# XX
# XX
# XXXXXX

# 2. while loop
# When we know the number of iterations we can use for loop
# But, when we need to iterate until a condition fails we can use 'while' loop

# Example-1 :
a = 0
while (a < 10):
    print(a)
    a = a + 1

# Output :
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Example-2:
value = 1

while value <= 5:
    print("*" * value)
    value += 1

print("Done!")

# Output :
# *
# **
# ***
# ****
# *****
# Done!

# While loop with else block
# else is always executed after the while loop is over unless
# a break statement is encountered.
a = 0
while (a < 5):
    print(a)
    a += 1
else:
    print("else block after while loop")

# Output :
# 0
# 1
# 2
# 3
# 4
# else block after while loop

# Example for 'else not executed'
a = 0
while (a < 5):
    print(a)
    a += 1
    if (a == 2):
        break
else:
    print("else block after while loop")
print('Process Done...')

# Output :
# 0
# 1
# Process Done...
