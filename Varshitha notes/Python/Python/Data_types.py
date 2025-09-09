#Data Types - built-in -
''' text format: string[str]
    Numeric : integer,float,complex,
    sequence : list,tuple,range
    mapping : Dict
    set : set,frozenset
    boolean : bool
    binary : bytes,bytearray,memory view
    none : NoneType'''

# how to know datatype of the variables

#Str
x = "helo"
print(type(x))      #<class 'str'
print(x)            #helo
#integer
x = 3
print(type(x))       #<class 'int'>
print(x)             #3
#float
x = 35.34
print(type(x))      #<class 'float'>
print(x)            #35.34
#complex
x = 1+1j
print(type(x))      #<class 'complex'>
print(x)            #(1+1j)
#List
x = ["a", "b", "c"]
print(type(x))      ##<class 'list'>
print(x)            #["a", "b", "c"]    #ordered and changeable
#Tuple
x = ('a', 'b', 'c')
print(type(x))      #<class 'tuple'>
print(x)            #('a', 'b', 'c')    #ordered and unchangeable
#range
x = range(6)
print(type(x))      #<class 'range'>
print(x)            #range(0,6)
#dict
x = {'name':'varshi','age':25}
print(type(x))      #<class 'dict'>
print(x['name'],x['age'])       #varshi 25
#set
x = {'q','2','5',"7"}
print(type(x))      #<class 'set'>
print(x)            #{'q','2','5',"7"}      #unordered and unindexed
#frozenset
x = frozenset({'q','2','5',"7"})
print(type(x))      #<class 'frozenset'>
y = frozenset({'z','xx','c',"7"})
print(y)        #frozenset({'z','xx','c',"7"})
z = x | y
print(z)        #frozenset({'2', '5', 'q', 'z', 'xx', '7', 'c'})    #merge the sets, remove the common value and prints one time
z = x & y
print(z)        #frozenset({'7'})   #picks only common value

'''what is the difference betweeb set and frozenset?
x = {"a","b","c"} #set    #unordered and unindexed    #mutable    #duplicates not allowed   #can be changed   #can be added   #can be removed  #can be merged  #can be updated    #can be iterated    #can be sliced
y = frozenset({"a","b","c"})  #frozenset    #unordered and unindexed    #immutable    #duplicates not allowed   #cannot be changed   #cannot be added   #cannot be removed  #can be merged  #cannot be updated    #can be iterated    #cannot be sliced'''


#boolean

print(10>9)     #True
print(10<9)     #False

x = True
y = False
print(type(x))      #<class 'bool'>
print(type(y))      #<class 'bool'>
print(x)            #True
#byte
'''---byte object in python
----Immutable sequnce of integer range of 0<+x<256
----Each string encoded as single byte
--Adv - Used when dealing withe binary data,such as reading or wirting from binary files,ntwrk protocols or handling raw data
---ENcoding string into diff char sets or decoding them back'''

x = b"Hello"      #treated as sequence of bytes not sequence of characters
print(type(x))          #<class 'bytes'>
print(x)                #b'Hello'
print(x[0])             # 72 (ASCII value for 'H')
print(x[1])             #101 (ASCII value for 'e')
##
#bytearray
'''---mutuable sequence of bytes 0<=x<256, REPLACE THE BYTES WITH CHARACTER THRU ASCCI CODE'''
x = bytearray(5)   ##for number
'''----initialising bytearray of length 5 filled with 'null bytes' ('\x00')'''
print(type(x))      #<class 'bytearray'>
print(x)            #bytearray(b'\x00\x00\x00\x00\x00')

x[0] = 65
print(x)           # bytearray(b'A\x00\x00\x00\x00)
'''---here we are replacing \x00 to A '''
x[1] = 65
print(x)            #bytearray(b'AA\x00\x00\x00')
#memeoryview
'''---view or manipulate the underlying data of objects like bytes or bytearray efficiently & without copying
----Adv -> instead creating the new object with its own memeory space,'memory view' shares the memeory fo the original object(like bytes) 
---------->and also helps in dealing larger data structures by allowing direct access and manipulation of data'''
''' this supports byte,bytearray,array
---- String are not directly compactiable'''
x = memoryview(bytes(5))        ##memeory of the bytes which is for number s
print(type(x))              #<class 'memoryview'>
print(x)                    #<memory at 0x0000018175764F40>
# y = memoryview(bytes(AB))       ##error - NameError: name 'AB' is not defined
# print(y)

x=[65,66,67,68,69,70]
y=memoryview(bytes(x))
print(y[0])         #65
print(y)            #<memory at 0x0000021712B784C0>

#None
'''builtin data type -represents the absence of the value
-- indidcates that a variable or an expression does not have or points to no objects
---None is a singleton object - one instance of object
--- Boolen evaluation - none evaluates to 'False' '''
x = None
print(type(x))              #<class 'NoneType'>

#wertyu


#Bitwise - 8421
# 2      - 0010
#10      - 1010

'''result1 = divide(10, 2): The bitwise OR of 10 (which is 1010 in binary) and 2 (which is 0010 in binary) results in 1010 (binary), which is 10 in decimal.
result2 = divide(10, 0): Since b is 0, the function returns None.'''

##setting the specific data types
x = str('Heloworld')
print(x)            #Heloworld
x= int(3.6)
print(x)            #3
x=float(66.8)
print(x)            #66.8
x = complex(33.5)
print(x)            #(33.5+0j)
x= list(("a", "b", "c"))
print(x)            #['a', 'b', 'c']
x= tuple(("a", "b", "c"))
print(x)            #('a', 'b', 'c')
x =range(5)
print(x)            #range(0,5)
x =dict(name='varshi', age=25)
print(x)            #{'name':'varshi','age'=25}
x = set(("a", "b", "c"))
print(x)            #{'a', 'b', 'c'}
x= frozenset(("a", "b", "c"))
print(x)            #frozenset({'a', 'b', 'c'})
x =bool(5)
y=bool(0)
z=bool(10>9)
print(x)            #True
print(y)            #False
print(z)            #True
x=bytes(5)
y=bytes(A)
z=bytes(6)
print(x)              #b'\x00\x00\x00\x00\x00'
# print(y)            #errorname 'A' is not defined
print(z)              #b'\x00\x00\x00\x00\x00\x00'
x=bytearray(5)
print(x)              #bytearray(b'\x00\x00\x00\x00\x00')
x=memoryview(bytes(5))
print(x)              #<memory at 0x000001ECF70C8580>
x=None
print(x)              #None

#For frozenset,range,bytearray =the output it will print with datatypes names only
#for bytes - the output print with b'
