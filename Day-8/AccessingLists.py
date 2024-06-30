# Accessing List Data - The list items are accessed by referring to the
# index number.
""" Negative indexing means beginning from the end, -1 refers to the
last element, -2 refers to the second last item etc.,
A range of indexes can be specified by specifying where to start and where
to end the range. When specifying a range, the return value will be a new
list with the specified items.
Note : The search will start at index 2 (included) and end at index 5 (not
included).
By leaving out the start value, the range will start at the first item.
By leaving out the end value, the range will go on to the end of the list. """
# Examples :
x = ['apple', 'banana', 'cherry']
print(x[1])                 # banana
print(x[-1])                # cherry

y = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(y[2:5])               # ['cherry', 'orange', 'kiwi']
print(y[:4])                # ['apple', 'banana', 'cherry', 'orange']
print(y[2:])                # ['cherry', 'orange', 'kiwi', 'melon', 'mango']


""" Range of Negative Indexes : Specify negative indexes if you want to start
the search from the end of the list. """
# Example :
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(fruits[-4:-1])        # ['orange', 'kiwi', 'melon']


""" Check if Item Exists : To determine if a specified item is present in a
list use the 'in' keyword. """
# Example : Check if 'apple' is present in the list.
fruits_list = ['apple', 'banana', 'cherry']
if 'apple' in fruits_list:
    print("Yes, 'apple' is in the fruits list.")


# Output : Yes, 'apple' is in the fruits list.


""" Change Item Value : To change the value of a specific item, refer to the
index number. """
# Example : Change the second item.
lst = ['apple', 'banana', 'cherry']
lst[1] = 'blackcurrant'
print(lst)

""" To insert more than one item, create a list with the new values, and
specify the index number where you want the new values to be inserted. """
# Example : Change the second value by replacing it with two new values.
list_fruits = ['apple', 'banana', 'cherry']
list_fruits[1] = ['blackcurrant', 'watermelon']
print(list_fruits)
# Output : ['apple', ['blackcurrant', 'watermelon'], 'cherry']


""" Change a Range of Item Values :
To change the value of items within a specific range, definea list with the
new values, and refer to the range of index numbers where you want to insert
the new values. """
# Example : Change the values 'banana' and 'cherry' with the values
# 'blackcurrant' and 'watermelon'.
fruit_list = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
fruit_list[1:3] = ['blackcurrant', 'watermelon']
print(fruit_list)
# Output : ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
