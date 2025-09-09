What is an Array?
An array is a special variable, which can hold more than one value at a time.

Arrays are used to store multiple values in one single variable:

ex:cars = ["Ford", "Volvo", "BMW"]

1.Access the Elements of an Array
"You refer to an array element by referring to the index number"

cars = ["Ford", "Volvo", "BMW"]
x =cars[0]
print(x)   #ford

2.Modify the values
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyoto"
print(cars)  #['Toyoto', 'Volvo', 'BMW']

3.The Length of an Array
"Use the len() method to return the length of an array (the number of elements in an array)"

cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)     #3

--Note: The length of an array is always one more than the highest array index.---

4.Looping Array Elements
"You can use the for in loop to loop through all the elements of an array"

cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)
# Ford
# Volvo
# BMW

5.Adding Array Elements
"You can use the append() method to add an element to an array."

cars = ["Ford", "Volvo", "BMW"]
cars.append("toyoto")
print(cars)
#['Ford', 'Volvo', 'BMW', 'toyoto']

6.Removing Array Elements
"You can use the pop() method to remove an element from the array."

cars = ["Ford", "Volvo", "BMW"]
cars.pop(2)
print(cars)
#['Ford', 'Volvo']

--remove() method to remove an element from the array.--

cars = ["Ford", "Volvo", "BMW"]
cars.remove("BMW")
print(cars)
#['Ford', 'Volvo']

--Note: The list's remove() method only removes the first occurrence of the specified value.

cars = ["Ford", "Volvo", "BMW", "BMW"]
cars.remove("BMW")
print(cars)
#['Ford', 'Volvo', 'BMW']

7.Array methods

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

7.