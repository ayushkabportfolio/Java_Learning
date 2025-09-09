add()	 	Adds an element to the set

set1 = {"apple", "banana", "cherry"}
set1.add("orange")
print(set1)
#{'cherry', 'apple', 'banana', 'orange'}

clear()	 	Removes all the elements from the set
set1 = {"apple", "banana", "cherry"}
set1.clear()
print(set1)
#set()

copy()	 	Returns a copy of the set  #1st copy to the other variable and add the required variable using add() method
set1 = {"apple", "banana", "cherry"}
set2=set1.copy()
set2.add("orange")
print(set2)
# {'cherry', 'apple', 'banana', 'orange'}


difference()	-	Returns a set containing the difference between two or more sets ,and return the remaining value from set 1
		---returns the original set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3= set1 - set2
print(set3)
# {'cherry', 'banana'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3= set1.difference(set2)
print(set3)
# {'cherry', 'banana'}

difference_update()	-=	Removes the items in this set that are also included in another, specified set
			---this will update the original set

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
# {'cherry', 'banana'}

discard()	 	Remove the specified item

set1 = {"apple", "banana", "cherry"}
set1.discard("banana")
print(set1)
# {'cherry', 'apple'}

intersection()	&	Returns a set, that is the intersection of two other sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3= set1.intersection(set2)
print(set3)
# {'apple'}

intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set3)
# {'apple'}

isdisjoint()	 	Returns whether two sets have a intersection or not

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.isdisjoint(set2)
print(set3)
#False

issubset()	<=	Returns whether another set contains this set or not
<	Returns whether all items in this set is present in other, specified set(s)

--simple way,if set1 elements present in the set2 then its true

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.issubset(set2)
print(set3)
# False
set4=set1 <= set2
print(set4)
#False

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple", "banana", "cherry"}
set3=set1.issubset(set2)
print(set3)
# True
set4=set1 <= set2
print(set4)
# True

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple", "banana", "cherry"}
set4=set1 < set2
print(set4)
# True


issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
--simple way,set2 checks all its values are containing in set1 or else it will print false

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple", "banana", "cherry"}
set3=set1.issuperset(set2)
print(set3)
# False
set4=set1 >= set2
print(set4)
# False

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple", "banana", "cherry"}
set4=set1 > set2
print(set4)
# False

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple", "banana", "cherry"}
set4=set2 > set1   ## set2 contains all the elements of the set 1
print(set4)
# True

pop()	 	Removes an random element from the set
set1 = {"apple", "banana", "cherry"}
set1.pop()
print(set1)
# {'apple', 'banana'}

remove()	 	Removes the specified element

set1 = {"apple", "banana", "cherry"}
set1.remove("cherry")
print(set1)
# {'apple', 'banana'}

symmetric_difference()	^	Returns a set with the symmetric differences of two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
# {'cherry', 'google', 'banana', 'microsoft'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
# {'cherry', 'google', 'banana', 'microsoft'}

symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
# {'cherry', 'google', 'banana', 'microsoft'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1 ^= set2
print(set1)
# {'cherry', 'google', 'banana', 'microsoft'}

union()	|	Return a set containing the union of sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 =set1.union(set2)
print(set3)
# {'cherry', 'microsoft', 'google', 'banana', 'apple'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3= set1 | set2
print(set3)
# {'cherry', 'microsoft', 'google', 'banana', 'apple'}


update()	|=	Update the set with the union of this set and others

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.update(set2)
print(set1)
# {'cherry', 'microsoft', 'google', 'banana', 'apple'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1 |= set2
print(set1)
# {'cherry', 'microsoft', 'google', 'banana', 'apple'}