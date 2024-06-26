# Function with Keyword Arguements
"""
The Keywords are mentioned during the function call along with their
corresponding values.
These keywords are mapped with the function arguements, so the function
can easily identify the corresponding values even if the order is not
maintained during the function call.
Using the Keyword Arguement, the arguement passed in function call is
matched with function definition on the basis of the name of the parameter.
"""

# Example :


def student_details(id, name):
    print('Student ID :', id)
    print('Student Name :', name)


student_details(id=1, name='SriLakshmi')
student_details(name='Bhavani', id=2)

# Output :
# Student ID : 1
# Student Name : SriLakshmi
# Student ID : 2
# Student Name : Bhavani
