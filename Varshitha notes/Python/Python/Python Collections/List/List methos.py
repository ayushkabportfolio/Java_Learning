append()	Adds an element at the end of the list

a = ["a","b","c"]
b = [1,2,3]
for x in b:
    a.append(x)
print(a)
#['a', 'b', 'c', 1, 2, 3]

clear()	Removes all the elements from the list
a = ["a","b","c"]
a.clear()
print(a)
#[]

copy()	Returns a copy of the list
a = ["a","b","c"]
b = a.copy()
print(b)
#['a', 'b', 'c']

count()	Returns the number of elements with the specified value

a = ["a", "b", "c"]
b = a.count("a")
print(b)
#1

extend()	Add the elements of a list (or any iterable), to the end of the current list

a = ["a", "b", "c"]
b = [1,2,3]
a.extend(b)
print(a)
['a', 'b', 'c', 1, 2, 3]

index()	Returns the index of the first element with the specified value
a = ["a", "b", "c"]
b = a.index("a")
print(b)
#0

insert()	Adds an element at the specified position
a = ["a", "b", "c"]
a.insert(3,"e")
print(a)
['a', 'b', 'c', 'e']

pop()	Removes the element at the specified position
a = ["a", "b", "c"]
a.pop(2)
print(a)
#['a', 'b']

remove()	Removes the item with the specified value
a = ["a", "b", "c"]
a.remove("a")
print(a)
#['b', 'c']
reverse()	Reverses the order of the list

a = ["a", "b", "c"]
a.reverse()
print(a)
#['c', 'b', 'a']

sort()	Sorts the list

a = ["banana", "orange", "kiwi", "cherry"]
a.sort()
print(a)
#['banana', 'cherry', 'kiwi', 'orange']