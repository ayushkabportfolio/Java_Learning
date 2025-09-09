clear()	Removes all the elements from the dictionary

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
a.clear()
print(a)
#{}

copy()	Returns a copy of the dictionary

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
b = a.copy()
print(b)
#{'name': 'varshi', 'age': 25, 'Gender': 'Female'}


fromkeys()	Returns a dictionary with the specified keys and value

a = {
    "name": 'varshi',
    "age": 25,
    "Gender": 'Female',
}
b= dict.fromkeys(["married"])
print(b)
# {'married': None}



get()	Returns the value of the specified key

a = {
    "name": 'varshi',
    "age": 25,
    "Gender": 'Female',
}
b =a.get("name")
print(b)   #varshi

items()	Returns a list containing a tuple for each key value pair

a = {
    "name": 'varshi',
    "age": 25,
    "Gender": 'Female',
}
b =a.items()
print(b)
#dict_items([('name', 'varshi'), ('age', 25), ('Gender', 'Female')])

keys()	Returns a list containing the dictionary's keys

a = {
    "name": 'varshi',
    "age": 25,
    "Gender": 'Female',
}
b = a.keys()
print(b)
# dict_keys(['name', 'age', 'Gender'])

pop()	Removes the element with the specified key
a = {
    "name": 'varshi',
    "age": 25,
    "Gender": 'Female',
}
a.pop("age")
print(a)
# {'name': 'varshi', 'Gender': 'Female'}

popitem()	Removes the last inserted key-value pair

a = {
    "name": 'varshi',
    "age": 25,
    "Gender": 'Female',
}
a.popitem()
print(a)
#{'name': 'varshi', 'age': 25}

setdefault()	Returns the value of the specified key.
If the key does not exist: insert the key, with the specified value

a = {
    "name": 'varshi',
    "age": 25,
    "Gender": 'Female',
}
a.setdefault("age",30)
print(a)            # # This does not change the value because "age" already exists
a.setdefault("married","not")
print(a)        #{'name': 'varshi', 'age': 25, 'Gender': 'Female', 'married': 'not'}


update()	Updates the dictionary with the specified key-value pairs

a = {
    "name": 'varshi',
    "age": 25,
    "Gender": 'Female',
}
a.update({"age":30})
print(a)
#{'name': 'varshi', 'age': 30, 'Gender': 'Female'}

values()	Returns a list of all the values in the dictionary

a = {
    "name": 'varshi',
    "age": 25,
    "Gender": 'Female',
}
b = a.values()
print(b)
#dict_values(['varshi', 25, 'Female'])