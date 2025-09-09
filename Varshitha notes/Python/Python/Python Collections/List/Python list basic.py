"""List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data

Lists are created using square brackets:"""

1.Create a list

#
x =["apple", "mango","banana"]
print(x)            #['apple', 'mango', 'banana']

x = list(("apple", "mango","banana"))
print(x)            #['apple', 'mango', 'banana']

''' **List Items**
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.'''

'''**Ordered**
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.'''

'''**Changeable**
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.'''

'''**Allow Duplicates**
Since lists are indexed, lists can have items with the same value:'''

example:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

'''**List Length**
To determine how many items a list has, use the len() function'''

example
thislist = ["apple", "banana", "cherry"]
print(len(thislist))        #3

''' **List Items - Data Types**
List items can be of any data type:'''

Example
String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

'''A list can contain different data types:'''
list1 = ["abc", 34, True, 40, "male"]

'''**type()**

<class 'list'>'''

example:
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

'''**The list() Constructor**
It is also possible to use the list() constructor when creating a new list.'''

example:Using the list() constructor to make a List
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


