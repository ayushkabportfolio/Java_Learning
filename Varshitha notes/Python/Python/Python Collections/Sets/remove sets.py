Remove sets
remove(), or the discard()

1.remove()
set1 = {"apple", "banana", "cherry"}
set1.remove("apple")
print(set1)
#{'banana', 'cherry'}

---Note: If the item to remove does not exist, remove() will raise an error.  ---

set1 = {"apple", "banana", "cherry"}
set1.remove("orange")
print(set1)
#KeyError: 'orange'

2.clear()
set1 = {"apple", "banana", "cherry"}
set1.clear()
print(set1)
#set()

3.del - removes the set completely
set1 = {"apple", "banana", "cherry"}
del set1
print(set1) #NameError: name 'set1' is not defined. Did you mean: 'set3'?

4.pop - removes random values from the list

set1 = {"apple", "banana", "cherry"}
set1.pop()
print(set1)
#{'cherry', 'apple'}

5.discard
set1 = {"apple", "banana", "cherry"}
set1.discard("cherry")
print(set1)
#{'banana', 'apple'}

---Note: If the item to remove does not exist, discard() will NOT raise an error. ,it just print set ---

set1 = {"apple", "banana", "cherry"}
set1.discard("orange")
print(set1)
#{'banana', 'cherry', 'apple'}
