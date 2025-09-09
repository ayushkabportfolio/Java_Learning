#Python - Access Tuple Items
Note: The first item has index 0

1.Thru Index

a = ("apple", "banana", "cherry")
print(a[0])
#apple

2.Negative Indexing
'''Negative indexing means start from the end.

-1 refers to the last item, -2 refers to the second last item etc.'''

a = ("apple", "banana", "cherry")
print(a[-1])
#cherry

3.Range of Indexes   [i:j-1]
'''You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.'''

a = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(a[2:3])
#('cherry',)

a = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(a[2:5])
# ('cherry', 'orange', 'kiwi')

a = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(a[:6])
#('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon')

a = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(a[-7:])
#('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')


4.Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

a = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "apple" in a:
    print("it is there")        #it is there


