import math

def abundant(n):
    divisors = [1]
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  
                divisors.append(n // i)
    return sum(divisors) > n

non_abundants = []
for i in range(1, 28123):
    is_sum_of_abundants = False
    for j in range(1, i//2 + 1): 
        if abundant(j) and abundant(i - j):
            is_sum_of_abundants = True
            break
    if not is_sum_of_abundants:
        non_abundants.append(i)

print(non_abundants)
print(sum(non_abundants))
