"""Python Assignment Operators
Assignment operators are used to assign values to variables"""
import random

Here variable of assiging values and assiging value with the operator should be same

#  =
 x = 5
Assiging value to a variable

# +=
x += 3 ==> x = x + 3

x = 3
x += 4
print(x)        #7

# -=
x -= 3	==> x = x - 3

x = 10
x -= 3
print(x)        #7

# *=	x
*= 3   ==>	x = x * 3

x=3
x*=10
print(x)        #3

# /=	x
/= 3   ==>	x = x / 3

x=25
x /= 5
print(x)        #5.0

# %=
x %= 3 ==>	x = x % 3

x = 45
x %= 3
print(x)        #0

# //=	x
//= 3 ==>	x = x // 3

x = 7
x //= -3
print(x)        #-3

# **=
x **= 3	 ==> x = x ** 3

x = 2
x **= 3
print(x)        #8


With Bitwise operators - works with binaries 0 and 1

# &=
'''AND - Returns 1 if both bits are 1, otherwise 0 
example : 
x = 3         0011
y = 2         0010
z = x & y     0010
  print (z)  ans:2 '''

x &= 3	==> x = x & 3
x =3
x &=2
print(x)        #2

# |=
'''OR - Returns 1 if at least one bit is 1  [here in both values either both can be 1 and any one can be 1,then o/p is 1 ]
example : 
x = 3         0011
y = 2         0010
z = x | y     0011
  print (z)  ans:3 '''

x |= 3	==> x = x | 3

x =3
x |=2
print(x)        #3

# ^=
'''XOR - Returns 1 if exactly one bit is 1, otherwise 0 [here in both values any one can be 1 ,then o/p is 1]
example : 
x = 3         0011
y = 2         0010
z = x ^ y     0001
  print (z)  ans:1 '''

x ^= 3	x = x ^ 3

x =3
x ^=2
print(x)        #1

# ~=
'''NOT -  Inverts the bits; if using a 1-bit width, ~0 results in 1. Note that in practice, 
the bit width affects the result 
(e.g., in an 8-bit representation, ~0 would be 11111111 which is -1 in signed representation).'''

Operation: ~0

Binary: ~0000 (assuming 1-bit representation)

Result: 0001 (1, in a 1-bit context)


# >>=
'''Right shift - Shifts bits to the right
example : 
x = 3         0011
y = 2         0010
z = x >> y    0000 --> This operation shifts the bits of x = 3 to the right by y = 2 positions.              
  print (z)  ans:0 '''

x >>= 3	x = x >> 3

x =3
x >>=2
print(x)        #0

# <<=	x
'''Left shift - hifts bits to the left
example : 
x = 3         0011    0110   1100
y = 2         
z = x << y        --> This operation shifts the bits of x = 3 to the left by y = 2 positions.
  print (z)  ans: 12

x = 5         0101    01010     10100   
y = 2         
z = x << y 
print(z)  ans: 20'''

<<= 3	x = x << 3

x =3
x <<=2
print(x)        #12


# :=
'''walrus operator - Walrus Operator (:=)

The walrus operator := assigns the value on its right to the variable on its left and returns the value. This allows you to perform an assignment and immediately use the value in an expression.

First Line: print(x := 3)

The expression x := 3 assigns 3 to x.
The print() function then outputs the result of the assignment, which is 3.
Second Line: print(x)

This line prints the value of x, which was assigned as 3 in the previous line.'''

print(x := 3)	==> x = 3
print(x)




