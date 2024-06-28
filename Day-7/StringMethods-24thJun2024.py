# String Methods - Python has a set of built-in methods that
# you can use on strings.
# Note : All string methods returns new values.
# They do not change the original String.

# 1. capitalize() - Converts the first character to upper case
# Example-1 :
str = "Python is a trending programming language"
str.capitalize()
print(str)      # Python is a trending programming language

# Example-2 : # for integer strings it will not work
txt = "522616 is a pincode"
txt.capitalize()
print(txt)      # 522616 is a pincode


# 2. casefold() - Converts string into lower case
""" This method is similar to the lower() method, but the casefold()
method is stronger, more aggressive, meaning that it will convert
more characters into lower case, and will find more matches when
comparing two strings and both are converted using the casefold()
method """
# Example-1 :
str = "PYTHON IS A TRENDING PROGRAMMING LANGUAGE"
print(str.casefold())       # python is a trending programming language

# Example-2 :
str1 = "Hello"
str2 = "hello"
if str1.casefold() == str2.casefold():
    print("The Strings are Equal (Case-Insensitive)")
else:
    print("The Strings are not Equal")
# Output :          The Strings are Equal (Case-Insensitive)


# 3. center() - Returns a centered string
""" The center() method will center align the string, using a specified
character (space is default) as the fill character
Syntax : string.center(length, character)
1. length - Required. The length of the returned string.
2. character - Optional. The character to fill the missing space on each side.
Default is space (" ") """
# Example-1 : Print the word "Engineering", taking up the space of 128
# characters, with "Engineering" in the middle.
word_center = "Engineering"
print(word_center.center(64))
# Output :                           Engineering

# Example-2 : Using the letter 'O' as the padding character
word_centerO = "Engineering"
print(word_centerO.center(28, 'O'))
# Output : OOOOOOOOEngineeringOOOOOOOOO


# 4. count() - Returns the number of times a specified value occurs in a string
""" Syntax : string.count(value, string, end)
1. value - Required. A String. The string value to search for
2. start - Optional. An integer. The position to start the search. Default is 0
3. stop - Optional. An inter. The position to end the search.
Default is the end of the string. """
# Example-1 : Returns the number of times the value 'is' appears in the string
word_count = "My favourite subject is Programming, Python is a programming\
language"
print(word_count.count('is'))           # 2

# Example-2 : Search from position 10 to 24
word_count1 = "My favourite subject is Programming, Python is a programming\
language"
print(word_count1.count('is', 10, 24))  # 1


# 5. encode() - Returns an encoded version of the string
""" The encode() method encodes the string, using the specified encoding.
If no encoding is specified, UTF-8 will be used.
Syntax : string.encode(encoding=encoding, errors=errors)
1. encoding - Optional. A string specifying the encoding to use.
Default is UTF-8.
2. errors - Optional. A string specifying the error method.
Legal values are :
 i) 'backslashreplace' - Uses a backslash instead of the character that
could not be encoded.
 ii) 'ignore' - Ignores the characters that cannot be encoded.
 iii) 'namereplace' - Replaces the character with a text explaining the
character.
 iv) 'strict' - Default, raises an error on failure.
 v) 'replace' - Replaces the character with a questionmark.
 vi) 'xmlcharrefreplace' - Replaces the character with an xml character. """
# Example-1 :
word_encode = "My name is Ståle"
print(word_encode.encode(encoding='ascii', errors='backslashreplace'))
print(word_encode.encode(encoding='ascii', errors='ignore'))
print(word_encode.encode(encoding='ascii', errors='namereplace'))
print(word_encode.encode(encoding='ascii', errors='replace'))
print(word_encode.encode(encoding='ascii', errors='xmlcharrefreplace'))
print(word_encode.encode(encoding='ascii', errors='strict'))

# Output :
# b'My name is St\\xe5le'
# b'My name is Stle'
# b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
# b'My name is St?le'
# b'My name is St&#229;le'
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-7\tempCodeRunnerFile.py",
# line 8, in <module>
#     print(word_encode.encode(encoding='ascii', errors='strict'))
# UnicodeEncodeError: 'ascii' codec can't encode character '\xe5' in
# position 13: ordinal not in range(128)


# 6. endswith() - Returns True if the string ends with the specified value,
# Otherwise False
""" Syntax : string.endswith(value, start, end)
 1. value - Required. The value to check if the string ends with.
 2. start - Optional. An integer specifying at which position to start
the search.
 3. end - Optional. An integer specifying at which position to end the search.
"""
# Example-1 :
word_endswith = "Hello, Welcome to my world."
print(word_endswith.endswith('my world.'))              # True

# Example-2 :
word_endswith1 = "Hello, Welcome to my world."
print(word_endswith1.endswith('my world.', 5, 11))      # False


# 7. expandtabs() - Sets the tab size to the number of specified number of
# whitespaces.
""" string.exandtabs(tabsize)
tabsize - Optional. A number specifying the tabsize.
Default tabsize is 8. """
# Example-1 :
word_exapandtabs = "H\te\tl\tl\to"
print(word_exapandtabs)
print(word_exapandtabs.expandtabs())
print(word_exapandtabs.expandtabs(2))
print(word_exapandtabs.expandtabs(4))
print(word_exapandtabs.expandtabs(10))

# Output :
# H       e       l       l       o
# H       e       l       l       o
# H e l l o
# H   e   l   l   o
# H         e         l         l         o


# 8. find() - Searches the string  for a specified value and returns the
# position of where it was found.
""" The find() method finds the first occurrence of the specified value.
The find() method returns -1 if the value is not found.
The find() method is almost the same as the index() method, the only
difference is that the index() method raises an exception if the value
is not found.
Syntax : string.find(value, start, end)
1. value - Required. The value to search for.
2. start - Optional. Where to start the search. Default is 0.
3. end - Optional. Where to end the search. Default is the end of the string.
"""
# Example-1 :
word_find = "Hello, Welcome to my world."
print(word_find.find('Welcome'))            # 7

# Example-2 :
word_find1 = "Hello, Welcome to my world."
print(word_find1.find('e', 5, 10))          # 8

# Example-3 :
word_find2 = "Hello, Welcome to my world."
print(word_find2.find('q'))                 # -1
print(word_find2.index('q'))
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-7\tempCodeRunnerFile.py",
# line 4, in <module>
#     print(word_find2.index('q'))
# ValueError: substring not found


# 9. index() - Searches the string for a specified value and returns the
# position of where it was found.
""" The index() method finds the first occurrence of the specified value.
The index() method raises an exception if the value is not found.
The index() method is almost the same as the find() method, the only difference
is that the find() method returns -1 if the value is not found.
Syntax : string.index(value, start, end)
1. value - Required. The value to search for.
2. start - Optional. Where to start the search. Default is 0.
3. end - Optional. Where to end the search. Default is to the end of the
string. """
# Example-1 :
word_index = "Hello, Welcome to my world."
print(word_index.index('Welcome'))              # 7

# Example-2 :
word_index1 = "Hello, Welcome to my world."
print(word_index1.index('e'))                   # 1


# 10. isalnum() - Returns True if all characters in the string are
# alphanumeric (combination of both alphabets & numbers).
""" The isalnum() method returns True if all the characters are alphanumeric,
meaning alphabet letter (a-z) and numbers (0-9).
Example of characters that are not alphanumeric:(space)!#%&? etc.,
Syntax : string.isalnum() """
# Example-1 :
word_alnum = "SriLakshmi9322"
print(word_alnum.isalnum())             # True


# Example-2 :
word_alnum1 = "SriLakshmi 9322"
print(word_alnum1.isalnum())        # False - Because whitespace before 9322


# 11. isalpha() - Returns True if all characters in the string are in the
# alphabet.
""" The isalpha() method returns True if all the characters are alphabet
letters(a-z).
Example of characters that are not alphabet letters:(space)!#%&? etc.,
Syntax : string.alpha() """
# Example-1 :
word_alpha = "CompanyXYZ"
print(word_alpha.isalpha())         # True

# Example-2 :
word_alpha1 = "Company123"
print(word_alpha1.isalpha())         # False


# 12. isdecimal() - Returns True if all characters in the string are decimals
""" The isdecimal() method returns True if all the characters are decimals(0-9)
This method is used on unicode objects.
Syntax : string.isdecimal() """
# Example-1 :
word_decimal = "\u0033"
print(word_decimal.isdecimal())     # True

# Example-2 :
unicode_0 = "\u0030"        # Unicode for '0'
unicode_G = "\u0047"        # Unicode for 'G'
print(unicode_0.isdecimal())        # True
print(unicode_G.isdecimal())        # False


# 13. isdigit() - Returns True if all characters in the string are digits
""" The isdigit() method returns True if all the characters are digits,
Otherwise False.
Exponents like ² are also considered to be a digit.
Syntax : string.isdigit() """
# Example-1 :
word_digit = "50800"
print(word_digit.isdigit())         # True

# Example-2 :
zero_unicode = "\u0030"             # Unicode for '0'
square_unicode = "\u00B2"           # Unicode for '²'
print(zero_unicode.isdigit())       # True
print(square_unicode.isdigit())     # True


# 14. isidentifier() - Returns True if the string is an identifier
""" A string is considered a valid identifier if it only contains alphanumeric
letters (a-z) and (0-9) or underscores (_).
A valid identifier cannot start with a number, or contain any spaces.
Syntax : string.isidentifier() """
# Example-1 :
word_identifier = "Demo"
print(word_identifier.isidentifier())       # True

# Example-2 :
my_folder = "MyFolder"
not_identifier = "2Name"
print(my_folder.isidentifier())             # True
print(not_identifier.isidentifier())        # False


# 15. islower() - Returns True if all characters in the string are lower case
""" The islower() method returns True if all the characters are in lower case
Otherwise False.
Numbers, Symbols and Spaces are not checked, only alphabet characters.
Syntax : string.islower() """
# Example-1 :
word_lower = "hello world!"
print(word_lower.islower())     # True

# Example-2 :
a = "Hello World!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())              # False
print(b.islower())              # True
print(c.islower())              # False


# 16. isnumeric() - Returns True if all the characters in the string
# are numeric, Otherwise False.
""" The isnumeric() method returns True if all the characters are numeric
(0-9), Otherwise False.
Exponents, like ² and ¾ are also considered to be numeric values.
Syntax : string.numeric() """
# Example-1 :
word_number = "565543"
print(word_number.isnumeric())          # True

# Example-2 :
x = "\u0030"        # Unicode for 0
y = "\u00B2"        # Unicode for ²
z = "10km2"
print(x.isnumeric())                    # True
print(y.isnumeric())                    # True
print(z.isnumeric())                    # False


# 17. isprintable()- Returns True if all characters in the string are printable
""" The isprintable() method returns True if all the characters are printable,
Otherwise False.
Example of non-printable character can be carriage return and line feed.
Syntax : string.isprintable() """
# Example-1 :
word_printable = "Hello! Are you #1?"
print(word_printable.isprintable())     # True

# Example-2 :
not_printable = "Hello\nAre you #1?"
print(not_printable.isprintable())      # False


# 18. isspace() - Returns True if all characters in the string are whitespaces
""" The isspace() method returns True if all the characters in a string are
whitespaces, Otherwise False.
Syntax : string.isspace() """
# Example-1 :
word_space = " "
print(word_space.isspace())             # True

# Example-2 :
no_space = " s "
print(no_space.isspace())               # False


# 19. istitle() - Returns True if the string follows the rules of a title
""" The istitle() method returns True if all words in the string start with a
upper case letter, and the rest of the word are lower case letters,
Otherwise False.
Symbols and numbers are ignored.
Syntax : string.istitle() """

# Example-1 :
title_string = "Hello, Welcome To My World!"
print(title_string.istitle())               # True

# Example-2 :
word_title = "HELLO, WELCOME TO MY WORLD"
word_title1 = "Hello"
word_title2 = "22 Names"
word_title3 = "This Is %'!?"
print(word_title.istitle())                 # False
print(word_title1.istitle())                # True
print(word_title2.istitle())                # True
print(word_title3.istitle())                # True


# 20. isupper() - Returns True if all characters in the string are uppercase
""" The isupper() method returns True if all the characters are in upper case,
Othewise False.
Numbers, Symbols & Spaces are not checked, only alphabet characters.
Syntax : string.isupper() """
# Example-1 :
word_upper = "HELLO, WELCOME TO MY WORLD!"
print(word_upper.isupper())                 # True

# Example-2 :
not_upper = "Hello World!"
with_number = "hello 123"
word_upper1 = "MY NAME IS PETER"
print(not_upper.isupper())                  # False
print(with_number.isupper())                # False
print(word_upper1.isupper())                # True


# 21. join() - Joins the elements of an iterable to the end of the string
""" The join() method takes all items in an iterable and joins them into
one string.
A string must be specified as the separator.
Syntax : string.join(iterable)
iterable - Required. Any iterable object where all the returned values
 are strings."""
#  Example-1 :
myTuple = ("John", "Peter", "Vicky")
print('#'.join(myTuple))                # John#Peter#Vicky

# Example-2 :
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
print(mySeparator.join(myDict))         # nameTESTcountry


# 22. ljust() - Returns a left justified version of the string
""" The ljust() method will left align the string, using a specified
character (space is default) as the fill character.
Syntax : string.ljust(length, character)
1. length - Required. The length of the returned string.
2. Optional - A character to fill the missing space (to the right of the
string). Default is ' ' (space). """
# Example-1 :
left_align = "banana"
print(left_align.ljust(20), "is my favourite fruit.")
# banana               is my favourite fruit.

# Example-2 :
word_lalign = "banana"
print(word_lalign.ljust(20, "O"))       # bananaOOOOOOOOOOOOOO

# Example-3 :
word = "banana"
print(word.ljust(20, 'so'))
# Output :
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-7\tempCodeRunnerFile.py",
# line 3, in <module>
#     print(word.ljust(20, 'so'))
# TypeError: The fill character must be exactly one character long


# 23. lower() - Converts a string into lower case
""" The lower() method returns a string where all characters are lowercase.
Symbols and Numbers are ignored.
Syntax : string.lower() """
# Example :
txt = "Hello my FRIENDS!"
print(txt.lower())                  # hello my friends!


# 24. replace() - Returns a string where a specified value is replaced with a
# specified value.
""" The replace() method replaces a specified phrase with another specified
phrase.
Note : All occurrences of the specified phrase will be replaced, if nothing
else is specified.
Syntax : string.replace(oldValue, newValue, count)
1. oldValue - Required. The string to search for.
2. newValue - Required. The string to replace the old value with.
3. count - Optional. A number specifying how many occurrences of the old value
you want to replace. Default is all occurrences. """
# Example-1 :
word_replace = "I like bananas"
print(word_replace.replace("bananas", "apples"))        # I like apples

# Example-2 :
word_replace1 = "one one was a race horse, two two was one too."
print(word_replace1.replace("one", "three", 2))
# three three was a race horse, two two was one too.


# 25. split() - Splits the string at the specified separator, and
# returns a list.
""" The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.
Note : When maxsplit is specified, the list will contain the specified number
of elements plus one.
Syntax : string.split(separator, maxsplit)
1. separator - Optional. Specifies the separator to use when splitting the
string. By default any whitespace is a separator.
2. maxsplit - Optional. Specifies how many splits to do. Default value is -1,
which is 'all occurrences'. """
# Example-1 :
split_words = "Welcome to the jungle"
print(split_words.split())          # ['Welcome', 'to', 'the', 'jungle']

# Example-2 :
split_words1 = "apple#banana#cherry#orange"
print(split_words1.split("#"))      # ['apple', 'banana', 'cherry', 'orange']


# 26. startswith() - Returns True if the string starts with the specified value
""" The startswith() method returns True if the string starts with the
specified value, Otherwise False.
Syntax : string.startswith(value, start, end)
1. value - Required. The value to check if the string starts with.
2. start - Optional. An integer specifying at which position to start
 the search.
3. end - Optional. An integer specifying at which position to end the search.
"""
# Example-1 :
string_startswith = "Hello, Welcome to my world."
print(string_startswith.startswith("Hello"))            # True

# Example-2 :
string_starts = "Hello, Welcome to my world."
print(string_starts.startswith("Wel", 7, 20))           # True


# 27. strip() - Returns a trimmed version of the string
""" The strip() method removes any leading (spaces at the beginning) and
trailing (spaces at the end) characters (space is the default leading
character to remove).
Syntax : string.strip(characters)
characters - Optional. A set of characters to remove as leading/trailing
characters."""
# Example-1 :
strip_word = "  banana  "
print("Of all fruits", strip_word.strip(), "is my favorite.")
# Of all fruits banana is my favorite.

# Example-2 :
strip_words = ",,,,,rrttgg.....banana....rrr"
print(strip_words.strip(",.grt"))           # banana


# 28. swapcase() - Swaps cases, lowercases becomes upper case and vice versa
""" The swapcase() method returns a string where all the upper case letters are
lower case and vice versa.
Syntax : string.swapcase() """
# Example :
string_swapcase = "Hello, My Name Is Peter."
print(string_swapcase.swapcase())           # hELLO, mY nAME iS pETER.


# 29. title() - Converts the first character of each word to upper case
""" The title() method returns a string where the first character in every
word is uppercase. Like a header, or title.
If the word contains a number or a symbol, the first letter after that will be
converted to upper case.
Syntax : string.title() """
# Example-1 :
title_string = "Welcome to my world!"
print(title_string.title())                 # Welcome To My World!

# Example-2 :
title_string1 = "hello b2b2b2 and 3g3g3g"
print(title_string1.title())                # Hello B2B2B2 And 3G3G3G


# 30. upper() - Converts a string into upper case
""" The upper() method returns a string where all characters are in upper case.
Symbols and Numbers are ignored.
Syntax : string.upper() """
# Example :
uppercase_string = "Hello, My friends!"
print(uppercase_string.upper())             # HELLO, MY FRIENDS!


# 31. rfind() - Searches the string for a specified value and returns the last
# position of where it was found.
""" The rfind() method finds the last occurrence of the specified value.
The rfind() method returns -1 if the value is not found.
The rfind() method is almost the same as the rindex() method.
Syntax : string.rfind(value, start, end)
1. value - Required. The value to search for.
2. start - Optional. Where to start the search. Default is 0.
3. end - Optional. Where to end the search. Default is to the end of the
 string. """
# Example-1 :
rfind_string = "Mi casa, su casa."
print(rfind_string.rfind('casa'))                   # 12

# Example-2 :
rfind_string1 = "Hello, Welcome to my world."
print(rfind_string1.rfind('e', 5, 10))              # 8

# Example-3 :
rfind_string2 = "Hello, Welcome to my wrold."
print(rfind_string2.rfind('q'))                     # -1
print(rfind_string2.rindex('q'))
# Traceback (most recent call last):
#   File "c:\Users\HP\Desktop\PythonFundamentals\Day-7\tempCodeRunnerFile.py",
# line 4, in <module>
#     print(rfind_string2.rindex('q'))
# ValueError: substring not found


# 32. rindex() - Searches the string for a specified value and returns the last
# position of where it was found.
""" The rindex() method finds the last occurrences of the specified value.
The rindex() method raises an exception if the value is not found.
The rindex() method is almost the same as the rfind() method.
Syntax : string.rindex(value, start, end)
1. value - Required. The value to search for.
2. start - Optional. Where to start the search. Default is 0.
3. end - Optional. Where to end the search. Default is to the end of the string
"""
# Example-1 :
rindex_string = "Mi casa, su casa."
print(rindex_string.rindex('casa'))                 # 12

# Example-2 :
rindex_string1 = "Hello, Welcome to my world!"
print(rindex_string1.rindex('e', 5, 10))            # 8


# 33. rjust() - Returns a right justified version of the string
""" The rjust() method will right align the string, using a specified character
(space is default) as the fill character.
Syntax : string.rjust(length, character)
1. length - Required. The length of the returned string.
2. character - Optional. A character to fill the missing space (to the left of
the string). Default is ' ' (space). """
# Example :
rjust_string = "banana"
print(rjust_string.rjust(20), "is my favorite fruit.")
#               banana is my favorite fruit.


# 34. rsplit() - Splits the string at the specified separator, and
# returns a list
""" The rsplit() method splits a string into a list, starting from the right.
If no 'max' is specified, this method will return the same as the
split() method.
Note : When maxsplit is specified, the list will contain the specified number
of elements plus one.
Syntax : string.rsplit(separator, maxsplit)
1. separator - Optional. Specifies the separator to use when splitting the
 string. By default any whitespace is a separator.
2. maxsplit - Optional. Specifies how many splits to do. Default value is -1,
 which is 'all occurrences'. """
#  Example :
right_split = "apple,banana,cherry"
# Setting the maxsplit parameter to 1, will return a list with 2 elements!
print(right_split.rsplit(',', 1))           # ['apple,banana', 'cherry']
# Note : The result has only 2 elements "apple,banana" is the first element,
# and "cherry" is the last.


# 35. rstrip() - Returns a right trim version of the string
""" The rstrip() method removes any trailing characters (characters at the end
of a string), space is the default trailing character to remove.
Syntax : string.rstrip(characters)
characters - Optional. A set of characters to remove as trailing characters."""
# Example :
rstrip_string = "   banana  "
print("Of all fruits", rstrip_string.rstrip(), "is my favorite.")
# Of all fruits    banana is my favorite.


# 36. splitlines() - Splits the string at line breaks and returns a list
""" The splitlines() method splits a string into a list. The splitting is done
at line breaks.
Syntax : string.splilines(keeplinebreaks) """
# Example :
linebreak_string = "Thank you for the music\nWelcome to the jungle"
print(linebreak_string.splitlines(True))
# ['Thank you for the music\n', 'Welcome to the jungle']


# 37. translate() - Returns a translated string
""" The translate() method returns a string where some specified characters are
replaced with the character described in a dictionary, or in a mapping table.
Use the maketrans() method to create a mapping table.
If a character is not specified in the dictionary/table, the character will not
be replaced.
If you use a dictionary, you must use ascii codes instead of characters.
Syntax : string.translate(table)
table - Required. Either a dictionary, or a mapping table describing how to
 perform the replace. """
# Example :
string_txt = "Hello Sam!"
myTable = string_txt.maketrans('S', 'P')
print(string_txt.translate(myTable))            # Hello Pam!


# 38. zfill() - Fills the string with a specified number of 0 values
# at the beginning
""" The zfill() method adds zero(s) at the beginning of the string, untill
it reaches the specified length.
If the value of the len parameter is less than the length of the string, no
filling is done.
Syntax : string.zfill(len)
len - Required. A number specifying the position of the element you want
to remove. """
# Example-1 :
num_string = "50"
print(num_string.zfill(10))             # 0000000050
