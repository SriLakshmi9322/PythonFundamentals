# Python Time Module
"""
Time Module allows us to work with time in Python. It allows functionality like
getting the current time, pausing the program from executing.

The time module comes with Python's Standard Utility module, so there is no
need to install it externally.
Syntax : import time

Epoch - The epoch is the point where the time starts and is platform-dependent.
        On windows and most unix systems, the epoch is January 1, 1970, 00:00:
        00 (UTC), and leap seconds are not counted towards the time in seconds
        since the epoch.
"""

# Example :
import time

print(time.gmtime(0))   # gmtime(0) - Time in the GMT (Greenwich Mean Time)

# Output :
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0,
# tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

"""
Note : The time before the epoch can still be represented in seconds but it
       will be negative. For example, 31 December 1969 will be represented as
       -86400 seconds.
"""


# To get current time in seconds since epoch :
import time

current_time = time.time()
print("Current Time in Seconds since epoch is :", current_time)

# Output :
# Current Time in Seconds since epoch is : 1721218853.523072


# To get time string from seconds
"""
time.ctime() - returns a 24 character time string but takes seconds as
arguement and computes time till mentioned seconds. If no arguement is passed,
time is calculated till the present.
"""
# Example :
import time

current_time = time.ctime(1721218853.523072)
print("Current Time :", current_time)

# Output : Current Time : Wed Jul 17 17:50:53 2024


# Delaying Execution of Programs
"""
Execution can be delayed using 'time.sleep()' method. This method is used to
halt the program execution for the time specified in the arguements.
"""
# Example :
import time

for i in range(4):
    time.sleep(1)           # 1 - second
    print(i)

# Output :
# 0
# 1
# 2
# 3
