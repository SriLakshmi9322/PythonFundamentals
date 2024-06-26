# Function with Default Arguements
# When we call the function, if we are not passing any arguements the default
# arguements we assigned at declaration time will be assigned by default.

# Example :
def employeeDetails(eid=1, ename='Anu', esal=10000):
    print('Emp ID :', eid)
    print('Emp Name :', ename)
    print('Emp Salary :', esal)


employeeDetails()
employeeDetails(222)
employeeDetails(333, 'Bhavani')
employeeDetails(111, 'SriDivya', 15000)
# Output :
# Emp ID : 1
# Emp Name : Anu
# Emp Salary : 10000
# Emp ID : 222
# Emp Name : Anu
# Emp Salary : 10000
# Emp ID : 333
# Emp Name : Bhavani
# Emp Salary : 10000
# Emp ID : 111
# Emp Name : SriDivya
# Emp Salary : 15000
