1.The while Loop
"With the while loop we can execute a set of statements as long as a condition is true."

i = 10
while i < 15:     ##if condition here only fails it wont print output so first here condition should pass
    print(i)
    i += 1
#print values form 10 to 14

2.The break Statement
"With the break statement we can stop the loop even if the while condition is true:"

i = 10
while i < 15:     ##if condition here only fails it wont print output so first here condition should pass
    print(i)
    if i == 13:
        break
    i += 1
#print values form 10 to 13

3.The continue Statement
"With the continue statement we can stop the current iteration, and continue with the next:"

i = 0
while i < 6:
    i += 1
    if i == 3:    ##here it will check 3 and stop tht number and print frm next number
        continue
    print(i)
# Note that number 3 is missing in the result

4.The else Statement
"With the else statement we can run a block of code once when the condition no longer is true:"

--Print a message once the condition is false:--

i = 10
while i < 15:
    print(i)
    i += 1
else:
    print("i is no longer smaller than 15")
"""10
11
12
13
14
i is no longer smaller than 15"""