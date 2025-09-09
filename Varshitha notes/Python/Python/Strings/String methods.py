'''Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. They do not change the original string.'''

1.str.capitalize()
# Capitalizes the first character of the string and makes all other characters lowercase.

txt = "hello world"
print(txt.capitalize())         #Hello world

2.str.upper()
# Converts all characters in the string to uppercase.

txt = "hello world"
print(txt.upper())              #HELLO WORLD

3.casefold() and str.lower()  -- both methods will do same
# Converts all characters in the string to lowercase.

txt = "HELLO WORLD"
print(txt.casefold())           #hello world

4.str.title()
# Capitalizes the first letter of each word in the string.

txt = 'helo world'
print(txt.title())              #Helo World

5.str.strip([chars])
# Removes leading and trailing whitespace (or characters specified in chars) from the string

txt = " hello world "
print(txt.strip())             #hello world

6.str.lstrip([chars])
# Removes leading whitespace (or characters specified in chars) from the string from left.

txt = " hello world "
print(txt.lstrip())              #hello world

7.str.rstrip([chars])
# Removes leading whitespace (or characters specified in chars) from the string from right.

txt = " hello world "
print(txt.rstrip())              # hello world

8.str.replace(old, new[, count])
# Replaces occurrences of the substring old with new. Optionally,
# you can specify the maximum number of occurrences to replace.

text = "hello world"
print(text.replace("world", "Python"))  # Output: "hello Python"

9.str.split([sep[, maxsplit]])
# Splits the string into a list of substrings based on the delimiter sep. Optionally,
# you can specify the maximum number of splits.

txt = "hello world Python"
print(txt.split())              #['hello', 'world', 'Python']

10.str.join(iterable)
# Joins elements of an iterable (e.g., a list) into a single string, with the string as the separator.

txt = ["hello", "world", "python"]
a = "".join(txt)            #"hello world Python"

11.str.find(sub[, start[, end]])
# Returns the 'lowest index' where the substring sub is found within the string. Returns -1 if not found. Optionally,
# you can specify the start and end indices.
       01234567
txt = "hello world Python"
print(txt.find("world"))        #6

        01234567890123456
text = "hello world world"
print(text.find("world"))      #6    not 12

12str.rfind(sub[, start[, end]])
# Returns the 'highest index' where the substring sub is found within the string.
# Returns -1 if not found. Optionally, you can specify the start and end indices.

text = "hello Python world "
print(text.rfind("world"))          # Output: 13

        012345678901234567
text = "hello world world"
print(text.rfind("world"))          # Output: 12


13.str.startswith(prefix[, start[, end]])
# Returns True if the string starts with the specified prefix. Optionally,
# you can specify the start and end indices.

txt = "hello world python"
print(txt.startswith("hello"))          #True
print(txt.startswith("world"))          #False

13.str.endswith(suffix[, start[, end]])
# Returns True if the string ends with the specified suffix. Optionally,
# you can specify the start and end indices.

txt = "hello world python"
print(txt.endswith("n"))                #True
print(txt.endswith("hello"))            #False
print(txt.endswith("Python"))           #False  - case sensitive - python in txt and here i finding for Python

15.str.isdigit()
# Returns True if all characters in the string are digits.

num= "12345"
print(num.isdigit())                    #True

txt = "acnc"
print(txt.isdigit())                    #False

16.str.isalpha()
# Returns True if all characters in the string are alphabetic.

txt="hello"
print(txt.isalpha())                    #True

num= "12345"
print(num.isalpha())                    #False

17.str.islower()
# Returns True if all characters in the string are lowercase.

text = "hello"
print(text.islower())  # Output: True

18.str.isupper()
# Returns True if all characters in the string are uppercase.

text = "HELLO"
print(text.isupper())  # Output: True

19.str.isspace()
# Returns True if all characters in the string are whitespace.

text = "   "
print(text.isspace())  # Output: True

20.str.zfill(width) - width required here
# Pads the string on the left with zeros to make it at least width characters long.

text = "42"
print(text.zfill(5))  # Output: "00042"

'''
in above example

zfill(5)  and output is 00042
so here ,defining the how many chaarcters should be there
if already 2 values exits and i want to make it 5 characters ,i will give zfill(5)
    so it adds extra 3 zeros to make it 5 character
'''

txt = 'hello'
print(txt.zfill(8))             #000hello

txt = 'hello'
print(txt.zfill())              # TypeError: str.zfill() takes exactly one argument (0 given)

txt = 'hello'
print(txt.zfill(3))             #hello