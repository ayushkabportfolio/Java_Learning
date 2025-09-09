Python If ... Else

Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

--Indentation--
** indentation is ery impt in python ,in other lang they use brackets to define but here whitespace is impt

without proper indentaion
a = 10
b = 40
if a<b:
print("True")       ##error

1.if
'''An "if statement" is written by using the if keyword.'''

--if conditions is true only then it will print the defined statement to print--

a = 10
b = 40
if a<b:
    print("True")
#False

2.Elif
"if the previous conditions were not true, then try this condition"

a = 10
b = 40
if a > b:
    print("False")
elif a < b:
    print("True")
#True      -- here scond condition is true according to logic ,so it printed true

3.Else
"The else keyword catches anything which isn't caught by the preceding conditions."

a = 10
b = 40
if a > b:
    print("False")
elif a == b:
    print("True")
else:
    print("a is smaller than b")
#a is smaller than b

a = 10
b = 40
if a > b:
    print("False")
else:
    print("a is smaller than b")
#a is smaller than b

4.Short Hand If
"If you have only one statement to execute, you can put it on the same line as the if statement."

a = 10
b = 40
if a < b: print("True")
#True

5.Short Hand If ... Else
"If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:"

a = 10
b = 40
print("False") if a > b else print("a is smaller than b")
#a is smaller than b

----You can also have multiple else statements on the same line:--

a = 10
b = 10
print("False") if a > b else print("yes both equal") if a == b else print("a is smaller than b")
# yes both equal

6.And
"The and keyword is a logical operator, and is used to combine conditional statements:"

a = 10
b =20
c = 100
if a < b and c > b:
    print("Both conditions are true")
#Both conditions are true

a = 10
b =20
c = 100
if a > b and c > b:
    print("Both conditions are true")  # no output becz in both conditions,one conditions is getting falied
#     for AND operator both the conditin should be true

7.Or
"The or keyword is a logical operator, and is used to combine conditional statements:"

a = 10
b =20
c = 100
if a > b or c > b:
    print("One conditions are true")
#One conditions are true    #     for OR operator One of the conditin should be true

8.Not
"The not keyword is a logical operator, and is used to reverse the result of the conditional statement:"

--if conditions failes only it will print output---

a = 10
b =20
c = 100
if not a >b:
    print("condition failes")
# condition failes

8.Nested If
"You can have if statements inside if statements, this is called nested if statements."

a = 10
b =20
c = 100
if a < b:
    print("condition failes")  ## if this conditions pass only it will move to next If condition
    if a == b:
        print("True")
    else:
        print("False")
#  condition failes
# False

9.The pass Statement
"if statements cannot be empty, but if you for some reason have an if statement with no content,
"put in the pass statement to avoid getting an error.""

a = 10
b =20
if a < b:
    pass   #no output  -- even condition check is happening but there is no content to print


