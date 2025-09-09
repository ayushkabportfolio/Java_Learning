#Basics py
#variables cant be used as python keywords
#if codes failes int the middle of the line,it will stuck there only ,it wont proceed
#variables - start with alphabet,underscore not with num and no space
"""myvariablename
my_varaible_name
_hello"""      #correct format
"""my varaible name
2myvariable""" # worng format

#Mutli words in variables name - C(mVV)P(MVV)s(m_v_v)
'''camel-myVariableNum
snake-my_variable_num
pascale-MyVariableNum'''

#case sensitive
#print datatype and # '' or  "" - both r same
x = 5
X = 'hi'
y = 'john'
z = "apple"
print(type(x))
print(type(y))
print(type(z))

#specifying the datatype is called casting ,ex: x=str(3)
X = int(3)
y = str(3)
z = float(3)
print(x)
print(y)
print(z)

#Many values to multiple variables : x, y ,z = 'o', 'p', 'z'
# x, y ,z = 'o', 'p', 'z'
x, y, z= ('o', 'p', 'z')
# x, y, z= ['o', 'p', 'z']    #all can be used
print(x, y ,z)
#unpack collections: x, y, z= ('o', 'p', 'z') # x, y, z= ['o', 'p', 'z']
print(x)     #value is printed frm above #Many values to multiple variables examples
print(y)
print(z)

#one value to multiple varibales: x=y=z = 'o'
x=y=z = complex(5)  #int or str or flot or complex or any datatype
print(x,y,z)
#print(x=y=z) thrw an error
print(x)
print(y)
print(z)
#x, y, z = 'a'  #throw an error
# print(x,y,z)
print(x)
print(y)
print(z)

#output variables
x = 5
y = 10
z = 'a'
# v = v     -- throw an error as not defined,either it shld be in '' or ""
print(x + y)
#print(x + y + z) -- throw an error as it contains int and  str and plus funct wont work between int and str
# print(x + y + v)  -- throw an error as it contains non defined variable ,i,e.v

#O/P multiple variables by separating by comma
x = 5
X = 'hi'
y = 'john'
z = "apple"
print(x,X,y,z)
print(x,X)  #print int str types

#global variables
x = 5
def funct():
    print(x)
funct()

##inside the fucnt the variables are considere as local variables
def fuctn():
    x = 2
    print(x)
fuctn()

##Gobal keyword  - create global variable inside the funct and call it outside the fucnt
def funct():
    global x
    x = 2
funct()
print(x)

##global variable and global keyword

#EX1:
x = "hello"   ##global variable
def funct():
    x = "hi"    # local variable
    print(x)
funct()
print(x)

#EX2:
x = "hello"   ##global variable
def funct():
    global y    #making x as global variable inside the funct
    y = "hi"
    print(y)
funct()
print(y)        ## calling from global keword
print(x)        ##calling global varibale which is defined outside the fucnt or global keywords








