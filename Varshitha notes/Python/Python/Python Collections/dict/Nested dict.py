Nested Dictionaries

A dictionary can contain dictionaries, this is called nested dictionaries.

1.Create a dictionary that contain three dictionaries:

a ={
    "a1":{"name":'varshi',
    "age":25,
    "Gender":'Female',
    },
    "a2":{
    "name" : "Tobias",
    "year" : 2007
    },
    "a3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(a)
#{'a1': {'name': 'varshi', 'age': 25, 'Gender': 'Female'},
# 'a2': {'name': 'Tobias', 'year': 2007}, 'a3': {'name': 'Linus', 'year': 2011}}

2.Create three dictionaries, then create one dictionary that will contain the other three dictionaries:


A1={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
A2={
    "name" : "Tobias",
"year" : 2007
}
A3 = {
    "name" : "Linus",
    "year" : 2011
}
total={
        "a1": A1,
        "a2": A2,
        "a3": A3
}

print(total)
#{'a1': {'name': 'varshi', 'age': 25, 'Gender': 'Female'},
# 'a2': {'name': 'Tobias', 'year': 2007}, 'a3': {'name': 'Linus', 'year': 2011}}

3.Access Items in Nested Dictionaries
To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

    a = {
        "a1": {"name": 'varshi',
               "age": 25,
               "Gender": 'Female',
               },
        "a2": {
            "name": "Tobias",
            "year": 2007
        },
        "a3": {
            "name": "Linus",
            "year": 2011
        }
    }
    print(a["a1"]["name"])   #varshi
    print(a["a2"]["year"])   #2007
    print(a["a3"]["name"])   #Linus

4.Loop Through Nested Dictionaries

by using the items() method like this:
Loop through the keys and values of all nested dictionaries:

a = {
    "a1": {"name": 'varshi',
           "age": 25,
           "Gender": 'Female',
           },
    "a2": {
        "name": "Tobias",
        "year": 2007
    },
    "a3": {
        "name": "Linus",
        "year": 2011
    }
}
for x ,obj in a.items():
    print(x)

    for y in obj:
        print(y + ':',obj[y] )
'''a1
name: varshi
age: 25
Gender: Female
a2
name: Tobias
year: 2007
a3
name: Linus
year: 2011'''

