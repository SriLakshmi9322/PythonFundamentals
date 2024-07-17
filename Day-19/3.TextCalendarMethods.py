# class calendar.TextCalendar :
"""
class calendar.TextCalendar is used to generate plain text calendar also it
allows us to edit the calendar and use it as per our requirement.
There are 4 methods in TextCalendar class :
1. formatmonth()
2. prmonth()
3. formatyear()
4. pryear()
"""

# 1. formatmonth() - Retrieve month's Calendar as a multi-line string.
# Syntax: formatmonth(year, month, width=0, lines=0)
# Example-1 :
import calendar

text_cal = calendar.TextCalendar(firstweekday=0)
print(text_cal.formatmonth(2024, 3))

# Output :
#      March 2024
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31

# Example-2 :
import calendar

text_cal = calendar.TextCalendar(firstweekday=0)
print(text_cal.formatmonth(2024, 3, w=5))

# Output :
#                 March 2024
#  Mon   Tue   Wed   Thu   Fri   Sat   Sun
#                            1     2     3
#    4     5     6     7     8     9    10
#   11    12    13    14    15    16    17
#   18    19    20    21    22    23    24
#   25    26    27    28    29    30    31

# Example-3 :
import calendar

text_cal = calendar.TextCalendar(firstweekday=0)
print(text_cal.formatmonth(2024, 3, 6, 2))

# Output :
#                    March 2024

#  Mon    Tue    Wed    Thu    Fri    Sat    Sun

#                                1      2      3

#    4      5      6      7      8      9     10

#   11     12     13     14     15     16     17

#   18     19     20     21     22     23     24

#   25     26     27     28     29     30     31


# 2. prmonth() - Print the month's Calendar.
# Syntax: prmonth(year, month, width=0, lines=0)
# Example-1 :
import calendar

text_cal = calendar.TextCalendar(firstweekday=0)
print(text_cal.prmonth(2024, 3))

# Output :
#      March 2024
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31
# None

# Example-2 :
import calendar

text_cal = calendar.TextCalendar(firstweekday=0)
print(text_cal.prmonth(2024, 3, w=5))

# Output :
#                 March 2024
#  Mon   Tue   Wed   Thu   Fri   Sat   Sun
#                            1     2     3
#    4     5     6     7     8     9    10
#   11    12    13    14    15    16    17
#   18    19    20    21    22    23    24
#   25    26    27    28    29    30    31
# None

# Example-3 :
import calendar

text_cal = calendar.TextCalendar(firstweekday=0)
print(text_cal.prmonth(2024, 3, 6, 2))

# Output :
#                    March 2024

#  Mon    Tue    Wed    Thu    Fri    Sat    Sun

#                                1      2      3

#    4      5      6      7      8      9     10

#   11     12     13     14     15     16     17

#   18     19     20     21     22     23     24

#   25     26     27     28     29     30     31

# None


# 3. formatyear() - Retrieve year's calendar as a multi-line String.
# Syntax: formatyear(year, width=2, lines=1, c=6, m=3)
# c - No. of spaces between month columns
# m - No. of months in a row
# Example-1 :
import calendar

text_cal = calendar.TextCalendar(firstweekday=0)
print(text_cal.formatyear(2024, 4))

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

# Example-2 :
import calendar

text_cal = calendar.TextCalendar(firstweekday=0)
print(text_cal.formatyear(2024, 4, c=3, m=2))

# Output :
#                                   2024

#              January                              February
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#   1    2    3    4    5    6    7                     1    2    3    4
#   8    9   10   11   12   13   14      5    6    7    8    9   10   11
#  15   16   17   18   19   20   21     12   13   14   15   16   17   18
#  22   23   24   25   26   27   28     19   20   21   22   23   24   25
#  29   30   31                         26   27   28   29

#               March                                April
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#                       1    2    3      1    2    3    4    5    6    7
#   4    5    6    7    8    9   10      8    9   10   11   12   13   14
#  11   12   13   14   15   16   17     15   16   17   18   19   20   21
#  18   19   20   21   22   23   24     22   23   24   25   26   27   28
#  25   26   27   28   29   30   31     29   30

#                May                                  June
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#             1    2    3    4    5                               1    2
#   6    7    8    9   10   11   12      3    4    5    6    7    8    9
#  13   14   15   16   17   18   19     10   11   12   13   14   15   16
#  20   21   22   23   24   25   26     17   18   19   20   21   22   23
#  27   28   29   30   31               24   25   26   27   28   29   30

#                July                                August
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#   1    2    3    4    5    6    7                     1    2    3    4
#   8    9   10   11   12   13   14      5    6    7    8    9   10   11
#  15   16   17   18   19   20   21     12   13   14   15   16   17   18
#  22   23   24   25   26   27   28     19   20   21   22   23   24   25
#  29   30   31                         26   27   28   29   30   31

#             September                             October
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#                                 1           1    2    3    4    5    6
#   2    3    4    5    6    7    8      7    8    9   10   11   12   13
#   9   10   11   12   13   14   15     14   15   16   17   18   19   20
#  16   17   18   19   20   21   22     21   22   23   24   25   26   27
#  23   24   25   26   27   28   29     28   29   30   31
#  30

#              November                             December
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#                       1    2    3                                    1
#   4    5    6    7    8    9   10      2    3    4    5    6    7    8
#  11   12   13   14   15   16   17      9   10   11   12   13   14   15
#  18   19   20   21   22   23   24     16   17   18   19   20   21   22
#  25   26   27   28   29   30          23   24   25   26   27   28   29
#                                       30   31

# 4. pryear() - Print the year's Calendar.
# Syntax: pryear(year, width=2, lines=1, c=6, m=3)
# Example-1 :
import calendar

text_cal = calendar.TextCalendar(firstweekday=0)
print(text_cal.pryear(2024, 2))

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

# Example-2 :
import calendar

text_cal = calendar.TextCalendar(firstweekday=0)
print(text_cal.pryear(2024, 4, c=3, m=2))

# Output :
#                                   2024

#              January                              February
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#   1    2    3    4    5    6    7                     1    2    3    4
#   8    9   10   11   12   13   14      5    6    7    8    9   10   11
#  15   16   17   18   19   20   21     12   13   14   15   16   17   18
#  22   23   24   25   26   27   28     19   20   21   22   23   24   25
#  29   30   31                         26   27   28   29

#               March                                April
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#                       1    2    3      1    2    3    4    5    6    7
#   4    5    6    7    8    9   10      8    9   10   11   12   13   14
#  11   12   13   14   15   16   17     15   16   17   18   19   20   21
#  18   19   20   21   22   23   24     22   23   24   25   26   27   28
#  25   26   27   28   29   30   31     29   30

#                May                                  June
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#             1    2    3    4    5                               1    2
#   6    7    8    9   10   11   12      3    4    5    6    7    8    9
#  13   14   15   16   17   18   19     10   11   12   13   14   15   16
#  20   21   22   23   24   25   26     17   18   19   20   21   22   23
#  27   28   29   30   31               24   25   26   27   28   29   30

#                July                                August
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#   1    2    3    4    5    6    7                     1    2    3    4
#   8    9   10   11   12   13   14      5    6    7    8    9   10   11
#  15   16   17   18   19   20   21     12   13   14   15   16   17   18
#  22   23   24   25   26   27   28     19   20   21   22   23   24   25
#  29   30   31                         26   27   28   29   30   31

#             September                             October
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#                                 1           1    2    3    4    5    6
#   2    3    4    5    6    7    8      7    8    9   10   11   12   13
#   9   10   11   12   13   14   15     14   15   16   17   18   19   20
#  16   17   18   19   20   21   22     21   22   23   24   25   26   27
#  23   24   25   26   27   28   29     28   29   30   31
#  30

#              November                             December
# Mon  Tue  Wed  Thu  Fri  Sat  Sun    Mon  Tue  Wed  Thu  Fri  Sat  Sun
#                       1    2    3                                    1
#   4    5    6    7    8    9   10      2    3    4    5    6    7    8
#  11   12   13   14   15   16   17      9   10   11   12   13   14   15
#  18   19   20   21   22   23   24     16   17   18   19   20   21   22
#  25   26   27   28   29   30          23   24   25   26   27   28   29
#                                       30   31
# None
