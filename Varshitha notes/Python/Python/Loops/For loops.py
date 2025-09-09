Python For Loops
"""A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc."""

1. for loop for list

a = ["apple", "banana", "cherry"]
for x in a:
    print(x)
# apple
# banana
# cherry

2.for loop using in string

a = "apple"
for x in a:
    print(x)
"""a
p
p
l
e"""

3.The break Statement
"With the break statement we can stop the loop before it has looped through all the items:"

a = ["apple", "banana", "cherry", "mango"]
for x in a:
    print(x)
    if x == "cherry":
        break               ##here print 1st it will do an dthen check the condition and break the statement
"""apple
banana
cherry"""

--the break comes before the print:--
a = ["apple", "banana", "cherry", "mango"]
for x in a:
    if x == "cherry":
        break
    print(x)    ##here 1st it is checking the conditions and if it is true then there only it willl break statement
"""apple
banana"""

4.The continue Statement

a = ["apple", "banana", "cherry", "mango"]
for x in a:
    print(x)
    if x == "cherry":           #after condition true also it will continue
        continue
    """apple
banana
cherry
mango"""

a = ["apple", "banana", "cherry", "mango"]
for x in a:
    if x == "cherry":           #after condition true also it will continue,but remove the chery
        continue
    print(x)

5.The range() Function
"To loop through a set of code a specified number of times, we can use the range() function,"

--The range() function returns a sequence of numbers, starting from 0 by default,
and increments by 1 (by default), and ends at a specified number.---
 #range(i-1) ,exampe range(3) it will print 0,1,2 not 3

for x in range(3):
    print(x)
# 0
#1
#2

--Using the start parameter:
for x in range(1,5):
    print(x)
# 1
# 2
# 3
# 4

--Increment the sequence by specifiying to value --- but usually default increment happens with 1--

range(start,end,defining default value)

for x in range(2,5,2):
    print(x)
# 2
# 4

6.Else in For Loop
"The else keyword in a for loop specifies a block of code to be executed when the loop is finished:"
--prints the for loop output and contect inside the else statement--

for x in "banana":
    print(x)
else:
    print("finished")
# b
# a
# n
# a
# n
# a
# finished

--Note: The else block will NOT be executed if the loop is stopped by a break statement.--

for x in "banana":
    if x == "a": break
    print(x)
else:
    print("finished")
# b

for x in "banana":
    if x == "c": break   ##here condition is failed so it will print else statement also
    print(x)
else:
    print("finished")

7.Nested Loops
"A nested loop is a loop inside a loop.

"The "inner loop" will be executed one time for each iteration of the "outer loop""

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x , y)
"""red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry"""

8.The pass Statement
"for loops cannot be empty, but if you for some reason have a for loop with no content,
"put in the pass statement to avoid getting an error."

for x in [ 1,2,3]:
    pass    #no o/p

