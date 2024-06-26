# Importing random module
import random

# (iii) Python - Random Module
# Functions in the random module depend on a pseudo-random number generator
# function random(), which generatesa random float number between 0.0 & 1.0.

# random.random() - generates a random float number between 0.0 to 1.0
# The function doesn't need any arguement.
print(random.random())          # 0.13497850303118875

# random.randint() -  returns a random integer between the specified integers
print(random.randint(1, 100))   # 20
print(random.randint(1, 100))   # 91

# random.randrange() - returns a randomly selected element from the range
# created by the start, stop & step arguements. The value of start is 0 by
# default. Similarly, the value of step is 1 by default.
print(random.randrange(1, 10))          # 2
print(random.randrange(1, 10, 2))       # 5
print(random.randrange(0, 101, 10))     # 50

# random.choice() - returns a randomly selected element from a non-empty
# sequence. An empty sequence as arguement raises an IndexError.
print(random.choice('computer'))                # u
print(random.choice([12, 23, 45, 67, 65, 43]))  # 67
print(random.choice([12, 23, 45, 67, 65, 43]))  # 45

# random.shuffle() - randomly re-orders the elements in a list
numbers = [12, 23, 45, 67, 65, 43]
random.shuffle(numbers)
print(numbers)                          # [45, 43, 23, 65, 67, 12]
random.shuffle(numbers)
print(numbers)                          # [12, 65, 43, 23, 67, 45]
