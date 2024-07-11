# SyntaxError
"""
SyntaxError: This exception is raised when the interpreter encounters a
             syntax error in the code, such as a misspelled keyword, a
             missing colon, or an unbalanced parenthesis.
"""

# Example-1 : Misspelled Keyword.
amount = int(input("Enter the amount you have in your Account : "))

in amount > 2999:
    print("You can purchase this Product.!")

# Output :
# File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 4
#     in amount > 2999:
#     ^
# SyntaxError: invalid syntax

# Example-2 : Missing Colon.
amount = int(input("Enter the amount you have in your Account : "))

if amount > 2999
    print("You can purchase this Product.!")

# Output :
# File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 4
#     if amount > 2999
#                    ^
# SyntaxError: invalid syntax

# Example-3 : An Unbalanced Parenthesis.
amount = int(input("Enter the amount you have in your Account : "))

if(amount > 2999:
    print("You can purchase this Product.!")

# Output :
# File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 4
#     if(amount > 2999:
#                      ^
# SyntaxError: invalid syntax


#  We can fix this by writing the correct syntax.
