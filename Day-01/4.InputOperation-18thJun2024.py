# Reading Input from the Keyboard - In Python input() is used to read the
# input from the keyboard dynamically.
# By default, the value of the input() will be stored as a String.
# Syntax : variable_name = input('prompt')

# Example :
name = input("Enter Employee name : ")
salary = input("Enter Salary : ")
company = input("Enter Company name : ")
print()
print("Displaying Employee Details :")
print("Name      ", "Salary", "Company   ")
print(name, salary, company)
# Output :-
# Enter Employee name : SriLakshmi
# Enter Salary : 100000
# Enter Company name : Google
#
# Displaying Employee Details :
# Name       Salary Company
# SriLakshmi 100000 Google

# To Accept numeric input from User
# Example :
first_number = int(input("Enter First Number : "))
second_number = int(input("Enter Second Number : "))
print("First Number : ", first_number)
print("Second Number : ", second_number)
sum = first_number + second_number
print("Addition of two numbers : ", sum)
# Output :-
# Enter First Number : 20
# Enter Second Number : 40
# First Number :  20
# Second Number :  40
# Addition of two numbers :  60

# To get multilple input values from the user in one line we can use split()
# Example :
n, a, p = input("Enter your Name, Age, Percentage separated by space:").split()
print()
print("User Details :", n, a, p)
# Output :-
# Enter your Name, Age, Percentage separated by space:SriLakshmi 21 73.94
#
# User Details : SriLakshmi 21 73.94
