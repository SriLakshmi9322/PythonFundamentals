# 4. TimeDelta Class from DateTime Module
"""
TimeDelta Class : A duration expressing the difference between two date, time
or datetime instances to microsecond resolution.

Python timedelta class is used for calculating differences in dates and also
can be used for date manipulations in Python. It is one of the easiest ways to
perform date manipulations.
Constructor Syntax : class datetime.timedelta(days=0, seconds=0,
microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
Returns Date.
"""

# Adding days to DateTime Object
from datetime import datetime, timedelta

ini_time_for_now = datetime.now()
print("Initial Date :", str(ini_time_for_now))

future_date_after_2yrs = ini_time_for_now + timedelta(days=730)
future_date_after_2days = ini_time_for_now + timedelta(days=2)

print("Future Date after 2yrs :", str(future_date_after_2yrs))
print("Future Date after 2days :", str(future_date_after_2days))

# Output :
# Initial Date : 2024-07-16 19:25:52.923128
# Future Date after 2yrs : 2026-07-16 19:25:52.923128
# Future Date after 2days : 2024-07-18 19:25:52.923128


# Difference between two dates and times
from datetime import datetime, timedelta

ini_time_for_now = datetime.now()
print("Initial Date :", str(ini_time_for_now))

new_final_time = ini_time_for_now + \
    timedelta(days=2)
print("New Final time :", str(new_final_time))
print("Time Difference :", str(new_final_time - ini_time_for_now))

# Output :
# Initial Date : 2024-07-16 19:29:46.502861
# New Final time : 2024-07-18 19:29:46.502861
# Time Difference : 2 days, 0:00:00
