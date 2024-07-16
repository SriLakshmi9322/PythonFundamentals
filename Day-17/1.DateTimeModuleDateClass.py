# DateTime Module
"""
DateTime Module is a built-in module that supplies class to work with Date
and Time.
These classes provides several functions to deal with dates, times and time
intervals.
This module is categorized into 6 main classes :
1. date
2. time
3. datetime
4. timedelta
5. tzinfo
6. timezone
"""

# 1. Date Class from DateTime module
"""
Date Class : An idealized naive date, assuming the current Gregorian Calendar
always was and always will be. It's attributes are year, month & day.
This class represents date in the format of 'YYYY-MM-DD'. The Constructor of
this class needs 3 mandatory arguements : 1. year
                                          2. month
                                          3. date
Syntax : class datetime.date(year, month, date)
Range of arguements :
for year  - 1 <= year <= MAXYEAR
for month - 1 <= month <= 12
for date  - 1 <= day <= no. of days in the given month/year.

If range exceeds it will cause 'TypeError'.
"""

# Date Object representing date in Python
from datetime import date

my_date = date(1996, 12, 11)
print("Date Passes as arguement is :", my_date)

# Output : Date Passes as arguement is : 1996-12-11


# To get current date
from datetime import date

today = date.today()
print("Today's date is :", today)

# Output : Today's date is : 2024-07-16


# To get today's year, month & date individually
from datetime import date

today = date.today()
print("Current Year :", today.year)
print("Current Month :", today.month)
print("Current Day :", today.day)

# Output :
# Current Year : 2024
# Current Month : 7
# Current Day : 16


# To get date from TimeStamp
"""
We can create date objects from timestamps using the fromtimestamp() method.
The timestamp is the no. of seconds from 1st January 1970 at UTC (Coordinated
Universal Time) to a particular Date.
"""
from datetime import datetime

date_time = datetime.fromtimestamp(1887639468)
print("DateTime from timestamp :", date_time)

# Output : DateTime from timestamp : 2029-10-25 21:47:48


# To convert Date to String
"""
We can convert date object to a string representation using 2 functions :
1. isoformat()
2. strftime()
"""
from datetime import date

today = date.today()
str_date = date.isoformat(today)
print("String Representation :", str_date)
print(type(str_date))

# Output :
# String Representation : 2024-07-16
# <class 'str'>
