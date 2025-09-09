Python has two built-in methods that you can use on tuples.

Method	Description

1.count()	Returns the number of times a specified value occurs in a tuple

a = ("apple", "banana", "cherry")
b = a.count("apple")
print(f"apple is these many time : {b}")
#apple is these many time : 1

index()	Searches the tuple for a specified value and returns the position of where it was found
a = ("apple", "banana", "cherry")
b = a.index("banana")
print(f"apple is these many time : {b}")
#apple is these many time : 1