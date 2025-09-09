Generating random values
#import random {built -in fucntion}

1.we can randomly print the integer

import random

for i in range(3):
    print(random.random())

2.If we want to print between the values

import random

for i  in range(3):
    print(random.randint(a=10,b=15)) #randint is for to print interger bewtenn the range including both end point
#14         #three times range it will print values between 10 & 15
# 11
# 10

3.How to select the random name frm the list
# "random.choice" method chooses value in the list randomly

import random

names = ["John","varshi","SMith"]
print(random.choice(names))

Qn: print random dice values like (1,3) using random and class

import random
class Dice:
    def roll(self):
        first = random.randint(1,6)
        Second = random.randint(1, 6)
        return first,Second         # by default this will print as tuple

dice = Dice()
print(dice.roll())


---------Working with directories-----
search in google with pyhton 3 module index

pathlib helps to print the file is present or not in tht directory or prints the files in the directory
helps to use relative paths

Here path of the main directory is considered - C:\Users\varshitha.r\OneDrive - Comviva Technologies LTD\learning

#will check directory is present or not
from pathlib import Path   #path is class

path =Path("From utube")            #From utube - relative path
print(path.exists())   #True

path =Path("From ")
print(path.exists())    #False

#will c how to create directory

from pathlib import Path
path = Path("Super")
print(path.mkdir())  #directory will be created in name Super i current path

#remove the direcroty

from pathlib import Path
path = Path("Super")
print(path.rmdir())

#How to check all files in current direcory

a.prints all the .py files inside the main path by using path.glob()
from pathlib import Path

path = Path()
# print(path.glob("x."))  o/p: <generator object Path.glob at 0x000002430ABFB890>
# for now we will just iterate with loop
for files in path.glob("*.py"):
    print(files)

b.prints all the files only
from pathlib import Path

path = Path()
# print(path.glob("x."))  o/p: <generator object Path.glob at 0x000002430ABFB890>
# for now we will just iterate with loop
for files in path.glob("*.*"):
    print(files)

c.Prints all the files and directory names
from pathlib import Path

path = Path()
# print(path.glob("x."))  o/p: <generator object Path.glob at 0x000002430ABFB890>
# for now we will just iterate with loop
for files in path.glob("*"):
    print(files)

