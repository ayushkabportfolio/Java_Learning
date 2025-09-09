---2D list---

List inside the list

matrics = [
    [1,2,3],
    [4,5,6]
]
print(matrics[0][2])        ##accessing the value inside the matrics
matrics[0][2] =8            #changing the value inside the matrics and printing new value
print(matrics[0][2])

---list methods----

1.pop() - removes last item
num = [5,6,7,8,1,3]
num.pop()
print(num)      #[5, 6, 7, 8, 1]

2.remove()
num = [5,6,7,8,1,3]
num.remove(8)
print(num)    #[5, 6, 7, 1, 3]

3.count()
num = [5,6,7,8,1,3]
print(num.count(6))

4.append()  --- add value at the end
num = [5,6,7,8,1,3]
num.append(10)
print(num)    #[5, 6, 7, 8, 1, 3, 10]

5.copy()
num = [5,6,7,8,1,3]
num2= num.copy()
print(num2)         #[5, 6, 7, 8, 1, 3]
num.append(10)
print(num)          #[5, 6, 7, 8, 1, 3, 10]

6.clear()
num = [5,6,7,8,1,3]
num.clear()

7.index
num = [5,6,7,8,1,3]
print(num.index(6))     #1

8.insert
num = [5,6,7,8,1,3]
num.insert(0,1)
print(num)      [1, 5, 6, 7, 8, 1, 3]

9.sort() --removes duplicate and print only one value  -- ascending
num = [5,6,7,8,1,3]
num.sort()
print(num)    #[1, 3, 5, 6, 7, 8]

10.reverse()  - just reverse the list
num = [5,6,7,8,1,3]
num.reverse()
print(num)     #[3, 1, 8, 7, 6, 5]

11.extend()  - extends the one list by attending 2nd list to the 1st list - duplicates allowed
num = [5,6,7,8,1,3]
num2 = [1,4,5,6]
num.extend(num2)
print(num)   #[5, 6, 7, 8, 1, 3, 1, 4, 5, 6]

12.HOw to reverse the list
num = [5,6,7,8,1,3]
num.sort()
num.reverse()
print(num)      #[8, 7, 6, 5, 3, 1]


13.qn - how to remove duplicates frm the list
num = [5,6,7,8,1,3,3,1,5]
unique=[]
for x in num:
    if x not in unique:
        unique.append(x)
print(unique)    #[5, 6, 7, 8, 1, 3]

----TUPLES----------
cant change ,modifu,insert,etc

only we can do count and index

1.count
num = (5,6,7,8,1,3,3,1,5)
print(num.count(1))      #2

2.index
num = (5,6,7,8,1,3,3,1,5)
print(num.index(1))         #4
print(num)

-------UNPACKING-----

coordinates = (1,2,3)  #tuple
x,y,z = coordinates
print(x,y,z) #1 2 3

coordinates = [1,2,3]   #list
x,y,z = coordinates
print(x,y,z) #1 2 3

-----Dictionaries---

customer = {
    "name" : "varshi",
    "age" : 25,
    "is_female" : True
}
print(customer["name"])

# add key-value pair
customer["DOB"] = "2000"
print(customer["DOB"])

#we can get the value frm 'get method'
print(customer.get("DOB"))

#if try to search for non existing value thru get method ,then NONE will be printed
print(customer.get("school"))

#if we try to provied one value along with non existing value,then get method will assume 2nd value as default and print tht
print(customer.get("school","varshitha"))

#if we pass dont pass any value inside the sq brackets ,then error will be printed
print(customer[])
#if we search for non existing value then error will  be printed
print(customer["school"])


Qn : Print one two three four when user provide 1234

Phn_num = input("phone.no:")
numbers = {
    "1" :"one",                         #keys should be string
    "2" : "Two",                       #TypeError: 'int' object is not iterable
    "3" : "Three",
    "4" : "Four"
}
output =""
for x in Phn_num:
    output += numbers.get(x, "!") + " "
print(output)

=====Palindrome==========

#check palindrom or not
word = int(1221)
my_str = str(word)
if word == int(my_str[::-1]):
    print("it is palindrom")
else:
    print("not")

#print reverse of the num

num =123
temp= num
rev =0
while num > 0:
    digit = num%10      ## Get the last digit
    rev = rev*10 + digit        ##Append the digit to the reversed number
    num=num//10             #removes the last digit frm the num
print(rev)

explination:
Input: 123
Processing:
digit = 3, rev = 0 * 10 + 3 = 3, num = 12
digit = 2, rev = 3 * 10 + 2 = 32, num = 1
digit = 1, rev = 32 * 10 + 1 = 321, num = 0
Output: 321
