# 2. Time Class from DateTime Module
"""
An idealized time, independent of any particular day, assuming that every day
has exactly 24*60*60. It's attributes are hour, minute, second, microsecond &
tzinfo.

Python Time Class : It creates time object which represent local time,
independent of any day.
Constructor Syntax : class datetime.time(hour=0, minute=0, second=0,
microsecond=0, tzinfo=None, *, fold=0)

All the arguements are Optional. tzinfo can be None. Otherwise all the
attributes must be integer in the following Range :
0 <= hour < 24
0 <= minute < 60
0 <= second < 60
0 <= microsecond < 1000000
fold in [0, 1]
"""

# Example-1 : Time Object representing time in Python
from datetime import time

my_time = time(13, 24, 56)
print("Entered Time :", my_time)

# With Single Arguement
my_time = time(minute=12)
print("Time with one Arguement :", my_time)

# With Zero Arguement
my_time = time()
print("Time without Arguement :", my_time)

# Output :
# Entered Time : 13:24:56
# Time with one Arguement : 00:12:00
# Time without Arguement : 00:00:00


# Example-2 : To Get hours, minutes, seconds & microseconds individually
from datetime import time

Time = time(11, 34, 56)
print("Hour :", Time.hour)
print("Minute :", Time.minute)
print("Second :", Time.second)
print("Microseconds :", Time.microsecond)

# Output :
# Hour : 11
# Minute : 34
# Second : 56
# Microseconds : 0


# Example-3 : Convert Time object to String
from datetime import time

Time = time(12, 24, 36, 1212)
str_time = Time.isoformat()

print("String Representation :", str_time)
print(type(str))

# Output :
# String Representation : 12:24:36.001212
# <class 'type'>
