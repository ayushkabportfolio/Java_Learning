Loop Through a Dictionary

You can loop through a dictionary by using a "for loop."

When looping through a dictionary, the return value are the "keys" of the dictionary,
but there are "methods to return the values as well".

1.Prints Key in loop
a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
for x in a:
    print(x)
# name
# age
# Gender

2.Prints values
a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
for x in a:
    print(a[x])
# varshi
# 25
# Female

3.Keys()

a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
for x in a.keys():
    print(x)
# name
# age
# Gender

4.Values()
a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
for x in a.values():
    print(x)
# varshi
# 25
# Female

5.items()
a ={
    "name":'varshi',
    "age":25,
    "Gender":'Female',
}
for name,age in a.items():  ##dont use quotes
    print(name,age)
#name varshi
# age 25
# Gender Female