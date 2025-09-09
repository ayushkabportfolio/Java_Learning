'''Booleans represent one of two values: True or False.
To evaluate any expression in Python'''

print(10 > 9)           #True
print(10 == 10)         #True
print(5<10)             #True
print(a < b)            #TypeError: '<' not supported between instances of 'int' and 'str

##prinitng the statment based on the considtions

a = 10
b = 15
c = 30
if a < b:
    print("True")
else:
    print("False")              #True
if c<b:
    print("True")
else:
    print("False")              #False

##Evaluate Values and Variables

#The bool() function allows you to evaluate any value, and give you True or False in return

print(bool("text"))         #True
print(bool(25))             #True
print(bool("25"))           #True
print(bool(-123))           #True
print(bool(0))              #False
print(bool())               #False


a = 'hello'
b =25
print(bool(a))              #True
print(bool(b))              #True

"""
Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.  """

bool("hello")               #True
bool(["a","b","c"])         #True
bool(("a","b","c"))         #True
bool()                      #False
bool(complex(1+1j))         #True

'''
Some Values are False
In fact, there are not many values that evaluate to False,
except empty values, such as (), [], {}, "", the number 0, and the value None.
And of course the value False evaluates to False.'''

bool()
bool([])
bool({})
bool(())
bool(0)
bool(None)
bool("")
bool(+)         # SYntax error for operator evaluation


'''One more value, or object in this case, evaluates to False,
 and that is if you have an object that is made from a class with a __len__ function that returns 0 or False'''
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))          #False


'''Functions can Return a Boolean'''
def myFunction() :
  return True
print(myFunction())         #True

def func():
    x=20
    print(x)                #20
    return True
func()                      #20
print(func())                #True

##if im not calling return here then o/p will be 'None'
def func():
    x=20
    print(x)                #20
    # return True
func()                      #20
print(func())               #None

'''Print "YES!" if the function returns True, otherwise print "NO!"'''

def func():
    return True

if func():
    print("Yes")
else:
    print("NO")                 #Yes

def func():
    return False #or 0

if func():
    print("Yes")
else:
    print("NO")                 #No


"""Python also has many built-in functions that return a boolean value, like the 'isinstance()' function,
 which can be used to determine if an object is of a certain data type"""

x = 200
y = "hello"
print(isinstance(x,int))        #True
print(isinstance(y,int))        #False
print(isinstance(y,str))        #True

