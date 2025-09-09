1.Add

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
a["Married"] ="not"
print(a)
#{'name': 'varshi', 'age': 25, 'Gender': 'Female', 'Married': 'not'}

2.update()  -- #adding key-value pair and changing the value for the key

#add
a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
a.update({"married":"not"})
print(a)
#{'name': 'varshi', 'age': 25, 'Gender': 'Female', 'married': 'not'}

3. items()
a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
x = a.items()
a["married"] = "not"
print(dict(x))
#{'name': 'varshi', 'age': 25, 'Gender': 'Female', 'married': 'not'}