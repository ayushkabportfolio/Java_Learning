# Add List Items
variable.append("value")
variable.insert(index,"value")
variable.extend(which variable to be added)
variable.[thru index]
variable.[thru index range]
can add any collections to the list thru extend

1.Append Items
To add an item to the end of the list, use the append() method:

a = ["apple", "banana", "cherry"]
a.append("orange")
print(a)
o/p:['apple', 'banana', 'cherry', 'orange']

2.Insert Items
The insert() method inserts an item at the specified index:

a = ["apple", "banana", "cherry"]
a.insert(0,"orange")
print(a)
o/p:['orange', 'apple', 'banana', 'cherry']

3.Extend List
To append elements from another list to the current list, use the extend() method

a = ["apple", "banana", "cherry"]
b = ['orange', 'pineappel']
a.extend(b)
print(a)
o/p:['apple', 'banana', 'cherry', 'orange', 'pineappel']

3.a.Add Any Iterable

The extend() method does not have to append lists, you can add any iterable object
(tuples, sets, dictionaries etc.)

tuple
a = ["apple", "banana", "cherry"]
b = ('orange', 'pineappel')
a.extend(b)
print(a)        #o/p:['apple', 'banana', 'cherry', 'orange', 'pineappel']
print(tuple(a))     #o/p:('apple', 'banana', 'cherry', 'orange', 'pineappel')

set
a = ["apple", "banana", "cherry"]
b = {'orange', 'pineappel'}
a.extend(b)
print(a)        #o/p:['apple', 'banana', 'cherry', 'orange', 'pineappel']
print(set(a))     #o/p:{'apple', 'pineappel', 'cherry', 'banana', 'orange'}

dict
a = ["apple", "banana", "cherry"]
b = {'fruit1':'orange', 'fruit2':'pineapple'}
a.extend(b.values())
print(a)        #o/p:['apple', 'banana', 'cherry', 'orange', 'pineapple']


--wrng--

a = ["apple", "banana", "cherry"]
b = {'fruit1':'orange', 'fruit2':'pineapple'}
a.extend(b)
print(a)
o/p:['apple', 'banana', 'cherry', 'fruit1', 'fruit2']
Instaed values it will add name of the dict