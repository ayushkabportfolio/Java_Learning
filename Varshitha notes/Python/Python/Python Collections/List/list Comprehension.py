List Comprehension

helps to create Shorter syntax - when want to create new list using the existing list


1.without comprehesion - using for loop

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
o/p:['apple', 'banana', 'mango']

2.with comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist= [x for x in fruits if "a" in x]  #1st x is empty variable,2nd x defining to fruits
print(newlist)                            # and 3rd x checking a letter inside the stored values in 2nd x
o/p: ['apple', 'banana', 'mango']


-3.--The syntax for using conditions inside

newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)                  #excluded the apple and print the list
##The condition if x != "apple"  will return True for all elements other than "apple",
# making the new list contain all fruits except "apple

4.without if statement
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
#["apple", "banana", "cherry", "kiwi", "mango"]

5.Iterable
he iterable can be any iterable object, like a list, tuple, set etc

5.a.with range
newlist = [x for x in range(10)]
print(newlist)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

5.b .with condition using range
newlist=[x for x in range(10) if x < 5]         #here in the range of 10 (0 to 9),it will check less than 5 and
print(newlist)                                      #print values less then 5
#[0, 1, 2, 3, 4]

6.Expression
"""The expression is the current item in the iteration, but it is also the outcome, 
which you can manipulate before it ends up like a list item in the new list:"""

methods can be used inside

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
#['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

7.set all values in the newlist to one varibale

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ["hello" for x in fruits]
print(newlist)
#['hello', 'hello', 'hello', 'hello', 'hello']

7.1.expression can be sued wiht conditions  - manipulate list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x!= "banana" else "orange" for x in fruits]
print(newlist)       #replaceses banana with orange
#['apple', 'orange', 'cherry', 'kiwi', 'mango']

