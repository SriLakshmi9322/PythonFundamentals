# Python Anonymous/Lambda Function :
""" In Python, an anonymous function is a function that is defined without a
name.
While normal functions are defined using the def keyword in Python, anonymous
functions are defined using the lambda keyword.
Hence, anonymous functions are also called lambda functions.
Lambda functions can have any number of arguements but only one expression. The
expression is evaluated and returned. Lambda functions can be used wherever
function objects are required.
Syntax : lambda arguements: expression """

# Example : Program to show the use of lambda functions.

double = lambda x: x * 2
print(double(5))            # 10

# Use with filter() - The filter() function in Python takes in a function and
# a list as arguements.
# Example : Program to filter out only the even items from a list.

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)             # [4, 6, 8, 12]


# Use with map() - The map() function in Python takes in a function and a list.
# Example : Program to double each item in a list using map()
my_lst = [1, 5, 4, 6, 8, 11, 3, 12]
new_lst = list(map(lambda x: x * 2, my_lst))
print(new_lst)              # [2, 10, 8, 12, 16, 22, 6, 24]
