# Change Item Value
variable[index] = [""]
varibale[index range]= [""]
variable.insert[index,"variable"]


1.To change the value of a specific item, refer to the index number:

a = ["apple", "banana", "cherry"]
a[1] = "orange"
print(a)
o/p:['apple', 'orange', 'cherry']

#Change a Range of Item Values

1.To change the value of items within a specific range, define a list with the new values,
and refer to the range of index numbers where you want to insert the new values

a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
a[0:3] = ["blackcurrant", "watermelon"]
print(a)
o/p:['blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

2.If you insert more items than you replace, the new items will be inserted where you specified,
and the remaining items will move accordingly:

a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(a[1:2])   #o/p:['banana']
a[1:2] = ["blackcurrant", "watermelon"]
print(a)
o/p:['apple', 'blackcurrant', 'watermelon', 'cherry', 'orange', 'kiwi', 'mango']

=--Replace--=
If you insert less items than you replace, the new items will be inserted where you specified,
and the remaining items will move accordingly

a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
a[1:3] = ["blackcurrant", "watermelon"]
print(a)
o/p:['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

=--Insert items--=

1stmethod
a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
a[1:1] = ["blackcurrant", "watermelon"]
print(a)
o/p:['apple', 'blackcurrant', 'watermelon', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

2nd method - insert

a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
a.insert(2,["blackcurrant", "watermelon"])
print(a)
# o/p:['apple', 'banana', ['blackcurrant', 'watermelon'], 'cherry', 'orange', 'kiwi', 'mango']
a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
a.insert(2,"blackcurrant")
print(a)
o/p:['apple', 'banana', 'blackcurrant', 'cherry', 'orange', 'kiwi', 'mango']