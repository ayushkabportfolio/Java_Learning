'''Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.'''

1.Dictionaries are written with curly brackets, and have keys and values:

create dict

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female'
}
print(a)
#{'name': 'varshi', 'age': 25, 'Gender': 'Female'}

2.How to print values inside the dict

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female'
}
print(a["Gender"])
#Female

3.Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

4.Changeable

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

5.Duplicates are not allowed

Dictionaries cannot have two items with the same key:

----Duplicate values will overwrite existing values:
    --and overwrites with the latest key value pair at the end

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
    "Gender":'Male'
}
print(a)  #{'name': 'varshi', 'age': 25, 'Gender': 'Male'}
print(a["Gender"])      #Male

6.Dictionary Length
To determine how many items a dictionary has, use the len() function:

---If 2 same Keys are there ,it will consider only one--

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
    "Gender":'Male'
}
print(len(a))   #3

7.Data Types
The values in dictionary items can be of any data type:
String, int, boolean, and list data types:
--Tuples should not contain immutable things inside the dict,
if it is mutable then tuple can be used inside the dict----

Immutable example:
a = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"],
   "Tuple": ("orange",)  #Immutable
}
print(a)

Mutuable example:
my_dict = {
    "fruits": ["apple", "banana"],
    "numbers": [1, 2, 3]
}
print(my_dict["fruits"])  # Output: ['apple', 'banana']
my_dict["fruits"].append("cherry")
print(my_dict["fruits"])  # Output: ['apple', 'banana', 'cherry']

8.type()  -- <class 'dict'>


a = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
    "Tuple": ("orange",)
}
print(type(a))  -- <class 'dict'>

9.The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.

constructdict= dict(name="varshi",age=25)
print(constructdict)
#{'name': 'varshi', 'age': 25}
