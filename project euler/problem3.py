import math
def prime(num):
    factors = []
    if num < 2:
        return False
    else:
        for i in range(math.ceil(math.sqrt(num)),2,-1):
            if num % i == 0:
                factors.append(i)
    if len(factors) == 0:            
        return True
    else:
        return factors

primes = prime(600851475143)
for i in primes:
    if prime(i) == True:
        print(i)
        break