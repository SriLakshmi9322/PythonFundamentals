# Conditional statements: Used to execute code based on certain conditions
# (if, else, elif).

# 1. Simple if statement - When we have a single condition to check
# if the given condtion is True, The instruction inside the if-block will
# be executed otherwise the block will not be executed

# Example-1 :
i = 10

if (i > 15):    # 10 is not less than 15 so inside code will not be executed
    print('10 is less than 15')


print('I am not inside if-block')

# Output :
# I am not inside if-block

# Example-2 :
i = 10

if (i < 15):    # 10 is less than 15 so inside code will be executed
    print('10 is less than 15')


print('I am not inside if-block')

# Output :
# 10 is less than 15
# I am not inside if-block

# Nested if Statement - When we want to check another condition inside one
# condition we can use nested-if statement

# Example :
i = 6

if (i > 0):       # First Condition
    if ((i % 2) == 0):
        print('i is a positive & even number')


print('Nested-if ends')

# Output :
# i is a positive & even number
# Nested-if ends

# 2. if-else statement - When we need to do some task for both conditions
# for True a block of code and if not True another block of code then
# we can use if-else statements

# Example :
i = 10

if (i > 15):
    print('10 is less than 15')
    print('I am in if-block')
else:
    print('10 is not less than 15')
    print('I am in else-block')


print('I am out of both if & else blocks')

# Output :
# 10 is not less than 15
# I am in else-block
# I am out of both if & else blocks


# 3. elif statements - When we have more than one condition to check
# one by one and when the a condition found to be True that particular
# block of code should be executed, than we can use elif-statements.
# After block executes it will be back to after elif statement code
# elif is short of 'else if'

# Example-1 :
i = 35

if (i == 15):
    print('i is 15')
elif (i == 25):
    print('i is 25')
elif (i == 35):
    print('i is 35')
else:
    print('i is not present')


# Output :      i is 35

# Example-2 :
number = 23
guess = int(input("Enter an integer : "))
if guess == number:
    print('Congratulations, You guessed it...')
elif guess < number:
    print('No, It is a little higher number...')
else:
    print('No, It is a little lower number...')


print('End of guessing...')

# Output :
# Enter an integer : 25
# No, It is a little lower number...
# End of guessing...

# Example-3 :
x = int(input('Please enter an integer : '))

if (x < 0):
    print('It is a Negative number')
elif (x > 0):
    print('It is a Positive Number')
else:
    print('Zero')


# Output :
#  Please enter an integer : 99
# It is a Positive Number
