# Importing statistics module
import statistics

# (ii) Python - Statistics Module
# The Statistics module provides functions to mathematical statistics of
# numeric data. E.g., mean(), median(), mode() & stdev()

# mean() - calculates the arithmetic mean of the numbers in a list
print(statistics.mean([2, 5, 6, 9]))            # 5.5

# median() - returns the middle value of numeric data in a list
print(statistics.median([1, 2, 3, 8, 9]))       # 3
print(statistics.median([1, 2, 3, 7, 8, 9]))    # 5.0

# mode() - returns the most common data point in the list
print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4, 2, 5, 6]))   # 2

# stdev() - calculates the standard deviation on a given sample in the form
# of a list
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]))
# Output :   1.3693063937629153
