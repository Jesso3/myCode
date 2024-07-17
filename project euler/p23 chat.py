import math

def get_divisors_sum(n):
    divisors_sum = 1  # Start with 1 since all numbers are divisible by 1
    sqrt_n = math.isqrt(n) + 1
    for i in range(2, sqrt_n):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def is_abundant(n):
    return get_divisors_sum(n) > n

limit = 28123  # Given limit
abundant_numbers = [i for i in range(12, limit) if is_abundant(i)]

can_be_written = [False] * (limit + 1)

for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        abundant_sum = abundant_numbers[i] + abundant_numbers[j]
        if abundant_sum <= limit:
            can_be_written[abundant_sum] = True
        else:
            break

result = sum(i for i in range(limit + 1) if not can_be_written[i])

print(result)
