index = 0

import math
def prime(num):
    factors = []
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(math.ceil(math.sqrt(num)),1,-1):
            if num % i == 0:
                return False
    return True
    
i = 2    
while(True):
    if prime(i)==True:
        index+=1
        if index == 10001:
            print(i)
            break
    i+=1

