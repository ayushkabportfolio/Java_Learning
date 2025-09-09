Copy list

b=a.copy()
b = list(a)
b=a(:)

copying one list value  to other list

1.Copy()

a = ["apple", "banana", "cherry"]
b = a.copy()
print(b)
#['apple', 'banana', 'cherry']

2.list()
a = ["apple", "banana", "cherry"]
b = list(a)
print(b)
#["apple", "banana", "cherry"]

3.Slice operator(:)

a = ["apple", "banana", "cherry"]
b = a[:]
print(b)
#["apple", "banana", "cherry"]