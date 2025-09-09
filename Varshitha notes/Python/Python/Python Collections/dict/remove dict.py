1.pop()

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
a.pop("age")
print(a)
#{'name': 'varshi', 'Gender': 'Female'}

2. clear()
a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
a.clear()
print(a)
#{}

3.popitems()
---Removes the last item from the dict--

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
a.popitem()
print(a)
#{'name': 'varshi', 'age': 25}

4.del

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
del a    ##delete all the complete dict
print(a)

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
del a["age"]    ##delete specified Key item
print(a)
#{'name': 'varshi', 'Gender': 'Female'}
