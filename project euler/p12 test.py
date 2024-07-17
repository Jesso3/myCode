def count_divisors(num):
    # Function to count the number of divisors
    divisors = 0
    i = 1
    while i <= num**0.5:
        if num % i == 0:
            if num // i == i:
                divisors += 1
            else:
                divisors += 2
        i += 1
    return divisors

def find_triangle_with_divisors(target_divisors):
    # Function to find the first triangle number with over a certain number of divisors
    n = 1
    triangle_num = 1

    while True:
        n += 1
        triangle_num += n

        # Check the number of divisors
        divisors = count_divisors(triangle_num)

        if divisors > target_divisors:
            return triangle_num

# Find the first triangle number with over 500 divisors
result = find_triangle_with_divisors(500)

print(f"The first triangle number with over 500 divisors is: {result}")
