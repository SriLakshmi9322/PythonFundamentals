# Data Hiding :
"""
An object's attributes may or may not be visible outside the class definition.
You need to name attributes with a double underscore prefix, and then those
attributes are not be visible to outsiders directly. """
# Example : Program to illustrate the concept 'Data Hiding'.


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter._JustCounter__secretCount)
print(counter.__secretCount)

# Output :
# 1
# 2
# 2
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-13\tempCodeRunnerFile.py",
# line 20, in <module>
#     print(counter.__secretCount)
# AttributeError: 'JustCounter' object has no attribute '__secretCount'
