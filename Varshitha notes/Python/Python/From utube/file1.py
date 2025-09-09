Note:
1.the input functions return value as string


name = input("what is your name? ")
print("hello " + name)
birth = input("what is your birth year? ")
# bith_year= int(birth)
age = 2024 - int(birth)
print(age)
if name == "varshi" :
    print("hey")
elif age == 25:
    print("hello")
else:
    print("wrng person")

====================
##taking inputs and printing
name= input("what is your name" )
print("hi " + name)
color= input("what is your fav color ")
print("nice color")
print(name + ' likes ' + color)
==================
##take whole num and convert to float
num1 = input("provide one whole num ")
print(type(num1))
print(float(num1))
========================
##pound to kg conversion
num1 = input("provide ponds ")
print(type(num1))
num2 = float(num1) * 0.45
print(num2)
=======================
##vlaue from the index

name = "varshi"
print(name[1:-1])    #it is reading ulta means (j -1: 1)
# therefore it will skip 'i' from end and prints
#arsh
=========================
##Formated string

name1 = "varshi"
name2 = "varshitha"
msg = f'{name1} [{name2}] is same names'
print(msg)
#varshi [varshitha] is same names




BUILD A SIMPLE CALCULATOR:
-------------------------
first_num = input("first num")
print(first_num)
second_num = input("second num")
print(second_num)
sum = float(first_num) + float(second_num)
# print(sum)        #directly print the value
# print("sum" + sum)        #error
print("sum" + str(sum))     #converts into string and print output

**IN ABOVE code using float instead int,becz whn user gives decimal values then there will be error
** float can take int as well float values

**in above script
print("sum" + sum)
##this will give error as print dont support "TypeError: can only concatenate str (not "float") to str"

so to make sum as string
print("sum") + str(sum))

** or we can direclty specify the input to datatype

first_num = float(input("first num"))
print(first_num)
second_num = float(input("second num"))
print(second_num)
sum = first_num + second_num
# print(sum)        #directly print the value
# print("sum" + sum)        #error
print("sum: " + str(sum))

-------Strings---------

a = "hello"
print(a)
#hello

a = "Hello"
print(a.upper()) #HELLO

a = "HELLO"
print(a.lower())#hello

**here it will print the index of tht word whr it starting--
a = "hi whr r u"
print(a.find("r"))  # 5 -- prints the index  of tht particular character

a = "hi whr r u"
print(a.find("whr"))  #5  - prints the index of the 'w' from whr it is starting

a = "hi whr r u"
print(a.replace("r", 'are')) #hi whare are u

a = "hi whr r u"
print(a.replace("are", 'r'))
 #hi whr r u
**In above example if we try to replace non existing charcter,then python dont give any error instead it will
    print new string and consume memory


a = "hi whr r u"
print("hi" in a) #True

a = "hi whr r u"
print("Hi" in a)  #False  --becz in the "a" varibale there is not word with Hi ,as python is case sensitive

a = "hi whr r u"
print(a.title())    #Hi Whr R U

print("hi " * 10)
#hi hi hi hi hi hi hi hi hi hi

------Arithmetic ----

+, - ,* , / ,// , %, **

argumented assignment

x =10
x += 3
print(x)

---operator precednece--

brackets
exponential
multi and divison
add and sub

x = 10 + 3 * 2 ** 2
print(x)  #22

x = (10 + 3) * 2 ** 2
print(x) #52

---math fuctions----

1.round - prints the round of the decimal num ,
if decimal is >= 0.5 ouput will the whole num which is along with decimal
x = 2.5 or 2.3
print(round(x))  #2

if decimal is <= 0.6 ouput will the whole num with +1 increment
x = 2.9  or 2.6
print(round(x)) #3

x = 2.6
print(round(x))

2.abs - absolute value - prints the positive value evn though it is negative

x = -2.3
print(abs(x))  #2.3

print(abs(-2))  #2

----math module---

import math

print(math.ceil(2.9))  ##3
print(math.floor(2.9))  ##2


QN1.Primitive type in python
ANs: String,Numbers(float,integer,complex) and boolean

QN2.
for number in range(3): #range strt with 0 1 2
    print("attempt", number +1,(number + 1) * "." )

#modified
for number in range(1, 4):      #range start with 1 2 3
    print("attempt", number,(number) * "." )

for number in range(1, 6, 2):      #range start with 1 2 3 and here 2 means,it will skip 2 numbers and print till the end num
    print("attempt", number,(number) * "." )


i = 6
while i >= 1:
    print("*" * i)
    i -=1
print("dome")

Qn3:if successfull is true break the for loop and if it is false ,print attempts and show failed

successfull =False / True
for number in range(3):
    print("attempt",number +1)
    if successfull:
        print("great")
        break
else:
    print("ur 2 attempts done and failed")

Qn4:print coordinates

for x in range(5):
    for y in range(2):
        print(f'({x} , {y})')

Qn5:user shld provide input continuosly until condition gets failed

command =""
while command.lower() != "quit":
    command = input(">>")
    print("Echo:" , command)

or  how to breake infinite loop


while True:
    command = input(">>>")
    print("ECHO:" ,command)
    if command.lower() == "quit":
        break

Qn6:print evn number

i = 2
count = 0
while i < 10:
    print(i)
    i += 2
    count += 1
print(f"we hv {count} even numbers")

#with break
i = 2
count = 0
while range(1, 10):
    print(i)
    i += 2
    count +=1
    if i >= 10:
        break
print(f"we hv {count} even numbers")

#with for loop
count =0
for i in range(1, 10):
    if i % 2 == 0:
        count +=1
        print(i)
print(f"we hv {count} even numbers")


functions has 2 types,

1.perform the actions
2calculate the code and return values


qn7:how to increment value by n value
def increment (number, by):
    return number + by

print(increment(2, 1))

#how to make default parameter value /optional paramter
def increment (number, by = 1):     #by =1 is optnal parameter
    return number + by

print(increment(2))

#if we r using optional paramter and req paramter then req parameter will cm first and at last optnal paramter
def increment (number, another,by = 1):
    return number + by +another

print(increment(2,1))

QN8:Multiply the given numbers using functn and for loop

def multiply(*numbers):  #astrick number will take n no. of values
    total = 1           #initially asisigning value to 1
    for number in numbers:      #numbers are looping
        total *=number
    return total                # return the total value after the completion of loop
#retrun shld cm under in the same line of for ,or else it will break the code the at the 1st argumented value itslef
print(multiply(2,2,3,4))        #48

QN9:**args,how to use it
when use **args,we can use n no. of keyvalue arguments or keyword argumnets and returns dictionary

def save_user(**user):
    print(user)

save_user(id=1,name="varshi",age=24)

#how can we access the value
def save_user(**user):
    print(user["age"])

save_user(id=1,name="varshi",age=24)

QN10: check num ber is divisible by 3 and 5 and both or if not print same value

def fizzbuzz(input_value):
    if (input_value %3 == 0) and (input_value %5 == 0):
        return "fixxbuzz"
    if input_value %3 == 0:
        return "Fizz"
    if input_value %5 == 0:
        return "Buzz"
    return input_value

print(fizzbuzz(55))