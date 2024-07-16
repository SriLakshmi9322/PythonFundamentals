# 3. DateTime class from DataTime Module
"""
DateTime Class : It is a combination of date & time along with the attributes
year, month, day, hour, minute, second, microsecond & tzinfo.

DateTime class contains information on both date & time. Like a date object,
datetime assumes the current Gregorian Calendar extended in both directions,
Like a time object, datetime assumes there are exactly 3600*24 seconds in every
day.
Constructor Syntax : class datetime.datetime(year, month, day, hour=0, minute=0,
second=0, microsecond=0, tzinfo=None, *, fold=0)
Here, year, month & day arguements are mandatory. tzinfo can be None, rest
attributes must be an integer in the following range :
MINYEAR <= year <= MAXYEAR
1 <= month <= 12
1 <= day <= no. of days in the given month & year
0 <= hour < 24
0 <= minute < 60
0 <= second < 60
0 <= microsecond < 1000000
fold in [0, 1]

Otherthan integer type results 'TypeError'
Out of Range results 'ValueError'
"""

# DateTime Object representing DateTime in Python
from datetime import datetime

a = datetime(1999, 12, 12)
print(a)

a = datetime(1999, 12, 12, 12, 12, 12, 342380)
print(a)

# Output :
# 1999-12-12 00:00:00
# 1999-12-12 12:12:12.342380


# To get year, month, hour, minute & timestamp
from datetime import datetime

a = datetime(1999, 12, 12, 12, 12, 12)
print("Year :", a.year)
print("Month :", a.month)
print("Hour :", a.hour)
print("Minute :", a.minute)
print("TimeStamp :", a.timestamp())

# Output :
# Year : 1999
# Month : 12
# Hour : 12
# Minute : 12
# TimeStamp : 944980932.0


# Current Date & Time
from datetime import datetime

today = datetime.now()
print("Current Date & Time is :", today)

# Output : Current Date & Time is : 2024-07-16 19:03:26.431180


# Convert Python DateTime to String
from datetime import datetime as dt

current_date = dt.now()
str_current_date = dt.isoformat(current_date)
print(str_current_date)
print(type(str_current_date))

# Output :
# 2024-07-16T19:07:08.575650
# <class 'str'>


# Format DateTime in Python
"""
In different countries the format of date is of different like date canbe of
format either 'dd-mm-yyyy' or can also be 'yyyy-mm-dd'.
To format datetime we have 2 functions : 1. strftime()
                                         2. strptime()
"""

# 1. Python DateTime strftime
"""
strftime() method converts the given date, time or datetime object to the
string representation of the given format.
"""
# Example :
from datetime import datetime as dt

now = dt.now()
print("Without formatting :", now)
# Example-1
s = now.strftime("%A %m %Y")
print("Example 1:", s)
# Example-2
s = now.strftime("%a %m %y")
print("Example 2:", s)
# Example-3
s = now.strftime("%I %p %S")
print("Example 3:", s)
# Example-4
s = now.strftime("%H:%M:%S")
print("Example 4:", s)

# Output :
# Without formatting : 2024-07-16 19:43:28.922000
# Example 1: Tuesday 07 2024
# Example 2: Tue 07 24
# Example 3: 07 PM 28
# Example 4: 19:43:28

# 2. Python DateTime strptime
"""
strptime() method creates a DateTime Object from the given String.
"""
# Example :
from datetime import datetime

time_data = ["25/05/99 02:35:8.023", "26/05/99 12:45:0.003",
             "27/05/99 07:35:5.523", "28/05/99 05:15:55.523"]

format_data = "%d/%m/%y %H:%M:%S.%f"

for i in time_data:
    print(datetime.strptime(i, format_data))

# Output :
# 1999-05-25 02:35:08.023000
# 1999-05-26 12:45:00.003000
# 1999-05-27 07:35:05.523000
# 1999-05-28 05:15:55.523000
