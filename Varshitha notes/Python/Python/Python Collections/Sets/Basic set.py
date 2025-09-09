'''Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are --unchangeable--, but you can remove items and add new items
Set items are unordered, unchangeable, and do not allow -- duplicate values--..'''

1.Create set

set1={"apple", "banana", "cherry"}
print(set1)
#{'banana', 'cherry', 'apple'}
'''Note: ---Sets are unordered---, so you cannot be sure in which order the items will appear.'''

2.Unordered

Unordered means that the items in a set do not have a defined order.

3.Unchangeable

Set items are unchangeable, meaning that we cannot change the items after the set has been created.
--Once a set is created, you cannot change its items, but you can remove items and add new items.---

4.Duplicates Not Allowed
Sets cannot have two items with the same value.
--if dupilcate values are present in the list,then in output it will print only one value---

set1 = {"apple", "banana", "cherry", "banana"}
print(set1)
#{'banana', 'cherry', 'apple'}

5.True and 1 is considered the same value:
Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#{True, 2, 'banana', 'cherry', 'apple'}


thisset = {"apple", "banana", "cherry", 1, True, 2}
print(thisset)
#{1, 2, 'banana', 'cherry', 'apple'}

6.False and 0 is considered the same value:
The values False and 0 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", False, 0, 2}
print(thisset)
#{False, 2, 'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", 0, False, 2}
print(thisset)
#{0, 2, 'banana', 'cherry', 'apple'}

7.Get the Length of a Set

thisset = {"apple", "banana", "cherry", False, 0, 2}
print(len(thisset))
#5

8.Set Items - Data Types
Set items can be of any data type:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

A set with strings, integers and boolean values:

set1 ={"apple", "banana",1, 5,True, False}

9.type()

set1 = {"apple", "banana", "cherry"}
print(type(set1))
<class 'set'>

10.The set() Constructor
It is also possible to use the set() constructor to make a set.

set1=set(("apple", "banana",1, 5,True, False))
print(set1)
@{False, 1, 5, 'banana', 'apple'}


