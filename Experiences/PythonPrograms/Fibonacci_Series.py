# A series of numbers in which each number is sum of two preceding numbers.
# It's first two numbers are fixed i.e. 0,1
# 0,1,1,2,3,5,8,13,21,44 etc...

N1 = 0
N2 = 1

print(N1)
print(N2)

for i in range(2,10): # start with 2 bcz first two numbers are fixed & end should be equal to how many numbers I want to print 10 means 10
    sum = N1 + N2
    print(sum)
    N1 = N2
    N2 = sum