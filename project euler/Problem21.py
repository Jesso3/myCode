import math
amicable_numbers = []
sums = [0]
for i in range(1,10001):
    sqrt = math.sqrt(i)
    divisors = [1]
    for j in range(2,math.ceil(sqrt)+1):
        if i/j % 1 == 0:
            divisors.append(j)
            divisors.append(int(i/j))
    sums.append(sum(divisors))
    if i == 2924:
        print(i,sum(divisors),sorted(divisors))
for i in range(len(sums)):
    if sums[i] < len(sums):
        if sums[sums[i]] == i and sums[i] != i:
            print(i,sums[i],sums[sums[i]])
            amicable_numbers.append(i)
print(sum(amicable_numbers))




