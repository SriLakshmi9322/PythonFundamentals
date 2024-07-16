""" Customize Sort Function : We can also customize  you own function by using
the keyword arguement key = function.
The function will return a number that will be used to sort the list (the
lowest number first).
"""


# Example-1 : Sort the list based on how close the number is to 50.
def myFunc(num):
    return abs(num - 50)


lst = [100, 50, 65, 82, 23]
lst.sort(key=myFunc)
print(lst)                  # [50, 65, 23, 82, 100]


""" Note : By default the sort() method is case sensitive, resulting in all
capital letters being sorted after lower case letter. """
# Example-1 :
lst1 = ['banana', 'Orange', 'Kiwi', 'cherry']
lst1.sort()
print(lst1)                 # ['Kiwi', 'Orange', 'banana', 'cherry']


""" Case Insensitive Sort : We can use built-in functions as key functions
when sorting a list. So if you want a case-insensitive sort function, use
str.lower as a key function. """
# Example-1 :
lst2 = ['banana', 'Orange', 'Kiwi', 'cherry']
lst2.sort(key=str.lower)
print(lst2)                 # ['banana', 'cherry', 'Kiwi', 'Orange']
