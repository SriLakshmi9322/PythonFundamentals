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

# Example-3 :
is_hot = True

if is_hot:
    print("It's a Hot Day!")

print("Enjoy Your Day.!!")

# Output :
# It's a Hot Day!
# Enjoy Your Day.!!

# Example-4 :
is_hot1 = False

if is_hot1:
    print("It's a Hot Day!")

print("Enjoy Your Day.!!")

# Output :
# Enjoy Your Day.!!

# Example-5 :
is_hot2 = True

if is_hot2:
    print("It's a Hot Day!")
    print("Drink Plenty of Water!!")

print("Enjoy Your Day.!!")

# Output :
# It's a Hot Day!
# Drink Plenty of Water!!
# Enjoy Your Day.!!

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

# Example-1 :
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

# Example-2 :
is_hot3 = False

if is_hot3:
    print("It's a Hot Day!")
    print("Drink Plenty of Water!!")
else:
    print("It's a Cold Day!")
    print("Wear Warm Clothes!!")

print("Enjoy Your Day.!!")

# Output :
# It's a Cold Day!
# Wear Warm Clothes!!
# Enjoy Your Day.!!


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

# Example-4 :
is_hot5 = False
is_cold = False

if is_hot5:
    print("It's a Hot Day!")
    print("Drink Plenty of Water!!")
elif is_cold:
    print("It's a Cold Day!")
    print("Wear Warm Clothes!!")
else:
    print("It's a lovely Day.!!")

print("Enjoy Your Day.!!") 

# Output :
# It's a lovely Day.!!
# Enjoy Your Day.!!
