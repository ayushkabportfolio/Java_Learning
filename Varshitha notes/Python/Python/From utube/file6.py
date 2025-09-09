classes
we can create new type ,wht evr we define inside class tht will be kinda blue print for thr objects
Objects are where we use the Class's defined types

To define classname ,we hv to follow pascal type mean,evry 1st letter of word will be Capital
ex: Point,EmailCenter ,MailBox etc
while defining class name we are not using any underscore btween the 2 words ,just making tht 1st letter as capital without space
ex: EmailCenter

class Point:
    def draw(self):
        print("draw")
    def label(self):
        print("label")

#now use use defined types in obejects

point1 = Point()        #call class
point1.draw()   #draw

point1 = Point()        #we can define attributes also
point1.x = 10
point1.y =20
print(point1.x)     #10
print(point1.y)     #20

point2 = Point()
point2.label()      #label
point2.x = 30
# print(point2.x)  #AttributeError: 'Point' object has no attribute 'x'
#                     here x value for point2 is not defined
print(point2.x)         #30

-----Constructor----
COnstructor helps to create a object by using init
Each object is sepaarte instance of a class

class Point:
    def __init__(self,x,y):     #here only we r initialsing the attributes within the class ,so tht in object we dont
        self.x = x                  #to define attibutes separately
        self.y = y
    def draw(self):
        print("draw")
    def label(self):
        print("label")

point1 = Point(10,20)        # here the attrubutes value it is assiging to x & y  #defiing obejct
print(point1.x)     #10

# we can update values also

point1.x = 11
print(point1.x)     #11

QN: class type is Person
    define -name attribute and talk() method

class Person:
    def __init__(self,name):    #name attribute
        self.name=name
    def talk(self):             #Talk method
        print("talk")

person1 = Person("varshi")
person1.talk()          #talk
print(person1.name)         #varshi


Qn2 : How to use name attribute in method and print it

class Person:
    def __init__(self,name):
        self.name =name
       def talk(self):
           print(f"Hi frnd {self.name}")  # here we r using self to map the attribute name and calling it

person1 = Person("varshi")
person1.talk() #Hi frnd varshi

# we can use talk() method for 2nd person also
person2 = Person("varshitha")
person2.talk()          #Hi frnd varshitha

------Inheritence------

Copying the methods frm parent class like how children will be hvng few chaarcters of their parent

#main class
class mammal:
    def walk(self):
        print("walk")

class dog(mammal):      #calling parent in dog class,so whatevr the methods in parent class,all methods will be used in child class
    def eat(self):                            #In child class we can define its own method also
        print("eat")
#dog object will has walk and eat both methods as mammal has walk and dog has eat method

class cat(dog):             #calling child inside the child like in hierarchy
    pass                #using pass to make the class valid without adding any methods or print
#here cat class will hv eat and walk as well,becz dog has eat method and in dog class we hv called mammal class ,& then Mammal has walk method

Animal = mammal()
Animal.walk()   #walk
dog1 =dog()         #define object
dog1.walk()     #walk
dog1.eat()      #eat
Cat = cat()
Cat.eat()       #eat

--------Modules----------
Modules is like a files or sections
calling one file functions in different lines
Modules used to maintain code properly and in constructive way,so tht modules can be reused

ex in supermarket page has so many sections or modules like vegetables,fruits,kitchen items etc

#defined fuctn in Character.py file
def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45

#import the module file and use functions in this file

import  Character

print(Character.lbs_to_kg(175))

#here we can impotr specific function frm module file
from Character import lbs_to_kg

lbs_to_kg(75)


Qn. write functn for find largets num in list and call it in diff module

# 1st module named as Utilis

def largest_num(numbers):
    num = take_list[0]
    for x in take_list:
        if x > num:
            num = x
    return num

#2nd module page where names file name as using.py

from Utilis import largest_num

take_list = [1,2,3,4,5]
maxi = largest_num(take_list)
print(maxi)


------Packages-----

Packages are like directories to maintain  constructive codes

In pycharm we hv option to create package or
we can create one directory and inside tht create __init__.py file name to make tht directory as package

1.Create a package [package name = shoping]
2.Create one module file [module name = ship]

#inside module file under package

def shipping():
    print("shipping")

#Now call the module whch is inside the package into so other module

a. we can call
# from package.module import fuctn
# fuctn

from shoping.ship import shipping

shipping()

    # if we want to call multiple fuctions
from shoping.ship import shipping,boating,etc..

shipping()

b.we can call package's module direclty
# from package import module
# module.funct

from shoping import ship

ship.shipping()


Note : dont give already existing method names ,not a good practise






