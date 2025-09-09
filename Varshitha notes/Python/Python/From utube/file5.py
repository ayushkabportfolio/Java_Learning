-emoji converter----
RED = "\033[31m"
RESET = "\033[0m"
msg = input(">> ")
word = msg.split(" ")
emoji = {
    ":)" : "😊",
    ":(" : "😔",
    "I"  : "❤You"
}
output = ''
for x in word:
    output += emoji.get(x,x) + ' '    ## it will check for the x value and if x value is
print(f'{RED}{output}{RESET}')          #not there then it will print x value only as default
##in above output myself only printed with color code

----Functions---
# repeatedly we can use piece code by calling its funct name
#when ppl r calling functions ,values should be written in () paranthesis
def greet_users():
    print("hello")
    print("hw r u")

print(input("say hi"))
greet_users()

----Parameters---

#difference between paramter and argument
paramter - it is the place where it holds the key
Argument - where it holds the informarion of the parameter

as a local variables we are using

def greet_users(name):      #name is parameter
    print(f"hello {name}")      # passing value of the name when func is called
    print("hw r u")

print(input("say hi"))
greet_users("varshi")       #varshi is argument

# here we can ass one paramter in to the multi functn names

def greet_users(name):      #name is parameter
    print(f"hello {name}")      # passing value of the name when func is called
    print("hw r u")

print(input("say hi"))
greet_users("varshi")
greet_users("varshitha")

# we can pass multi paramaters and same num of argument shld be passed

def greet_users(First_name,sec_name):      #name is parameter
    print(f"hello {First_name} {sec_name}")      # passing value of the name when func is called
    print("hw r u")
# print(input("say hi"))
greet_users("varshi", "gowda")      #here these are positional arguments
                                                    #1st arugument is for 1st paramter and so on

---------keyword Argument-----

#keyword argument is used to improve code readability when Numeric is begin called as aruguments
#here we can define the argument with the paramter or keyword so that where we can use value for
# paramter when calling inside the fucnt

def greet_users(First_name,sec_name):      #name is parameter
    print(f"hello {First_name} {sec_name}")      # passing value of the name when func is called
    print("hw r u")
# print(input("say hi"))
greet_users(sec_name= "gowda",First_name="varshi")      #where evr we want we can assign value to paramter

#Here if we are using both positional and keyword argument
# 1st we hv to use positional only then keyword we hv use as it will asign value to 1st paramter and then it can do
# keyword argument

def greet_users(First_name,sec_name,Third_name):      #name is parameter
    print(f"hello {First_name} {sec_name} {Third_name}")      # passing value of the name when func is called
    print("hw r u")
# print(input("say hi"))
greet_users("varshi",Third_name="U R",sec_name= "gowda")

======Return statement=======
Returns the value of the function where outside of the fuctn

def square(num):
    b = num * num
    return b
print(square(num=2))

def square(num):
    return num * num

print(square(3))

##if we dont call return in fuctn,python byitself print none output

def square(num):
    print(num * num)   #4

print(square(num=2))        #for this it returns none,first it will send 2 to insisde the funtn and pront value 4

========Creating reusable functions=========

def emoji_func(message):
    words = message.split(" ")
    emojis = {
    ":)" : "😊",
    ":(" : "😔"
    }
    output = ""
    for x in words:
        output += emojis.get(x, x) + " "
    return output

message = input("msg: ")
print(emoji_func(message))


========handle exception=======
we have try and except methd

try:
    age = int(input("age: "))
    income = int(input("income: "))
    divi = income / age
    print(divi)
except ValueError:
    print("invalid value")
except ZeroDivisionError:
    print("0 cant be excepted")
