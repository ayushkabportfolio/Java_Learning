'''Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers'''

#
&
'''AND	Sets each bit to 1 if both bits are 1	
x & y'''

x = 3              0011
y = 2              0010
print(x & y)       0010  #2

#
|
'''OR	Sets each bit to 1 if one of two bits is 1	
x | y '''

x = 3              0011
y = 2              0010
print(x | y)       0011 #3

#
^
'''XOR	Sets each bit to 1 if only one of two bits is 1	
x ^ y'''

x = 3              0011
y = 2              0010
print(x ^ y)       0001 #1

#
~
'''NOT	Inverts all the bits	
~x'''

x = 3              0011
print(~x)          #-3
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).16bits

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""

#
<<
'''Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	
x << 2'''

##move 2 positions
x = 3               #0011
print(x << 2)       #12    1100

##move 3 positions
x = 4               #0100
print(x << 3)       #32      100000

#
>>
'''Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, 
and let the rightmost bits fall off	
x >> 2'''

#move by 2 positions
x = 3               #0011
print(x >> 2)       #0  0000