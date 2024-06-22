# Performing Math Calculations :-
# We can use numbers & special symbols (to tell what kind of calculation)
# to calculate mathematical calculations in Python.

# Example :
print(2 + 2)        # 4 - Addition
print(2 - 2)        # 0 - Subraction
print(2 * 2)        # 4 - Multiplication
print(2 / 2)        # 1.0 - Division (returns floating value)
print(12 % 10)      # 2 - Modulo (for Remainder)
print(5 // 2)       # 2 - floor Division
# (// -for getting without decimal part - result will be rounded to integer)
print(3 ** 2)       # 9 - Exponentiation (3 to the power of 2)

print("2" + "2")        # 22 - We can't use string values for calculation
# If we want to calculate on numbers in the form of strings we can simply
# convert the values to integer or float than perform operations.

# Example :
num = "2"
num = int(num)          # Here, int() - converts str type into int type
print(num + num)        # 4

num = "2"
num = float(num)        # Here, float() - converts str type into int type
print(num + num)        # 4.0


"""
Calculations in Python follow the order of Operations (for Expressions),
which is sometimes called "PEMDAS"
P - Parentheses
E - Exponentiation
M - Multiplication
D - Division
A - Addition
S - Subtraction
"""
# Examples :
print((6 - 2) * 5)      # 20
print(6 - 2 * 5)        # -4
# In 1st expression, there is parentheses which has highest priority
# (6 - 2) * 5 - Parentheses first
# 4 * 5
# 20
# In 2nd expression, the priority will be for multiplication operator first
# 6 - 2 * 5 - Multiplication first
# 6 - 10
# -4

"""
Activity-1 : Make a Simple Chatbot that asks a series of questions,
explaining to you why it is superior after each one.
The robot will have a variable level of
one-upmanship (feeling of superiority over another).
"""
one_up_level = 1
a1 = input("How many seconds does it take you to run the 100 meter dash? ")
a1 = int(a1)
print("That's Cool... I can do it in", a1 - one_up_level, "seconds though.")
print("And I don't even have legs, sooooo......")

print("But What about your GPA? I'm sure that's pretty good,eh? ")
a2 = input("Enter your GPA: ")
a2 = float(a2)
print("Alright mine was", a2 + one_up_level)
print("Not that it matters, LOL")
# Output :-
# How many seconds does it take you to run the 100 meter dash? 5
# That's Cool... I can do it in 4 seconds though.
# And I don't even have legs, sooooo......
# But What about your GPA? I'm sure that's pretty good,eh?
# Enter your GPA: 73.94
# Alright mine was 74.94
# Not that it matters, LOL

"""
Activity-2 : Make a simple program that tells you if first given number is a
multiple of second given number.
"""
print("Is_a_multiple_of_?")
num1 = input("Enter First Number : ")
num2 = input("Enter Second Number : ")
print(int(num1) % int(num2))
print("If the number above is zero (0), then", num1, "is multiple of", num2)
# Output :-
# Is_a_multiple_of_?
# Enter First Number : 25
# Enter Second Number : 5
# 0
# If the number above is zero (0), then 25 is multiple of 5
