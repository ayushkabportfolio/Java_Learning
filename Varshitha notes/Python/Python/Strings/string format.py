##Python Variables chapter, we cannot combine strings and numbers like this:

age = 36
txt = "My name is John, I am " + age
print(txt)              #TypeError: can only concatenate str (not "int") to str

## therefore to combine string and integer,we use string format
"""To specify a string as an f-string, simply put an 'f' in front of the string literal, and 'add curly brackets {}' as placeholders for variables and other operations."""

age = 36
word = f'my age is {age}'
print(word)

##Placeholders and Modifiers
"""A placeholder can contain variables, operations, functions, and modifiers to format the value.
---- inside the f'' ,what ever we are calling in {}- called as placeholder
---- A placeholder can include a modifier to format the value."""

x = "hello"
y = "world"
z = "you are the one"
a = f" {x} {y}"
print(z + a)        #you are the one hello world
print(z + f" {x} {y}")        #you are the one hello world
x = 25
y = 36
z = "you are the one"
a = f" {x} {y}"
print(z + a)        #you are the one 25 36

x = 25
y = 36
z = "you are the one"
a = f" {x} + {y}"
print(z + a)            #you are the one 25 + 36

'''A modifier is included by adding a 'colon :' 
----followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:'''

a = 35
b = f' im having {a:.2f}'
print(b)            # im having 35.00

"""A placeholder can contain Python code, like math operations:"""

a = 25
b = 30
z = f"{a} + {b}"
print(z)            #25 + 36

a = 25
b = 30
z = f"{a + b}"
y = f"{a * b}"
x = f"{a / b}"
print(z)            #55
print(y)            #750
print(x)            #0.8333333333333334
