# Control Statements - control statements change execution
# from their normal sequence.
# In Python, we have 3 control statements (break, continue, pass)

# 1. break - It brings control out of the loop
# Using for loop
for i in range(1, 10):
    if (i == 4):
        break
    print(i)

# Output :
# 1
# 2
# 3

# Using while loop
while 1:
    n = input("Please enter 'hello' : ")
    if n.strip() == 'hello':
        print("You entered correctly.!!")
        # break
    else:
        print('You entered wrong input...')

# Output :
# You entered correctly.!!
# Please enter 'hello' : hello

# 2. continue - It skips a specific condition
# and resumes the remaining iterations
# Using for loop
for i in range(1, 6):
    if (i == 4):
        continue
    print(i)

# Output :
# 1
# 2
# 3
# 5

# Using while loop
while True:
    n = input("Enter Some name (To stop enter 'exit'): ")
    if (n == 'exit'):
        break
    elif (len(n) < 3):
        print('Name is very small...')
    print('You entered a Good name...')

# Output :
# Enter Some name (To stop enter 'exit'): SriLakshmi
# You entered a Good name...
# Enter Some name (To stop enter 'exit'): exit


# 3. pass - We use pass statements to write empty loops.
# Pass is also used for empty control statements, functions, and classes.
# Example :
for i in 'Python':
    if i == 't':
        pass
    print(i)

# Output :
# P
# y
# t
# h
# o
# n
