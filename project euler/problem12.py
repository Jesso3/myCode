import math

def triangular(n):
    return sum(i for i in range(n+1))

def divisors(n):
    num = 1
    for i in range(1,math.ceil(n/2)+1):
        if n % i == 0:
            num+=1
    return num

i = 0
while(True):
    if divisors(triangular(i)) >= 500:
        print(i)
        break
    i+=1
