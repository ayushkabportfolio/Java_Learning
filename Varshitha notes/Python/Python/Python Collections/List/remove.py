Remove Specified Item

varibale.remove("variable")
variable.pop(index)
variable.pop() -removes at the end
del variable - removes whle list and no output
variable.clear()   - removes whole list values and output will be []

1.The remove() method removes the specified item
a = ["apple", "banana", "cherry"]
a.remove("banana")
print(a)
o/p:['apple', 'cherry']

2.If there are more than one item with the specified value, the remove() method removes the first occurrence

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
o/p:['apple', 'cherry', 'banana', 'kiwi']


##to remove both the bananas in the list
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
while "banana" in thislist:
    thislist.remove("banana")
    print(thislist)
o/p:['apple', 'cherry', 'kiwi']

3.Remove Specified Index

a.The pop() method removes the specified index value

a = ["apple", "banana", "cherry", "banana", "kiwi"]
a.pop(2)
print(a)
o/p: ['apple', 'banana', 'banana', 'kiwi']

b.If you do not specify the index, the pop() method removes the last item.

a = ["apple", "banana", "cherry", "banana", "kiwi"]
a.pop()
print(a)
o/p: ['apple', 'banana', 'cherry', 'banana']

4.The del keyword also removes the specified index: not a method

a = ["apple", "banana", "cherry", "banana", "kiwi"]
del a[4]
print(a)
o/p:['apple', 'banana', 'cherry', 'banana']

4.1.thru del we can remove full list only

a = ["apple", "banana", "cherry", "banana", "kiwi"]
del a  #no output

5.Clear the List
The clear() method empties the list.

The list still remains, but it has no content.

a = ["apple", "banana", "cherry", "banana", "kiwi"]
a.clear()
print(a)   o/p:[]


