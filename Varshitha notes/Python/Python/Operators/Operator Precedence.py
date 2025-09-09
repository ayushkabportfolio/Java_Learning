"""Operator Precedence
Operator precedence describes the order in which operations are performed"""

#example
Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3)) #0

#Example
Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:

print(100 + 5 * 3)      #115

'''The precedence order is described in the table below, starting with the highest precedence at the top:'''

()	Parentheses	
**	Exponentiation
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT
*  /  //  %	Multiplication, division, floor division, and modulus
+  -	Addition and subtraction
<<  >>	Bitwise left and right shifts
&	Bitwise AND
^	Bitwise XOR
|	Bitwise OR
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
not	Logical NOT
and	AND
or	OR