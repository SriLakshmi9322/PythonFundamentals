# Python Calendar Module
"""
Python Calendar Module allows us to output calendars like the program and
provides additional useful functions related to the calendar.
"""

# To display the Python Calendar of a given Month
# Example :
import calendar

yy = 2024
mm = 3
print(calendar.month(yy, mm))

# Output :
#      March 2024
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31


# To display the Python Calendar of the given Year
# Example :
import calendar

print("The Calendar of Year '2024' is :")
print(calendar.calendar(2024))

# Output :
# The Calendar of Year '2024' is :
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
