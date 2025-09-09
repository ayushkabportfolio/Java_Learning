 ##surronded by double or single quotes

 print("hello")
 print('hello')

x=str("hi")
print(x)
x=str('hi')
print(x)
x=str('25')
print(x)
x=str(25)
print(x)
print(type(x))

##assigning string to variable
x="hello"
print(x)
x=("hello")
print(x)

##Quotes inside the quotes
'''Valid'''
print("hello")
print('hello')
print("hey 'super'")
print('hey "super"')
print("hey book's are super")

'''invalid'''
print('hey book's are super')
print("hey "super"")
print('hey 'super'')

'''Note -  if using double quote as main quotes,inside single quote or single apostrophe shld be used'''

##multipleline strings  --> using it is used as
x = '''hey beautiful
        how r u
        can i call u'''
print(x)

x = """hey beautiful
        how r u
        can i call u"""
print(x)

x = ('''hey beautiful
        how r u
        can i call u''')
print(x)

##string are array
'''Python not hv characters datatype
    single charc is a string with length 1
    sq brackets can access the elements of the string
    --Note--: 1st charc start with '0' '''

 #   012345678910 - in this sequence elements r reading
a = "hello world"
print(a[3])     #l
print(a[5])     #space
print(a[6])     #w
print(a[10])    #d

##looping through string
#for loop
    for x in "Hello":
    print(x)        #H
                    # e
                    # l
                    # l
                    # o

'''Here in abv exmaple,x is taking one by one value from the Hello string and printing one after the other'''

##string length

    #12345   - counting numbers of characters/elements in the strin
x = "hello"
print(len(x))           #5

##check string inside the phrase or charc present in the string
        #this will give u boolean output
        #using 'in'
x = "hey super how r u"
print('hey' in x)           #True
print('r' in x)             #True
print('you' in x)           #False

'''by using if statement how to check the character'''

x = 'hey super how r u'
if 'hey' in x:
print("'hey' is there")

##Check if not - to check pharse or character is not present in the string
            #using 'not in'
            #this will give u boolean output
x = "hey super how r u"
print('hey' not in x)           #False
print('r' not in x)             #False
print('you' not in x)           #True

'''by using if statement how to check the character'''

x = 'hey super how r u'
if 'hey' not in x:
    print("'hey' is not there")             # no output
if 'you' not in x:
    print('"you" is not there')         #"you" is not there

##slicing the string
    #return part of the charc from the string
#  012345678910  - here output will be i:j-1
x="hello world"
print(x[1:3])           #el
print(x[0:7])           #hello w
 print(len(x))

'''slice from start'''
   012345678910   -  here output is [:j-1]
x="hello world"
print(x[:3])        #hel

'''slice from end'''
   012345678910   -  here output is [j:]
x="hello world"
print(x[9:])        #ld
print(x[3:])         #lo world
print(x[0:])         #hello world
print(x[:0])         #no o/p

'''Negative indexing'''
  #use -ve indexing to start the slice frm the end of the string

     10987654321  [with minus] -- [i-1:j-1]
x = "Hello world"
print(x[-1:-9])               #no o/p
print(x[-9:-1])               # llo worl
print(x[-11:])                #Hello world
print(x[:0])                  #no o/p
print(x[0:])                  #Hello world
print(x[:-4])                 #Hello w

x = "Hello world"
print(x[0:5])                   #Hello
print(x[6:11])                  #world
print(x[:-6])                   #Hello
print(x[-5:])                   #world