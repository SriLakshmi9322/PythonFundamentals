# 6. TimeZone class from DateTime Module
"""
TimeZone Class : A class that implements the tzinfo abstract base class as a
fixed offset from the UTC (Coordinated Universal Time).

Time Zones in DateTime can be  used in the case where one might want to display
time according to the time zone of a specific region. This can be done using
the pytz module of Python. This module serves the date-time conversion
functionalities and helps users serving international client bases.
"""

# Example :
from datetime import datetime
from pytz import timezone

format = "%Y-%m-%d %H:%M:%S %Z%z"

now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(format))

timezones = ['Asia/Kolkata', 'Europe/Kiev', 'America/New_York']

for tzone in timezones:
    now_asia = now_utc.astimezone(timezone(tzone))
    print(now_asia.strftime(format))

# Output :
# 2024-07-16 14:48:27 UTC+0000
# 2024-07-16 20:18:27 IST+0530
# 2024-07-16 17:48:27 EEST+0300
# 2024-07-16 10:48:27 EDT-0400
