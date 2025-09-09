Sorting the list

1.Aplhabetically sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#['banana', 'kiwi', 'mango', 'orange', 'pineapple']

2.Numeric sorting

a = [20, 30, 10, 15,100]
a.sort()
print(a)
#[10, 15, 20, 30, 100]

3.sort descending -   big to small
using => reverse = True inside sort

a = [20, 30, 10, 15,100]
a.sort(reverse=True)
print(a)
#[100, 30, 20, 15, 10]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
#['pineapple', 'orange', 'mango', 'kiwi', 'banana']

4.sort ascending - small to big

a = [20, 30, 10, 15,100]
a.sort(reverse=False)
print(a)
#[10, 15, 20, 30, 100]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=False)
print(thislist)
#['banana', 'kiwi', 'mango', 'orange', 'pineapple']

5.Customize Sort Function

customise the soritng by using function

QN:Sort the list based on how close the number is to 50:
def funct(n):
    return abs(n - 50)          #,n values will be taken from the thislist list and it will do diff with 50
                                        # and c which value is near to 50 according to the difference output it will sort the values
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=funct)
print(thislist)
#[50, 65, 23, 82, 100]

6.Case Insensitive Sort
Prints the capital letter containing values 1st and then small letter values in the list

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# ['Kiwi', 'Orange', 'banana', 'cherry']


#Prints the small letter containing values 1st and then  capital values in the list
key=str.lower

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

6,reversing
irrespective of the aplahabet order in list ,it will just reverse the list and print

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#['cherry', 'Kiwi', 'Orange', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.reverse()
print(thislist)
#[23, 82, 65, 50, 100]