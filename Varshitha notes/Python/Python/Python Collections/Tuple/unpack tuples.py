'''to extract the values back into variables. This is called "unpacking":'''

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry")
(green, yellow) = fruits

print(green)
print(yellow)
print(red)
#ValueError: too many values to unpack (expected 2)


Using Asterisk*

----Note: The number of variables must match the number of values in the tuple,
if not, you must use an asterisk to collect the remaining values as a list.from the end-----

fruits = ("apple", "banana", "cherry")
(green, *yellow) = fruits

print(green)
print(yellow)
# apple
# ['banana', 'cherry']


---If the number of variables is less than the number of values, you can add an * to the variable name
and the values will be assigned to the variable as a list from the end:---

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

---If the asterisk is added to another variable name than the last, Python will assign values to the variable until
the number of values left matches the number of variables left.------
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)
#apple
# ['banana', 'cherry', 'strawberry']
# raspberry