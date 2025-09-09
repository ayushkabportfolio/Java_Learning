Access Dictionary Items

1.You can access the items of a dictionary by referring to its key name, inside square brackets:

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
print(a)  #{'name': 'varshi', 'age': 25, 'Gender': 'Female'}
print(a["Gender"])  #Female

2.Get()

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
x = a.get("age")
print(x)
#25

3.Get Keys
---- keys()---   #print only the Keys

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
x = a.keys()
print(x)
#dict_keys(['name', 'age', 'Gender'])

----adding new item to the original dict using "keys()"

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
x = a.keys()
a["married"] = "not"
print(x)
#dict_keys(['name', 'age', 'Gender', 'married'])

4.Get Values
The values() method will return a list of all the values in the dictionary.
--values()--

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
x = a.values()
print(x)  #dict_values(['varshi', 25, 'Female'])

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
x = a.values()
a["married"] = "not"
print(x)
#dict_values(['varshi', 25, 'Female', 'not'])

============================
NOTE:HERE WITHOUT KEYS() and Values() USAGE ALSO WE CAN ADD KEY -value pair TO THE DICT
a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
a["married"] = "not"
print(a)
#{'name': 'varshi', 'age': 25, 'Gender': 'Female', 'married': 'not'}

5.Get Items
The items() method will return each item in a dictionary, as tuples in a list.

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
x = a.items()
print(x)
# dict_items([('name', 'varshi'), ('age', 25), ('Gender', 'Female')])


------using items()  change the value of the key inside dict ,by using used Key inside the dict

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
x = a.items()
print(x)        #dict_items([('name', 'varshi'), ('age', 25), ('Gender', 'Female')])
a["Gender"] = "male"
print(x)            #dict_items([('name', 'varshi'), ('age', 25), ('Gender', 'male')])

----using items() - add the key value pair inside the item

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
x = a.items()
print(x)        #dict_items([('name', 'varshi'), ('age', 25), ('Gender', 'Female')])
a["married"] = "not"
print(x)        #dict_items([('name', 'varshi'), ('age', 25), ('Gender', 'Female'), ('married', 'not')])

6.Check if Key Exists
To determine if a "specified key" is present in a dictionary use the in keyword:

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
if "Gender" in a:
    print(a["Gender"])
#Female


---No output for the values
a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
if 25 in a:
    print("yes")

----if values want to be checked

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
if 25 in a.values():
    print("yes")
#yes

----if Keys want to be checked:

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
if "Gender" in a.keys():
    print("yes")
#yes
    