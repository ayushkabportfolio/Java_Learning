Loop Through a List

1.for new_variable in list_defined_varibale:
2.for new_variable in range(len(list_defined_varibale)):  # here it is calculating length of the list
        print(list_defined_varibale[index])
3.define variable wirh value
i = 0       #define to 0
while i < (len(list_defined_varibale))
    print(list_defined_varibale[i])
    i =i+1
4.define variable wirh value
[print(new_variable) for new_variable in list_defined_varibale]


1.You can loop through the list items by using a for loop

a = ["apple", "banana", "cherry"]
for x in a:
    print(x)
o/p:    apple
        banana
        cherry

2.Loop Through the Index Numbers
loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

a = ["apple", "banana", "cherry"]
for i in range(len(a)):   #here it is calculating length of the list
    print(a[0])           #and a[0] is apple and based on the length of the list index,tht many times o/p will be printed
o/p: apple
     apple
     apple

a = ["apple", "banana", "cherry"]
for i in range(len(a)):
    print(a[i])             #here i is 0,1,2 and it will print the values of the index from list
o/p: apple
    banana
    cherry

a = ["apple", "banana", "cherry"]
for i in range(len(a)):
    print(a)                        #here im not defining any index and based on the length calculated ,i.e,0,1,2
o/p: ['apple', 'banana', 'cherry']  #thht num of time value of the a variable it will print
     ['apple', 'banana', 'cherry']
     ['apple', 'banana', 'cherry']

3.Using a While Loop

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.

a = ['apple', 'banana', 'cherry']
i =0
while i < (len(a)):
    print(a[i])
    i = i+1
o/p: apple
    banana
    cherry

4.Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists

a = ['apple', 'banana', 'cherry']
[print(x) for x in a]               #prints all the varibale value one after the other
o/p: apple
    banana
    cherry

a = ['apple', 'banana', 'cherry']
[print(x) for x in a[1]]    #prints variable letter in new line
o/p:
b
a
n
a
n
a

