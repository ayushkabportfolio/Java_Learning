9.Default Parameter Value
"If we call the function without argument, it uses the default value:"

def myfucnt(name = "varshitha"):
    print(name + ' Gowda')

myfucnt("varshi")
myfucnt("qwerty")
myfucnt()      #here im not calling any argument,it is default taking defined value
# varshi Gowda
# qwerty Gowda
# varshitha Gowda

10.Passing a List as an Argument
"""You can send any data types of argument to a function (string, number, list, dictionary etc.),
and it will be treated as the same data type inside the function."""

---if you send a List as an argument, it will still be a List when it reaches the function---

def funct(food):
    for x in food:
        print(x)
fruits=["apple","mango","banana"]
funct(fruits)
# apple
# mango
# banana

11.Return Values
"To let a function return a value, use the return statement:"

def funct(x):
    return 5 * x
print(funct(3))
#15

12.The pass Statement
"""function definitions cannot be empty, but if you for some reason have a function definition with no content, 
put in the pass statement to avoid getting an error."""

def name(x):
    pass  #no o/p

13.Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
#
# To specify that a function can have only positional arguments, add , / after the arguments

def name(x, /):
    print(x)
name(3)
#3

---Without the , / you are actually allowed to use keyword arguments even
if the function expects positional arguments---

def name(x):
    print(x)
name(3)
#3

def name(x):
    print(x)
name(x = 3)
#3

---But when adding the , / you will get an error if you try to send a keyword argument--


def name(x, /):
    print(x)
name(x=3)
#TypeError: name() got some positional-only arguments passed as keyword arguments: 'x'

14.Keyword-Only Arguments
"To specify that a function can have only keyword arguments, add *, before the arguments"

def my_function(*, x):
  print(x)
my_function(x = 3)
#3

--Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments--

def name(x):
    print(x)
name(3)
#3

--But when adding the *, / you will get an error if you try to send a positional argument:
def my_function(*, x):
  print(x)
my_function(3)
#TypeError: my_function() takes 0 positional arguments but 1 was given

15.Combine Positional-Only and Keyword-Only

"You can combine the two argument types in the same function."

"Any argument before the / , are positional-only, and any argument after the *, are keyword-only"

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
#26

16.Recursion
"""
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself.
This has the benefit of meaning that you can loop through data to reach a result."""

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Recursion Example Results
# 1
# 3
# 6
# 10
# 15
# 21