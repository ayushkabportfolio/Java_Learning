#Numbers

#Int,float,complex

#Integer - int
'''whole number +ve or -ve,without decimal'''

x = int(-34)
print(x)            #-34
x = int(89.00)
print(x)            #89
x = int(89)
print(x)            #89
x = int(11.2+1j)
print(x)            #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

##Float
'''Floating point +ve or -ve,with decimal'''
x = float(89.0)
print(x)                #89.0
x = float(-89.0)
print(x)                #89.0
x = float(89+0j)
print(x)                #TypeError: float() argument must be a string or a real number, not 'complex'

'''scientific numbers with 'e' which is to indicate the power of 10'''
x =float(34e2)
print(x)                    #3400.0
# x =float(e34)
# print(x)                    #NameError: name 'e34' is not defined
x =float(1e34)
print(x)                    #1e+34
x =float(-5.345e4)
print(x)                    #-53450.0

##Complex
x =complex(1+1j)
print(x)                    #(1+1j)
x =complex(-2j)
print(x)                    #(-0-2j)
x =complex(34e2)
print(x)                    #(3400+0j)
x =complex(e34)
print(x)                    #NameError: name 'e34' is not defined
x =complex(1e34)
print(x)                    #1e+34+0j
x =complex(-5.345e)
print(x)                    #SyntaxError: invalid decimal literal

''' here after 'e' what ever the value will be there it will consider as power
ex : 1e34 means  1x10 power of the 34
The notation 34e2 means 34 * 10^2
----34e2 is equivalent to 34 * 10^2, which is 34 * 100, resulting in 3400.0
----The complex function can take one argument that is a float, 
----and it creates a complex number with that float as the real part and 0.0 as the imaginary part:
complex(3400.0) results in 3400.0 + 0.0j'''

##-----RANDOM NUMBERS------##
'''to print random values within the range
---Built in functn,import and use it in the script'''

import random

print(random.randrange(1,10))       #7
print(random.randint(1,10))             #3
print(random.randbytes(10))                   #b'\xbff\xc9\xd18\x84L\x88\xf0I'
print(random.getrandbits(34))                 #16826510356


##------casting-----##
'''specifiying the data types to variables or simply print desired value by providing data types'''

x = int(89)
print(x)                    #89

x = float(89.0)
print(x)                    #89.0

x =complex(1+1j)
print(x)                    #(1+1j)

x = str('24')
print(x)                    #24

x = str("hey")
print(x)                    #hey
