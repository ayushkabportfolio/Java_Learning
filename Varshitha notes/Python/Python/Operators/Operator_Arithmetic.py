'''Operators are used to perform operations on variables and values.'''
print(10 + 5)           #15

"""Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""

1.Python Arithmetic Operators

#+	Addition	x + y

a=10
b=5
z = a +b
print(z)        #15
print(a+b)      #15
x="hel"
y="bel"
print(x+y)      #helbel

#-	Subtraction	x - y
a=10
b=5
z = a -b
print(z)        #5
print(a-b)      #5
x="hel"
y="bel"
print(x-y)      #TypeError: unsupported operand type(s) for -: 'str' and 'str'

#*	Multiplication	x * y
a=10
b=5
z = a*b
print(z)        #50
print(a*b)      #50
x="hel"
y="bel"
print(x*y)      #TypeError: can't multiply sequence by non-int of type 'str'

#/	Division	x / y
a=10
b=5
z = a/b
print(z)        #2
print(a/b)      #2
x="hel"
y="bel"
print(x/y)      #TypeError: unsupported operand type(s) for /: 'str' and 'str'

#%	Modulus	x % y -- remainder will print
'''The modulus operator (%) returns the remainder of the division between two numbers. 
It is useful for determining if a number is divisible by another or for periodic calculations.'''

a=10
b=5
z = a%b
print(z)        #0
print(a%b)      #0
x="hel"
y="bel"
print(x%y)      #TypeError: not all arguments converted during string formatting

print(-10 % 3)  # Output: 2
print(10 % -3)  # Output: -2
    """-10 % 3 is 2, because -10 divided by 3 is -4 with a remainder of 2.
        10 % -3 is -2, because 10 divided by -3 is -4 with a remainder of -2."""

#**	Exponentiation	x ** y
'''The exponentiation operator (**) raises a number (the base) to the power of another number (the exponent).
 It is used to compute powers and roots.'''

a=10
b=5
z = a ** b
print(z)        #100000
print(a**b)      #100000
x="hel"
y="bel"
print(x**y)         #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'

print(2 ** 3)  # Output: 8

print(2 ** -3)  # Output: 0.125
        """Explanation: 2 ** -3 is equivalent to 1 / (2 ** 3), which is 0.125.""" """  1
                                                                                       --  (divided)
                                                                                      (2**3)"""

#//	Floor division	x // y  -- rounding of for the negative int and provifinh whole number for thr +ve int
"""Floor division in Python is performed using the // operator. This operator divides two numbers and 
returns the largest integer less than or equal to the result,
 effectively "flooring" the result of the division."""

a=10
b=5
z = a ** b
print(z)        #2
print(a**b)      #2
x="hel"
y="bel"
print(x**y)         #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'

#Integer Division
print(7 // 3)   # Output: 2
print(-7 // 3)  # Output: -3
        '''7 // 3 results in 2, because 7 / 3 is 2.333... and the floor value is 2.
            -7 // 3 results in -3, because -7 / 3 is -2.333... and the floor value is -3'''

#With Negative Divisor
print(7 // -3)  # Output: -3
print(-7 // -3) # Output: 2
        '''7 // -3 results in -3, because 7 / -3 is -2.333... and the floor value is -3.
            -7 // -3 results in 2, because -7 / -3 is 2.333... and the floor value is 2.'''

#With Floating-Point Numbers
print(7.5 // 2)    # Output: 3.0
print(-7.5 // 2)   # Output: -4.0
        '''7.5 // 2 results in 3.0, because 7.5 / 2 is 3.75 and the floor value is 3.0.
            -7.5 // 2 results in -4.0, because -7.5 / 2 is -3.75 and the floor value is -4.0'''
