# Python program to Convert a string of bits into decimal Integer.

binary_string = input("Enter a String of bits : ")
decimal = 0
exponent = len(binary_string) - 1
for i in binary_string:
    decimal = decimal + int(i) * 2 ** exponent
    exponent = exponent - 1

print("The integer value is :", decimal)

# Output-1 :
# Enter a String of bits : 0101
# The integer value is : 5

# Output-2 :
# Enter a String of bits : 1111111111
# The integer value is : 1023
