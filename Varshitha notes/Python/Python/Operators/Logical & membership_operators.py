'''Python Identity Operators
Identity operators are used to compare the objects,
not if they are equal, but if they are actually the same object, with the same memory location'''

#
is
'''Returns True if both variables are the same object	
x is y'''

x ="your r very beauitful"
y = "your r very beauitful"
print(x is y)       #True

x ="your are very beauitful"
y = "your r very beauitful"
print(x is y)       #False

#is not
'''Returns True if both variables are not the same object	
x is not y'''

x ="your are very beauitful"
y = "your r very beauitful"
print(x is not y)       #True

x ="your r very beauitful"
y = "your r very beauitful"
print(x is not y)       #false

'''
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object'''

#
in
'''Returns True if a sequence with the specified value is present in the object	
x in y'''

y = "your r very beauitful"
print('your' in  y)         #True

y = "your r very beauitful"
print('are' in  y)          #False

#
not in
'''Returns True if a sequence with the specified value is not present in the object	
x not in y'''

y = "your r very beauitful"
print('your' not in  y)         #False

y = "your r very beauitful"
print('are' not in  y)          #True