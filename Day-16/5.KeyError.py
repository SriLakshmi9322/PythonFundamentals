# KeyError
"""
KeyError: This exception is raised when a key is not found in a dictionary.
"""

# Example :
studentDetails = {
    'Name': "SriLakshmi",
    'Age': 21,
    'Course': "Python"
}

getStudentInfo = input("What info about the student do you want : ")
print(studentDetails[getStudentInfo])

# Output :
# What info about the student do you want : cgpa
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-15\tempCodeRunnerFile.py",
# line 9, in <module>
#     print(studentDetails[getStudentInfo])
# KeyError: 'cgpa'

# Solution-1 : Using 'if-else' block & 'in' Keyword.
studentDetails = {
    'Name': "SriLakshmi",
    'Age': 21,
    'Course': "Python"
}

getStudentInfo = input("Enter the Key for the Value which you want : ")

if getStudentInfo in studentDetails:
    print(studentDetails[getStudentInfo])
else:
    print("The keyword does not Exists...")

# Output :
# Enter the Key for the Value which you want : cgpa
# The keyword does not Exists...

# Solution-2 : Using 'try-except' Block.
try:
    studentDetails = {
        'Name': "SriLakshmi",
        'Age': 21,
        'Course': "Python"
    }

    getStudentInfo = input("Enter the Key for the Value which you want : ")
    print(studentDetails[getStudentInfo])
except KeyError:
    print("Error: Key does not Exists...")

# Output :
# Enter the Key for the Value which you want : cgpa
# Error: Key does not Exists...
