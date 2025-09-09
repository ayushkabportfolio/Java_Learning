FUNCTIONS

'''A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.'''

1.Creating function
 using def keyword

def my_fucnt():
    print("hello")

2.calling a fucntion

def my_fucnt():
    print("hello")

my_fucnt()    #hello

3. Arguments
'''Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses.
 You can add as many arguments as you want, just separate them with a comma'''

def myfucnt(name):
    print(name + ' Gowda')

myfucnt("varshi")
myfucnt("qwerty")
#varshi Gowda
# qwerty Gowda

4. Parameters or Arguments?

'''The terms parameter and argument can be used for the same thing: information that are passed into a function.'''

'''From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.'''

5.Number  of arguments

'''By default, a function must be called with the correct number of arguments. 
Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, 
not more, and not less.'''

def name(name,lastname):
    print(name + ' is ' + lastname)

name('varshi', 'Gowda')
#varshi is Gowda

---wrngly argument passing--
def name(name,lastname):
    print(name + ' is ' + lastname)

name('varshi')
#TypeError: name() missing 1 required positional argument: 'lastname'

6.Arbitrary Arguments, *args

"""If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly"""

def name(*firstname):
    print("your name is" + ' ' + firstname[2])

name("varshi", "qwerty","qazwsx")
#your name is qazwsx

7.Keyword Arguments
"""
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter."""

def name(child1, child2, child3):
    print("my childe name is" + ' '+ child3)

name(child3="varshi" , child1="qwerty", child2 = "qazwsx")
#my childe name is varshi

8.Arbitrary Keyword Arguments, **kwargs
"""If you do not know how many keyword arguments that will be passed into your function, add two asterisk:
** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly
"""

def name(**child):
    print("my child name is" + ' '+ child["child1"])

name(child1="varshi", child2="qwerty")








