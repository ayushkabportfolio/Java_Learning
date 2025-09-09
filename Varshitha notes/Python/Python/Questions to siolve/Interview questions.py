"""1.swap first and last element of a list"""

a = [1,2,3,4,5]

a[0],a[-1]=a[-1],a[0]

print(a)       # [5, 2, 3, 4, 1]

""""2. swap 2 numbers"""

a = 1
b = 4
a,b= b,a
print(a,b)      #4 1

'''3.SUm of all elements in the array'''

a = [1,2,3,4,5]

#with loop

i = 0
for x  in a:
    i =i+x
print(i)        #15

#with sum function
print(sum(a))   #15

#with sum function adding 10 to the sum of the array
print(sum(a,10))        #25

'''4.print the list by keep on adding the elements'''
a = [1,2,3,4,5]
i = 0
for x in a:
    i =i+x
    print(i)        #1 3 6 10 15

'''5.length of the list and strings'''
# even space is counted in strings

#123456..
a = [1,2,3,4,5]
print(len(a))    #5

#01234567891011....
a = "hello,world "
print(len(a))       #12

'''6.star pattern'''

a = [1,2,3,4,5]

for x in a:
    print('*' * x)    #* ** *** **** *****

'''7. print the list in reverse order'''

a = [1,2,3,4,5]
print(a[::-1])      #[5, 4, 3, 2, 1]

'''8.reverse the string'''

a = 'helllo'
print(a[::-1])      #ollleh

'''9.Second largest number'''

a = [1,2,3,4,8,987,23,0]

a.sort()
print(a)    #[0, 1, 2, 3, 4, 8, 23, 987]
print(a[-2])        #23

'''10. remove duplicates from the list'''

a = [1,2,3,4,8,987,23,0,1,2,3,4,8,987,23,0]
print(list(set(a)))     #[0, 1, 2, 3, 4, 987, 8, 23]

'''11. check if the list is empty'''

a = []
if not a:
    print("list is empty")      #list is empty

'''12.reverse the words in string'''
a = "hi hello there"

b = a.split()
print(b)
c = b[::-1]
print(c)
d = ' '.join(c)
print(d)

13. '''reverse each word in the string'''
x = 'Hi there hello'
words = x.split(' ')
print(words)
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])
print(' '.join(reversed_words))

14.primenumber
x = [1,2,3,4,5,14,23,36,-9]
for num in x:
    count = 0
    if num > 1: # first condition
        for i in range(1,num+1):
            if num%i == 0:
                count = count+1
        if count ==2:
            print(num,"is a prime number")
        else :
            print(num,"is not prime number")

15.multiply the list
x = [1,2,3]
b=1
for a in x:
    b = a * b
print(b)

16.min and max element in array
x = [1,-3,23,999,0,1.29]

x.sort()
print(x)
print("min" ,x[0])
print('max',x[-1])

17.fibonacci series
N1 = 0
N2 = 1

print(N1)
print(N2)

for i in range(2,10): # start with 2 bcz first two numbers are fixed & end should be equal to how many numbers I want to print 10 means 10
    sum = N1 + N2
    print(sum)
    N1 = N2
    N2 = sum

18.count of the occurence of the elements in the list
x = ['A','B','C','A','A','C']

print(x.count(("A")))

19.count of the elements in the list
x = ['A','B','C','A','A','C']
print(len(x))

20.pallindrom
a= 'tenet'
b = a[::-1]
print(b)
if b == a:
    print("palindrome")
else:
    print("not a palindrome")

20.check special characters
x = 'Hi there^^* men'
special_characters = "!@#$%^&*()-+?_=,<>/"
special_found = False


for char in x:
    if char in special_characters:
        special_found = True
        break
if special_found == True:
    print("Yes")
else:
    print('No')