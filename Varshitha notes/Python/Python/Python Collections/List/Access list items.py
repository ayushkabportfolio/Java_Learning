#Access Items
print(variable[index])
print(variable[-ve index])
print(variable[range index])
check if variable is there or not
---if "apple" in thislist:
    print("yes it is there")


1.List items are indexed and you can access them by referring to the index number:
Note: The first item has index 0.

thislist = ["apple", "banana", "cherry"]
print(thislist[1])          #banana

2.Negative Indexing
Negative indexing means start from the end
Note:-1 refers to the last item, -2 refers to the second last item etc

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])             #cherry

3.Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

Note:When specifying a range, the return value will be a new list with the specified items.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])   #i:j-1
o/p : ['cherry', 'orange', 'kiwi']    #Note: The search will start at index 2 (included) and end at index 5 (not included).

Example
This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
o/p:['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[3:])
o/p:['orange', 'kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:-1])        # i:j-1
o/p:['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
o/p:['orange', 'kiwi', 'melon']

4.Check if Item Exists
To determine if a specified item is present in a list use the in keyword:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in thislist:
    print("yes it is there")
o/p:yes it is there