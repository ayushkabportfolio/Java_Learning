# Change Tuple Values
'''Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.'''

#Workaround can be done - convert tuple to list and then add,remove,change

1.Change/replace

a=("apple", "banana", "cherry")
b=list(a)
print(b)            #['apple', 'banana', 'cherry']
b[1] = "Kiwi"
print(b)            #['apple', 'Kiwi', 'cherry']
a = tuple(b)
print(a)        #('apple', 'Kiwi', 'cherry')

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#('apple', 'kiwi', 'cherry')


2.Add items to the list

a=("apple", "banana", "cherry")
b=list(a)
b.append("orange")
print(b)            #['apple', 'banana', 'cherry', 'orange']
a=tuple(b)
print(a)
('apple', 'banana', 'cherry', 'orange')  # Print the tuple after converting the modified list

a=("apple", "banana", "cherry")
b=list(a)
b.insert(1,"orange")
print(b)            #['apple', 'banana', 'cherry', 'orange']
a=tuple(b)
print(a)        #('apple', 'orange', 'banana', 'cherry')

a=("apple", "banana", "cherry")
c = ("cool","bool")
b=list(a)
d=list(c)
b.extend(d)
print(b)            #['apple', 'banana', 'cherry', 'cool', 'bool']
a=tuple(b)
print(a)        #('apple', 'banana', 'cherry', 'cool', 'bool')

3.tuple to tuple adding

a=("apple", "banana", "cherry")
b = ("cool","bool")

a += b
print(a)
# ('apple', 'banana', 'cherry', 'cool', 'bool')

4.Remove Items

a=("apple", "banana", "cherry")
b=list(a)
b.remove("apple")
print(b)
a =tuple(b)
print(a)
#("banana", "cherry")

a=("apple", "banana", "cherry")
b=list(a)
b.pop(1)
print(b)
a =tuple(b)
print(a)
#('apple', 'cherry')

a=("apple", "banana", "cherry")
b=list(a)
b.clear()
print(b)
a =tuple(b)
print(a)
#()

---The del keyword can delete the tuple completely:---

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

a=("apple", "banana", "cherry")
b=list(a)
del b
a = tuple(b)
print(a)        #NameError: name 'b' is not defined

