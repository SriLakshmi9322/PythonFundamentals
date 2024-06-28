# Python program to convert a Decimal integer to Binary

decimal = int(input("Enter a Decimal Integer : "))
if decimal == 0:
    print(0)

else:
    print("Quotient Remainder Binary")
    binary_string = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary_string = str(remainder) + binary_string
        print("%5d%8d%12s" % (decimal, remainder, binary_string))
print("The Binary representation is", binary_string)

# Output-1 :
# Enter a Decimal Integer : 10
# Quotient Remainder Binary
#     5       0           0
#     2       1          10
#     1       0         010
#     0       1        1010
# The Binary representation is 1010

# Output-2 :
# Enter a Decimal Integer : 99
# Quotient Remainder Binary
#    49       1           1
#    24       1          11
#    12       0         011
#     6       0        0011
#     3       0       00011
#     1       1      100011
#     0       1     1100011
# The Binary representation is 1100011
