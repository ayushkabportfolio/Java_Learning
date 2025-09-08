# A prime number is one which has only two factors i.e 1 & itself i.e. which is only divisible by 1 & itself.
# All prime numbers are positive
# 1 is not a prime number, so all prime numbers are above 1

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
