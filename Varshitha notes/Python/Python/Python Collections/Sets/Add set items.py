Add Items
Once a set is created, you cannot change its items, but you can add new items.

1.To add one item to a set use the add() method.

set1 = {"apple", "banana", "cherry"}
set1.add("orange")
print(set1)
#{'banana', 'orange', 'cherry', 'apple'}

2.adding 2 tuples - .update()

set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "banana", "mango"}
print(set1+set2) ##TypeError: unsupported operand type(s) for +: 'set' and 'set'

set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "banana", "mango"}
set1.update(set2)
print(set1)
#{'banana', 'orange', 'cherry', 'mango', 'apple'}

3.Sets can be added with list
set1 = {"apple", "banana", "cherry"}
set2 = ["orange", "banana", "mango"]
set1.update(set2)
print(set1)
#{'banana', 'orange', 'cherry', 'mango', 'apple'}

4.Sets can be added with Tuple
set1 = {"apple", "banana", "cherry"}
set2 = ("orange", "banana", "mango")
set1.update(set2)
print(set1)
#{'banana', 'orange', 'cherry', 'mango', 'apple'}


5.Sets can be added with dict
set1 = {"apple", "banana", "cherry"}
set2 = dict(name="varshi",age=26)
set1.update(set2)
print(set1)

#{'banana', 'age', 'name', 'cherry', 'apple'}