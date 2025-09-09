--conditions---
1.if statement

its_hot = False
its_cold = False
if its_hot:
    print("summer")
    print("wear white color dresses")
elif its_cold:
    print("winter")
    print("wear dark color dress")
else:
    print("its rainy")
print("it is season")      ##this print is onot involed insidde the if condition,globally it is defined

2.price of the house is $1M
if buyer has good credit:
    they need to put down 10%
otherwise
   they need to put down 20%
print the down the payment


price_of_d_house = 10000
is_good_credit = False
if is_good_credit:
    down_payment = 0.1 * price_of_d_house
else:
    down_payment = 0.2 * price_of_d_house
print(f'down payment is ${down_payment}')


------logical operatores----

AND - both should be true

QN . if applicant has high income and good credit eligible for loan


has_high_income = True
has_good_credit = True
if has_good_credit and has_high_income:
    print("eligible for loan")

OR - any one can be true
has_high_income = True
has_good_credit = False
if has_good_credit or has_high_income:
    print("eligible for loan")

not - print bool opp to the o/p

has_criminal_Record = False
has_good_credit = True
if has_good_credit and not has_criminal_Record:
    print("eligible for loan")

---------comparison operators---------

 > < == >= <= !=
QN . if temperature is greater than 30
        its a hot day
    otherwise if its less than 30
        its a normal day
    otherwise
    its neither hot ot normal


temperature = 35
if temperature > 30:
    print("its a hot day")
elif temperature < 30:
    print("its a normal day")
else:
    print("its neither hot or cold day")

QN2. If name is less then 3 characters long
        name must be atleast 3 char
    otherwise if it is more than 50 char long
        name can be maximum char 50
    otherwise
        name looks good


name = input("what is your name")
name2 = len(name)

if name2 < 3:
    print("name must be atleast 3 char")
elif name2 > 50:
    print("name can be maximum char 50")
else:
    print("looks good")

----weight conversion ---
converting pounds and kilos

1.If other than L or l,do calculation for pounds and print

weight = int(input("weight"))
unit = input("L or K")
if unit.upper() == "L":   ##if we are using upper() then after the equals it shld be capital
    converter = weight * 0.45
    print(f'kilos {converter}')
else:
    converter = weight / 0.45
    print(f'pounds {converter}')


1.If user gives exact values then only do calculations according to input
weight = int(input("weight"))
unit = input("L or K")
if unit == "L" and "l":
    converter = weight * 0.45
    print(f'kilos {converter}')
elif unit == "k" and "K":
    converter = weight / 0.45
    print(f'pounds {converter}')
else:
    print("provide correct value")

*******While loops***********

while condition:  - executes bloack of code multiple times until unless it break the code
<<here the condition will be true ,until tht conditions get failed loop will not be break or
else loop will be infinite>>

ex1:
i = 1
while i <= 3:
    print(i)
    # i = i+ 1        3
print("done")       #done

ex2:
i = 1
while i <= 3:
    print('*' * i)
    i = i+ 1
print("done")
#*
# **
# ***
# done

ex2:
i = 6
while i >= 1:
    print('*' * i)
    i = i - 1
print("done")
# ******
# *****
# ****
# ***
# **
# *
# done

ex:3 - guess the number with three chances

secret_num = 10
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    guess = int(input("guess: "))
    guess_count += 1
    if guess == secret_num:
        print("correct num")
        break                       #if condition is crt at below 2 guess ,imediatly it will braek while loop and exxecute else
else:
    print("wrong guess")

