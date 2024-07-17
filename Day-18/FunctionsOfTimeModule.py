# Functions of Time Module
"""
Time Module has struct_time Class :
time.struct_class Class - struct_class helps to access local time.
i.e, non-epochal timestamps. It returns a named tuple whose value can be
accessed by both index & attribute name.
Syntax : time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0,
                            tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1,
                            tm_isdst=0)
-------------------------------------------------
Index   Attribute_Name      Values
-------------------------------------------------
0       tm_year             0000, ...., 9999
1       tm_mon              1, 2, ..., 11, 12
2       tm_mday             1, 2, ..., 30, 31
3       tm_hour             0, 1, ..., 22, 23
4       tm_min              0, 1, ..., 58, 59
5       tm_sec              0, 1, ..., 60, 61
6       tm_wday             0, 1, ..., 6, sun-6
7       tm_yday             1, 2, ..., 365, 366
8       tm_isdst            0, 1 or -1
-------------------------------------------------

This class contains various functions. They are:
"""

# 1. time.localtime() method :
"""
This method returns the struct_time object in localtime. It takes epoch as an
arguement (no. of seconds), Default it takes current time as an arguement.
"""
# To get local time from epoch
import time

obj = time.localtime(1721218853.523072)
print(obj)

# Output :
# time.struct_time(tm_year=2024, tm_mon=7, tm_mday=17, tm_hour=17, tm_min=50,
# tm_sec=53, tm_wday=2, tm_yday=199, tm_isdst=0)


# 2. time.mktime() method :
"""
It is inverse function of 'time.localtime()'. It converts thr epoch value into
seconds.
"""
# Example
import time

obj1 = time.gmtime(1721218853.523072)
time_sec = time.mktime(obj1)
print("Local Time (in seconds) :", time_sec)

# Output : Local Time (in seconds) : 1721199053.0


# 3. time.gmtime() method :
"""
time.gmtime() Converts a specified timestamp into a 'time.struct_time' object
representing the corresponding date & time in the GMT (Greenwich Mean Time)
timezone.
"""
# Example :
import time

obj = time.gmtime(1721218853.523072)
print(obj)

# Output :
# time.struct_time(tm_year=2024, tm_mon=7, tm_mday=17, tm_hour=12, tm_min=20,
# tm_sec=53, tm_wday=2, tm_yday=199, tm_isdst=0)


# 4. time.strftime() method :
# This method converts struct_time object to a string.
from time import gmtime, strftime

s = strftime("%a, %d %b %Y %H:%M:%S", gmtime(1721218853.523072))
print(s)

# Output : Wed, 17 Jul 2024 12:20:53


# 5. time.asctime() method :
"""
This method used for converting tuple to 'time.struct_time' object to string.
Sample : Day Mon Date  Hour:Min:Sec Year
"""
# Example :
import time

obj = time.gmtime(1721218853.523072)
time_str = time.asctime(obj)
print(time_str)

obj = time.localtime(1721218853.523072)
time_str = time.asctime(obj)
print(time_str)

# Output :
# Wed Jul 17 12:20:53 2024
# Wed Jul 17 17:50:53 2024


# 6. time.strptime() method :
# Converts string into struct_time class object.
# Example :
import time

string = "Wed, 17 Jul 2024 17:50:53"
obj = time.strptime(string, "%a, %d %b %Y %H:%M:%S")
print(obj)

# Output :
# time.struct_time(tm_year=2024, tm_mon=7, tm_mday=17, tm_hour=17, tm_min=50,
# tm_sec=53, tm_wday=2, tm_yday=199, tm_isdst=-1)
