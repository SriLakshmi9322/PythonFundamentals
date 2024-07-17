# Additional Functions of calendar module

# 1. setfirstweekday(weekday) - Set the first day of the week.
import calendar

first_weekday = calendar.setfirstweekday(calendar.SUNDAY)
print(first_weekday)

# Output : None

# 2. firstweekday() - Returns the first weekday number.
import calendar

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.firstweekday())

# Output : 6

# 3. isleap(year) - Checks if the year is a leap year.
import calendar

print(calendar.isleap(2024))
print(calendar.isleap(2023))

# Output :
# True
# False

# 4. leapdays(year1, year2) - Returns the no. of leap days between years.
import calendar

print(calendar.leapdays(2002, 2024))

# Output : 5

# 5. weekday(year, month, day) - Returns the weekday number for a date.
# 0 - Monday
import calendar

print(calendar.weekday(2024, 3, 9))

# Output : 5

# 6. weekheader(n) - Returns a header with abbreviated weekday names.
import calendar

print(calendar.weekheader(3))

# Output : Mon Tue Wed Thu Fri Sat Sun

# 7. monthrange(year, month) - Returns the starting weekday number and no. of
#                              days in the month.
import calendar

print(calendar.monthrange(2024, 3))

# (4, 31)

# 8. monthcalendar(year, month) - Returns a matrix representing the month's
#                                 calendar.
import calendar

print(calendar.monthcalendar(2024, 3))

# Output :
# [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17],
# [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]]

# 9. prmonth(year, month) - Prints the Calendar month.
# Syntax : prmonth(theyear, themonth, w=0, l=0)
import calendar

print(calendar.prmonth(2024, 3))

# Output :
#      March 2024
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31
# None

# 10. prcal(year) - Prints the calendar for a year.
# prcal(year, w=0, l=0, c=6, m=3)
import calendar

print(calendar.prcal(2024))

# Output :
#                                   2024

#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7                1  2  3  4                   1  2  3
#  8  9 10 11 12 13 14       5  6  7  8  9 10 11       4  5  6  7  8  9 10
# 15 16 17 18 19 20 21      12 13 14 15 16 17 18      11 12 13 14 15 16 17
# 22 23 24 25 26 27 28      19 20 21 22 23 24 25      18 19 20 21 22 23 24
# 29 30 31                  26 27 28 29               25 26 27 28 29 30 31

#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7             1  2  3  4  5                      1  2
#  8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
# 15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
# 22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
# 29 30                     27 28 29 30 31            24 25 26 27 28 29 30

#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7                1  2  3  4                         1
#  8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
# 15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
# 22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
# 29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
#                                                     30

#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6                   1  2  3                         1
#  7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
# 14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
# 21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
# 28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
#                                                     30 31
# None

# 11. month(year, month) - Prints the month of a specific year.
# Syntax : month(theyear, themonth, w=0, l=0)
import calendar

print(calendar.month(2024, 3, w=3, l=2))

# Output :
#          March 2024

# Mon Tue Wed Thu Fri Sat Sun

#                   1   2   3

#   4   5   6   7   8   9  10

#  11  12  13  14  15  16  17

#  18  19  20  21  22  23  24

#  25  26  27  28  29  30  31

# 12. calendar(year) - Displays the calendar for the given year.
# Syntax : calendar(year, w=2, l=1, c=6, m=3)
import calendar

print(calendar.calendar(2024))

# Output :
#                                   2024

#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7                1  2  3  4                   1  2  3
#  8  9 10 11 12 13 14       5  6  7  8  9 10 11       4  5  6  7  8  9 10
# 15 16 17 18 19 20 21      12 13 14 15 16 17 18      11 12 13 14 15 16 17
# 22 23 24 25 26 27 28      19 20 21 22 23 24 25      18 19 20 21 22 23 24
# 29 30 31                  26 27 28 29               25 26 27 28 29 30 31

#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7             1  2  3  4  5                      1  2
#  8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
# 15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
# 22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
# 29 30                     27 28 29 30 31            24 25 26 27 28 29 30

#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7                1  2  3  4                         1
#  8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
# 15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
# 22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
# 29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
#                                                     30

#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6                   1  2  3                         1
#  7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
# 14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
# 21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
# 28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
#                                                     30 31
