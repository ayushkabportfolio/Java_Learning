1.Change Values

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
a["Gender"] ="Male"
print(a)
#{'name': 'varshi', 'age': 25, 'Gender': 'Male'}

2.Items()

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
x = a.items()
a["Gender"] = "Male"
print(x)

3.update()  -- #adding key-value pair and changing the value for the key

#add
a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
a.update({"married":"not"})
print(a)
#{'name': 'varshi', 'age': 25, 'Gender': 'Female', 'married': 'not'}

#change
a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
a.update({"Gender":"male"})
print(a)
#{'name': 'varshi', 'age': 25, 'Gender': 'male'}


a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
x = a.items()
a["married"] = "not"
print(dict(x))
#{'name': 'varshi', 'age': 25, 'Gender': 'Female', 'married': 'not'}