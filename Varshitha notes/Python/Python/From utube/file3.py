---car game---

automate car start,stop,quit - execute code until quit is provided the user
and if more than one time start,stop,quit command is provided user should get alert
help  -- can be upper or lower
start - to start the car
stop - to stop the car
quit - to quit the car

<randamly enter value>
i dont understand ..
start
car started ..ready to go
stop
car stopped
quit
quiting the car game

--Solution
command = ""        #dummily assign variable
started = False
while True:
    command = input("> ").lower()       #converting the input to the lower and using same variable in below
    if command == "start":
        if started:
            print("already started")
        else:
            started = True
            print("car started ..ready to go")
    elif command == "stop":
        if not started:
            print("it is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print('''
        start - to start the car
        stop - to stop the car
        quit - to quit the car
            ''')
    elif command == "quit":
        print("bye bye")
        break
    else:
        print("i dont understand ..")

--tried and correct code--

value = ""
started = False
stopped = False
while True:
    value = input("> ").upper()
    if value == "HELP":
       print('''
start - to start the car
stop - to stop the car
quit - to quit the car
    ''')
    elif value == "START":
        if started:
            print("already started")
        else:
            started = True
            print("car started ..ready to go")
    elif value == "STOP":
        if stopped:
            print("already stopped")
        else:
            stopped = True
            print("car stopped")
    elif value == "QUIT":
            print("quiting the car game")
            break
    else:
        print("i dont understand ..")

----For loops-------- iterates the over items of a collection

for item in 'Python':   # here item will iterrate one character at a one time in the string
    print(item)

for a in ["a","b","c"]:
    print(a)

for a in [1,2,3]:
    print(a)

for x in range(5):  #range(i)
    print(x)

for x in range(2, 8):     #range(i,i-1)  becz it starts frm 0
    print(x)

for x in range(2,8,3):   #range(i,i-1,j)   frm 1 to i-1 it will skip accoridng to j value
    print(x)   #o/p 2 5

Qns:calculate total price in the cart of list

prices = [10,20,30]
total =0    #initially assign to 0 value,and using tht add we are doing
for x in prices:
        total += x
print(f'total : {total}')     #print shld be outside the for loop or else it will be incremneted

---Nested loops-----

Qn:priniting co ordinates

for x in range(3):
    for y in range(2):
        print(f'({x}, {y})')
o/p:\
(0, 0)       #1st it execute x and then y and print the values
(0, 1)       #next it go back to y and keeping x as 0 and y will be 1   ,now for execution if x one time,y value 0,1 it completed
(1, 0)       #now it will go back x line and increment to 1 and y will be 0 for the nxt x iteration
(1, 1)       #it go back to y and increment to 1 and now y value is completed 0,1
(2, 0)       #now it go back to x and print new intertaion and making y to 0
(2, 1)       #it go back to y and increment to 1 and now y value is completed 0,1

Guess_num = 9
gues_count = 0
guess_limit = 3
while gues_count < guess_limit:
    guess = int(input("guess: "))
    gues_count += 1
    if Guess_num == guess:
         print("correct num")
                break
    else:
        print("try again")

Qn: print
xxxxx
xx
xxxxx
xx
xx

solutn:

#without nested
values = [5,2,5,2,2]
for a in values:
    print('x' * a)
#with nested loop
values = [5,2,5,2,2]
for a in values:
    output = ""
    for b in range(a):
        output += "x"
    print(output)


below both code print same o/p
i =  1
while i <=5:
    print('x' * i)
    i+=1
print("done")

values = [1,2,3,4,5]
for a in values:
    print("x" * a)

---accessing list ---

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[0])          #apple
print(thislist[2:5])        #cherry orange  kiwi
print(thislist[:4])         #apple banana cherry orange

#changing the value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[0] = "mango"
print(thislist)
#['mango', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

Qn:write a program to find largest num in the list

num = [1,2,3,4,5,6]
max = num[0]        #assuming 1st index as greatest and then comparing and printing which is larger while in the iteration
for x in num:
    if x > max:
        max = x
print(max)


qn:write a program based on the vehical Speed

# a.Why we are using RESET in the print,becz
#  If you don't reset the formatting, the color or style may continue to be applied to all following output,
#  which can lead to confusing or undesirable results.

RED = "\033[31m"
GREEN = "\033[32m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

speed = int(input("how much speed u r going"))
if speed > 100:
    print(f" {RED} your crossing your limit{RESET}")
elif 1 < speed <= 50:
    print(f"{ORANGE}medium speed{RESET}")
else:
    print(f"{GREEN}good to go{RESET}")

Speed= ''
while True:
    speed = int(input("How much your speed"))
    if speed > 100:
        print(f" {RED} your crossing your limit{RESET}")
    elif 20 <= speed <= 50:
        print(f"{ORANGE}medium speed{RESET}")
    else:
        print(f"{GREEN}good to go{RESET}")
        break