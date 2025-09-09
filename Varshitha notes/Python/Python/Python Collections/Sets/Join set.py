'''Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.
"""""""""""""""""""""""
Union() = return the original set

set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "banana", "mango"}
set3=set1.union(set2)
print(set3)
print(set1)  ---- this will return the original set

update() = new set will be retuned

set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "banana", "mango"}
set1.update(set2)
print(set1)  -- this will return new set
""""""""""""""""""""""""""""""""""
The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

'''


1.Union()
The union() method returns a new set with all items from both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "banana", "mango"}
set3=set1.union(set2)
print(set3)
#{'cherry', 'banana', 'orange', 'apple', 'mango'}

---You can use the | operator instead of the union() method, and you will get the same result.--

ex:a
set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "banana", "mango"}
set3=set1 | set2
print(set3)
#{'cherry', 'banana', 'orange', 'apple', 'mango'}

ex:b
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#{1, 'b', 2, 3, 'a', 'c'}

1.a.Join multiple sets - with update and or operator |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {True, False}
set4 = dict(name='varshi',age=26)
set5=set1.union(set2,set3,set4)
set6 = set1 | set2 | set3| set4
print(set5)
print(set6)
#{False, 1, 2, 3, 'a', 'name', 'b', 'age', 'c'}
#TypeError: unsupported operand type(s) for |: 'set' and 'dict'

---Note:  unsupported operand type(s) for |: 'set' and 'dict'----

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {True, False}
set6 = set1 | set2 | set3
print(set5)
#{False, 1, 2, 3, 'a', 'name', 'b', 'age', 'c'}

1.b.Join diff data type

set1 = {"a", "b", "c"}
set2 = (1, 2, 3)
set3=set1.union(set2)
print(set3)
#{1, 2, 3, 'a', 'b', 'c'}
set4= set1 | set2
print(set4) #TypeError: unsupported operand type(s) for |: 'set' and 'tuple'

----Note: The  | operator only allows you to join sets with sets,
    and not with other data types like you can with the  union() method.---

2.Update()
'''The update() method inserts all items from one set into another.

The update() changes the original set, and does not return a new set.'''

set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "banana", "mango"}
set1.update(set2)
print(set1)
#{'cherry', 'banana', 'orange', 'apple', 'mango'}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {True, False}
set4 = dict(name='varshi',age=26)
set3.update(set4)
print(set3)
#{False, True, 'name', 'age'} == here instead value of the dict it is printing key

4.Intersection() and & AND operator

prints only the duplicate values



set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "banana", "mango"}
set3 =set1.intersection(set2)
print(set3)
#{'banana'}

set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "banana", "mango"}
set3= set1 & set2
print(set3)
#{'banana'}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {True, False}
set4 = set1 & set2 & set3
print(set4)
#set() becz no duplicate value

set1 = {"a", 2, "c"}
set2 = {1, 2, False}
set3 = {True, False, 2}
set4 = dict(name='varshi',age=26)
set5=set1.intersection(set2,set3,set4)
print(set5)  #set()

--Note: The & operator only allows you to join sets with sets,
    and not with other data types like you can with the intersection() method.----
set6 = set1 & set2 & set3 & set4
print(set6)  #TypeError: unsupported operand type(s) for &: 'set' and 'dict'

set1 = {"a", 2, "c"}
set2 = {1, 2, False}
set3 =set1.intersection(set2)
print(set3)
#{2}

5.intersection_update()
The intersection_update() method will also keep ONLY the duplicates,
but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)
#{'apple'}

5.a.Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)  #{False, 1, 'apple'}
set1.intersection_update(set2)
print(set1) #{False, 1, 'apple'}

6.Difference

The difference() method will return a new set that will contain only the items
from the first set that are not present in the other set.

--in simple ,it will remove duplicate value and print left over values from the set 1

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
#{'cherry', 'banana'}

6.a .You can use the " - operator" instead of the difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)
#{'cherry', 'banana'}

--Note: The - operator only allows you to join sets with sets,
    and not with other data types like you can with the difference() method.---

7.difference_update()
The difference_update() method will also keep the items from the first set that are not in the other set,
but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
#{'cherry', 'banana'}

8.Symmetric Differences
The symmetric_difference() method will keep only the elements that are NOT present in both sets.

--in simple ,it will remove duplicate value and print left over values from the both sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
# {'cherry', 'google', 'banana', 'microsoft'}

8.a .  ^ operator instead of the symmetric_difference() method,
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
# {'cherry', 'google', 'banana', 'microsoft'}

---Note: The ^ operator only allows you to join sets with sets,
    and not with other data types like you can with the symmetric_difference() method.---

9.symmetric_difference_update()
The symmetric_difference_update() method will also keep all but the duplicates,
but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
# {'cherry', 'google', 'banana', 'microsoft'}