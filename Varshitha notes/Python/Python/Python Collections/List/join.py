Join list

joining the 2 lists

1. +

a = ["a","b","c"]
b = [1,2,3]
c = a +b
print(c)
#['a', 'b', 'c', 1, 2, 3]

2.append
a = ["a","b","c"]
b = [1,2,3]
for x in b:
    a.append(x)
print(a)
#['a', 'b', 'c', 1, 2, 3]

3.extend
a = ["a","b","c"]
b = [1,2,3]
a.extend(b)
print(a)
#['a', 'b', 'c', 1, 2, 3]

a = ["a","b","c"]
b = [1,2,3]
for x in b:
    a.extend(x)
print(a)####error :TypeError: 'int' object is not iterable

