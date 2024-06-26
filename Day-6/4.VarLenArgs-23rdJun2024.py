# Function with Variable length Arguements
"""
This is very useful when we do not know the exact number of arguements
that will be passed to a function.
Or we can have a design where any number of arguements can be passed
based on the requirement.
"""

# Example :


def display_arguements(*var):
    for i in var:
        print('Variable Arguement :', i)


display_arguements()
display_arguements(10, 20, 30)
display_arguements(10, 20.3, 'Bhavani')

# Output :
# Variable Arguement : 10
# Variable Arguement : 20
# Variable Arguement : 30
# Variable Arguement : 10
# Variable Arguement : 20.3
# Variable Arguement : Bhavani
