'''Python Logical Operators
Logical operators are used to combine conditional statements and result in boolean'''

#
and - both the conditions shld satisfy
'''Returns True if both statements are true
x < 5 and  x < 10	'''

x=2
print(x < 5 and  x < 10)        #True

#
or  - any one condition is satisfied ,then True
'''Returns True if one of the statements is true	
x < 5 or x < 1	'''

x = 3
print(x < 5 or x < 1)       #True

#
not	- reverse the output
'''Reverse the result, returns False if the result is true	
not(x < 5 and x < 10)'''

x=2
print(not(x < 5 and  x < 10))        #False
