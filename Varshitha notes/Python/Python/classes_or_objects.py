Python Classes/Objects
"""Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects."""

1.create class

class myclass:
    x = 5
2.Create object
Now we can use created class from above to create object


class myclass:
    x = 5
a = myclass()
print(a.x)
#5

3.The __init__() Function
"""All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, 
or other operations that are necessary to do when the object is being created"""

class person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age
a = person("varshi", 25)
print(a.name)
print(a.age)
# varshi
# 25

Note: The __init__() function is called automatically every time the class is being used to create a new object.

4.The __str__() Function
"""The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned"""

class person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name}{self.age}'
a = person("varshi",25)
print(a)
#vasrhi25

5.Object Methods
"""Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#Hello my name is John

Note: The self parameter is a reference to the current instance of the class,
    and is used to access variables that belong to the class.

6.The self Parameter
"""The self parameter is a reference to the current instance of the class, 
    and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like,
but it has to be the first parameter of any function in the class:"""

Example
Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
#Hello my name is John

6.Modify Object Properties
"You can modify properties on objects like this:"

class person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age

a = person("varshi", 25)
a.age = 30
print(a.age) #30

7.Delete Object Properties
"You can delete properties on objects by using the del keyword"

class person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age

a = person("varshi", 25)
del a.age
print(a.age)
#ttributeError: 'person' object has no attribute 'age'

8.Delete Objects
"You can delete objects by using the del keyword"

class person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age

a = person("varshi", 25)
del a   #no output becz it has deleted object only

9.The pass Statement
"class definitions cannot be empty, but if you for some reason have a class definition with no content,"
"put in the pass statement to avoid getting an error."

class person:
    pass  #not o/p

