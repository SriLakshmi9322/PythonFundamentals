# Destroying Object's (Garbage Collection) :

""" Python deletes unneeded object's (built-in types or class instance)
automatically to free the memory space. The process by which Python
periodically reclaims blocks of memory that no longer are in use is termed as
Garbage Collection.

Python's Garbage Collector runs during program execution and is triggered when
an object's referrence count reaches zero. An object's referrence count changes
as the number of aliases that point to it changes.

An Object's referrence count increases when it is assigned a new name or placed
in a container (list, tuple or dictionary). The object's referrence count
decreases when it is deleted with del, its referrence is reassigned, or its
referrence goes out of scope, when an object's referrence count reaches zero,
Python collects it automatically.

a = 40    # Create object <40>
b = a     # Increases ref. count of <40>
c = [b]   # Increases ref. count of <40>

del a     # Decreases ref. count of <40>
b = 100   # Decreases ref. count of <40>
c[0] = -1 # Decreases ref. count of <40>

We normally will not notice when the garbage collector destroys an orphaned
instance and reclaims its space. But a class can implement the special method
__del__(), called a destructor, that is invoked when the instance is about to
be destroyed. This method might be used to clean up any non-memory resources
used by an instance. """

# Example : This __del__() prints the class name of an instance that is about
# to be destroyed-


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed.!!")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))        # Prints the id's of the objects
del pt1
del pt2
del pt3

# Output :
# 2293295833344 2293295833344 2293295833344
# Point destroyed.!!
