##----Modify strings---

#Uppercase
x="hello"
print(x.upper())            #HELLO
print(x.isupper())          #False      #checks if the string is Upper case
print(x.islower())          #True       #checks if the string is lower case
#lower case
x="HELO"
print(x.lower())            #helo
print(x.islower())          #False      #checks if the string is lower case
print(x.isupper())          #True       #checks if the string is Upper case
#Remove space
x=" hello "
print(x.strip())            #hello
print(x.lstrip())           #hello       #removes the left space
print(x.rstrip())           # hello      #removes the right space

#replace string
x = "hello"
print(x.replace("h", "H"))   #Hello

''' for string only replace works for others it wont
x=['A','B']
x=tuple('A','B')
x=dict(name='varshi',age=''25)
etc  '''

#Split string  - splits the strings into 2 sets

x = "hello world"
print(x.split())             #['hello', 'world']         ##by default splits from the left
print(x.rsplit())            #['hello', 'world']         ##splits from right
x= """Hello
world
how 
r
u"""
print(x.splitlines())           #['Hello', 'world', 'how ', 'r', 'u']

x = "apple,banana,cherry"
print(x.split(","))  # Output: ['apple', 'banana', 'cherry']

x = "apple|banana|cherry"
print(x.split("|"))  # Output: ['apple', 'banana', 'cherry']

x = "apple banana cherry"
print(x.split(" "))  # Output: ['apple', 'banana', 'cherry']

x = "apple,,banana,,cherry"
print(x.split(","))  # Output: ['apple', '', 'banana', '', 'cherry']

x = "apple,,banana,,cherry"
print(x.split(",",2))    #['apple', '', 'banana,,cherry']

x = "apple banana cherry date"      #here it splits from the left end in the count of 210
print(x.split(" ", 2))      3['apple', 'banana', 'cherry date']

x = "apple banana cherry date"      #here it splits from the right end in the count of 210
print(x.rsplit(" ", 2))  # Output: ['apple banana', 'cherry', 'date']

x = "apple banana cherry date color"      #here it splits from the right end in the count of 210
print(x.rsplit(" ", 2))     # Output: ['apple banana cherry', 'date', 'color']

x = "apple banana cherry date color"      #here it splits from the right end in the count of 10
print(x.rsplit(" ", 1))        #['apple banana cherry date', 'color']

#------------------------------------------------------------------#

##-----String concatention---------------#
''' joining two or more strings, lists, or other sequences together into one continuous sequence
--- first operations should be defined to one varibale and then tht variable shold be printed
---concat can be done for the str+str,int+int not for the str+int'''

#by using +
x = "hello"
y = "world"
z = x + y
print(z)                #helloworld
a = x + " " + y
print(a)
print(x + " " + y)                #hello world


#by using join() - joins the strings in the list

words = ["Hello", "World"]
result = " ".join(words)
print(result)  # Output: "Hello World"

#list concatenation
x = [1,2,3]
y = [3,4,5]
z = x + y               #merges the 2 list
print(z)                #[1, 2, 3, 3, 4, 5]

#extend() method   -- for list it will work
x = [1,2,3]
y = [3,4,5]
z = x.extend(y)         #for the x list add y list values and extend it and print 1st list's variable
print(x)                #[1, 2, 3, 3, 4, 5]

#Tuple concatenation
x = (1,2,3)
y = (3,4,5)
z = x + y               #merges the 2 tuples
print(z)                #(1, 2, 3, 3, 4, 5)

x = ('1','1','2')
x = (1,2,3)
y = (3,4,5)
# z = x.extend(y)           #for tuple it wont work
z = "".join(x)
print(x)

x = ('1','1','2')
y = (3,4,5)
z = "".join(x)              # for list of strings only it will join,not for tuple of the string
print(x)                    #('1', '1', '2')




