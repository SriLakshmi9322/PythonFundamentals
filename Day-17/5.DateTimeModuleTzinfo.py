# 7. tzinfo class from DateTime Module
"""
tzinfo - It provides timezone information objects.

DateTime.tzinfo() : datetime.now() contains no information regarding timezones.
It only makes use of the current System time. tzinfo is an abstract base class
in Python. It cannot be directly instantiated. A concrete subclass must derive
from this abstract class and implement the methods offered by it.

The tzinfo class instance can be provided to the DateTime and time object
constructors. It is used in scenarios such as converting local time to UTC or
accounting for daylight savings time.
"""

# Example :
import datetime as dt
from dateutil import tz

tz_string = dt.datetime.now(dt.timezone.utc).astimezone().tzname()

print("datetime.now() :", tz_string)
NYC = tz.gettz("Europe / Berlin")
dt1 = dt.datetime(2022, 5, 21, 12, 0)
dt2 = dt.datetime(2022, 12, 21, 12, 0, tzinfo=NYC)

print("Naive Object :", dt1.tzname())
print("Aware Object :", dt2.tzname())

# Output :
# datetime.now() : India Standard Time
# Naive Object : None
# Aware Object : None
