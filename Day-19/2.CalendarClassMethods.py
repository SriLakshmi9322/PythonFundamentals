# class calendar.Calendar :
"""
class calendar.Calendar methods are used for preparing the calendar data for
formatting.
"""

# 1. iterweekdays() - Iterator for weekday numbers used in a week.
import calendar

obj = calendar.Calendar(firstweekday=0)     # 0 - starting weekday number

for day in obj.iterweekdays():
    print(day)

# Output :
# 0
# 1
# 2
# 3
# 4
# 5
# 6

# 2. itermonthdates() - Iterator for dates in a specified month.
from calendar import Calendar

obj = Calendar(firstweekday=4)
for day in obj.itermonthdates(2024, 3):
    print(day)

# Output :
# 2024-03-01
# 2024-03-02
# 2024-03-03
# 2024-03-04
# 2024-03-05
# 2024-03-06
# 2024-03-07
# 2024-03-08
# 2024-03-09
# 2024-03-10
# 2024-03-11
# 2024-03-12
# 2024-03-13
# 2024-03-14
# 2024-03-15
# 2024-03-16
# 2024-03-17
# 2024-03-18
# 2024-03-19
# 2024-03-20
# 2024-03-21
# 2024-03-22
# 2024-03-23
# 2024-03-24
# 2024-03-25
# 2024-03-26
# 2024-03-27
# 2024-03-28
# 2024-03-29
# 2024-03-30
# 2024-03-31
# 2024-04-01
# 2024-04-02
# 2024-04-03
# 2024-04-04

# 3. itermonthdays() - Iterator for days of a specified month.
from calendar import Calendar

obj = Calendar()
for day in obj.itermonthdays(2024, 3):
    print(day, end=" ")

# Output :
# 0 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
# 27 28 29 30 31

# 4. itermonthdays2() - Iterator with days as tuples days, weekday number.
from calendar import Calendar

obj = Calendar(firstweekday=4)
for day in obj.itermonthdays2(2024, 3):
    print(day, end=" ")

# Output :
# (1, 4) (2, 5) (3, 6) (4, 0) (5, 1) (6, 2) (7, 3) (8, 4) (9, 5) (10, 6)
# (11, 0) (12, 1) (13, 2) (14, 3) (15, 4) (16, 5) (17, 6) (18, 0) (19, 1)
# (20, 2) (21, 3) (22, 4) (23, 5) (24, 6) (25, 0) (26, 1) (27, 2) (28, 3)
# (29, 4) (30, 5) (31, 6) (0, 0) (0, 1) (0, 2) (0, 3)

# 5. itermonthdays3() - Iterator with tuples year, month, day, weekday number.
from calendar import Calendar

obj = Calendar(firstweekday=4)
for day in obj.itermonthdays3(2024, 3):
    print(day)

# Output :
# (2024, 3, 1)
# (2024, 3, 2)
# (2024, 3, 3)
# (2024, 3, 4)
# (2024, 3, 5)
# (2024, 3, 6)
# (2024, 3, 7)
# (2024, 3, 8)
# (2024, 3, 9)
# (2024, 3, 10)
# (2024, 3, 11)
# (2024, 3, 12)
# (2024, 3, 13)
# (2024, 3, 14)
# (2024, 3, 15)
# (2024, 3, 16)
# (2024, 3, 17)
# (2024, 3, 18)
# (2024, 3, 19)
# (2024, 3, 20)
# (2024, 3, 21)
# (2024, 3, 22)
# (2024, 3, 23)
# (2024, 3, 24)
# (2024, 3, 25)
# (2024, 3, 26)
# (2024, 3, 27)
# (2024, 3, 28)
# (2024, 3, 29)
# (2024, 3, 30)
# (2024, 3, 31)
# (2024, 4, 1)
# (2024, 4, 2)
# (2024, 4, 3)
# (2024, 4, 4)

# 6. itermonthdays4() - Similar to itermonthdays3(), restricted to a datetime
#                       date range.
from calendar import Calendar

obj = Calendar(firstweekday=4)
for day in obj.itermonthdays4(2024, 3):
    print(day)

# Output :
# (2024, 3, 1, 4)
# (2024, 3, 2, 5)
# (2024, 3, 3, 6)
# (2024, 3, 4, 0)
# (2024, 3, 5, 1)
# (2024, 3, 6, 2)
# (2024, 3, 7, 3)
# (2024, 3, 8, 4)
# (2024, 3, 9, 5)
# (2024, 3, 10, 6)
# (2024, 3, 11, 0)
# (2024, 3, 12, 1)
# (2024, 3, 13, 2)
# (2024, 3, 14, 3)
# (2024, 3, 15, 4)
# (2024, 3, 16, 5)
# (2024, 3, 17, 6)
# (2024, 3, 18, 0)
# (2024, 3, 19, 1)
# (2024, 3, 20, 2)
# (2024, 3, 21, 3)
# (2024, 3, 22, 4)
# (2024, 3, 23, 5)
# (2024, 3, 24, 6)
# (2024, 3, 25, 0)
# (2024, 3, 26, 1)
# (2024, 3, 27, 2)
# (2024, 3, 28, 3)
# (2024, 3, 29, 4)
# (2024, 3, 30, 5)
# (2024, 3, 31, 6)
# (2024, 4, 1, 0)
# (2024, 4, 2, 1)
# (2024, 4, 3, 2)
# (2024, 4, 4, 3)

# 7. monthdatescalendar() - List of weeks in a specified month.
from calendar import Calendar

obj = Calendar(firstweekday=4)
print(obj.monthdatescalendar(2024, 3))

# Output :
# [[datetime.date(2024, 3, 1), datetime.date(2024, 3, 2),
# datetime.date(2024, 3, 3), datetime.date(2024, 3, 4),
# datetime.date(2024, 3, 5), datetime.date(2024, 3, 6),
# datetime.date(2024, 3, 7)], [datetime.date(2024, 3, 8),
# datetime.date(2024, 3, 9), datetime.date(2024, 3, 10),
# datetime.date(2024, 3, 11), datetime.date(2024, 3, 12),
# datetime.date(2024, 3, 13), datetime.date(2024, 3, 14)],
# [datetime.date(2024, 3, 15), datetime.date(2024, 3, 16),
# datetime.date(2024, 3, 17), datetime.date(2024, 3, 18),
# datetime.date(2024, 3, 19), datetime.date(2024, 3, 20),
# datetime.date(2024, 3, 21)], [datetime.date(2024, 3, 22),
# datetime.date(2024, 3, 23), datetime.date(2024, 3, 24),
# datetime.date(2024, 3, 25), datetime.date(2024, 3, 26),
# datetime.date(2024, 3, 27), datetime.date(2024, 3, 28)],
# [datetime.date(2024, 3, 29), datetime.date(2024, 3, 30),
# datetime.date(2024, 3, 31), datetime.date(2024, 4, 1),
# datetime.date(2024, 4, 2), datetime.date(2024, 4, 3),
# datetime.date(2024, 4, 4)]]

# 8. monthdayscalendar() - List of weeks in a month.
from calendar import Calendar

obj = Calendar(firstweekday=4)
print(obj.monthdayscalendar(2024, 3))

# Output :
# [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14],
# [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28],
# [29, 30, 31, 0, 0, 0, 0]]

# 9. monthdays2calendar() - List of weeks with full weeks in a specific month.
from calendar import Calendar

obj = Calendar(firstweekday=4)
print(obj.monthdays2calendar(2024, 3))

# Output :
# [[(1, 4), (2, 5), (3, 6), (4, 0), (5, 1), (6, 2), (7, 3)], [(8, 4), (9, 5),
# (10, 6), (11, 0), (12, 1), (13, 2), (14, 3)], [(15, 4), (16, 5), (17, 6),
# (18, 0), (19, 1), (20, 2), (21, 3)], [(22, 4), (23, 5), (24, 6), (25, 0),
# (26, 1), (27, 2), (28, 3)], [(29, 4), (30, 5), (31, 6), (0, 0), (0, 1),
# (0, 2), (0, 3)]]

# 10. yeardatescalendar() - List of weeks for a specified month.
from calendar import Calendar

obj = Calendar(firstweekday=0)
print(obj.yeardatescalendar(2024, 3))

# Output :
# [[[[datetime.date(2024, 1, 1), datetime.date(2024, 1, 2),
# datetime.date(2024, 1, 3), datetime.date(2024, 1, 4),
# datetime.date(2024, 1, 5), datetime.date(2024, 1, 6),
# datetime.date(2024, 1, 7)], [datetime.date(2024, 1, 8),
# datetime.date(2024, 1, 9), datetime.date(2024, 1, 10),
# datetime.date(2024, 1, 11), datetime.date(2024, 1, 12),
# ...
# ...
# datetime.date(2025, 1, 4), datetime.date(2025, 1, 5)]]]]

# 11. yeardayscalendar() - List of day number for a specified year.
from calendar import Calendar

obj = Calendar()
print(obj.yeardayscalendar(2024))

# Output :
# [[[[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14],
# [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28],
# [29, 30, 31, 0, 0, 0, 0]], [[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11],
# [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25],
# [26, 27, 28, 29, 0, 0, 0]], [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10],
# [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24],
# [25, 26, 27, 28, 29, 30, 31]]], [[[1, 2, 3, 4, 5, 6, 7],
# [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21],
# [22, 23, 24, 25, 26, 27, 28], [29, 30, 0, 0, 0, 0, 0]],
# [[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12],
# [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26],
# [27, 28, 29, 30, 31, 0, 0]], [[0, 0, 0, 0, 0, 1, 2], [3, 4, 5, 6, 7, 8, 9],
# [10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23],
# [24, 25, 26, 27, 28, 29, 30]]], [[[1, 2, 3, 4, 5, 6, 7],
# [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21],
# [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 0, 0, 0, 0]],
# [[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11],
# [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25],
# [26, 27, 28, 29, 30, 31, 0]], [[0, 0, 0, 0, 0, 0, 1],
# [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15],
# [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29],
# [30, 0, 0, 0, 0, 0, 0]]], [[[0, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13],
# [14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27],
# [28, 29, 30, 31, 0, 0, 0]], [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10],
# [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24],
# [25, 26, 27, 28, 29, 30, 0]], [[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8],
# [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22],
# [23, 24, 25, 26, 27, 28, 29], [30, 31, 0, 0, 0, 0, 0]]]]

# 12. year2dayscalendar() - List of days with full months in a specified year.
from calendar import Calendar

obj = Calendar()
print(obj.yeardays2calendar(2024))

# Output :
# [[[[(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)], [(8, 0), (9, 1),
# (10, 2), (11, 3), (12, 4), (13, 5), (14, 6)], [(15, 0), (16, 1), (17, 2),
# (18, 3), (19, 4), (20, 5), (21, 6)], [(22, 0), (23, 1), (24, 2), (25, 3),
# (26, 4), (27, 5), (28, 6)], [(29, 0), (30, 1), (31, 2), (0, 3), (0, 4),
# (0, 5), (0, 6)]], [[(0, 0), (0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 6)],
# [(5, 0), (6, 1), (7, 2), (8, 3), (9, 4), (10, 5), (11, 6)], [(12, 0),
# ...
# ...
# ...
# (27, 4), (28, 5), (29, 6)], [(30, 0), (31, 1), (0, 2), (0, 3), (0, 4),
# (0, 5), (0, 6)]]]]
