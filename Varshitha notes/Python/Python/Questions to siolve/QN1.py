=========Adding============

1.add 2 numbers
o/p = sum of 5 and 7 is 12

num1 =5
num2 = 7
sum =num1+num2
print("sum", "of" ,num1, "and", num2, "is" ,sum)

2.Add Two Numbers with User Input
#y float used is user may provide deciaml values also

num1 = float(input("num1"))
num2 = float(input("\nnum2"))
sum = num1 + num2
print("sum", "of" ,num1, "and", num2, "is" ,sum)

3.Add Two Numbers in Python Using Function

def add(a,b):
    sum = a + b
    return sum

a =2
b=3
print(add(a,b))

4.Add Two Numbers Using operator.add() Method

import operator
a =2
b=3
sum = operator.add(a,b)
print(sum)

=======Maximum number==========

1.Find Maximum of two numbers in Python

Given two numbers, write a Python code to find the Maximum of these two numbers.
Input: a = 2, b = 4
Output: 4

num1 =2
num2 = 4
if num1 > num2:
    print(num1)
else:
    print(num2)

'or' - with defining functing and calling tht fuctn

def maxi(num1 ,num2):
    if num1 > num2:
        return num1
    else:
        return num2

# num1=2
# num2=4
# print(maxi(num1=2,num2=4))     #keyword argument also we can pass and check
# or
print(maxi(2,4))        #thru positional argument also we can check

2.Find Maximum of two numbers Using max() function

num1=2
num2=4
maximum = max(num1,num2)
print(maximum)

3.Maximum of two numbers Using Ternary Operator

num1=2
num2=4
print(num1 if num1 > num2 else num2)

4.Maximum of two numbers Using list comprehension

num1=2
num2=4
sum =[num1 if num1 > num2 else num2]
print(sum)

5.Maximum of two numbers Using sort() method
sort is only for list not for tuple

num1=2
num2=4
sum = [num1,num2]
sum.sort()
print(sum[-1])

=======Factorial===========
5 = 1x2x3x4x5 = 120

1.with for loop

num = 5
factorial =1
for i in range(1,num+1):
    factorial *= i
print(factorial)

2.functn

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = 5
print(factorial(n))

=====Python Program to Check Armstrong Number=====

Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

n = 153
while True:
    a = n//10
    b = a ** 3
    if a == 0:
        break
    print(b)


#Question
'''Write a Python function divide(a, b) that takes two integers a and b as input and returns the result of the bitwise OR operation between a and b. If b is 0, the function should return None. Test the function with the following inputs:  
a = 10, b = 2
a = 10, b = 0
Expected Output:
For a = 10 and b = 2, the output should be 10.
For a = 10 and b = 0, the output should be None.
'''

def divide(a, b):
    if b == 0:
        return None
    else:
        return a | b  # This uses the bitwise OR operator

# Function calls and print statements should be outside the function
result1 = divide(10, 2)
result2 = divide(10, 0)
print(result1)          #10
print(result2)          #None