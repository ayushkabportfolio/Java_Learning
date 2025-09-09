Tuples
'''Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:'''

1.Create a tuple

a =("apple", "banana", "cherry")
print(a)
#("apple", "banana", "cherry")

2.Allow duplicate

a =("apple", "banana", "cherry", "cherry")
print(a)
# ("apple", "banana", "cherry", "cherry")

3.Length of the tuple
a =("apple", "banana", "cherry", "cherry")
print(len(a))
#4

a =("apple", "banana", "cherry", "cherry")
print(len(a[2]))
#6

5.Create Tuple With One Item
"""To create a tuple with only one item, you have to add a comma after the item, 
otherwise Python will not recognize it as a tuple."""

a =("apple",)           ##IF ONE VALUE TO BE TUPLE THEN COMMS SHOULD BE THERE AFTER 1ST VALUE
print(type(a))
#<class 'tuple'>

a =("apple")            ##NOT a TUPLE
print(type(a))
#<class 'str'>

6.Tuple Items - Data Types
"""Tuple items can be of any data type:"""

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

"""A tuple can contain different data types:"""
tuple1 = ("abc", 34, True, 40, "male")

7.type()
---From Python's perspective, tuples are defined as objects with the data type 'tuple':

<class 'tuple'>---

tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1))
#<class 'tuple'>

8.The tuple() Constructor

tuple1= tuple(("abc", 34, True, 40, "male"))
print(tuple1)
#('abc', 34, True, 40, 'male')
