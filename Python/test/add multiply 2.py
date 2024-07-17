def find_factor_pairs(number):
    factor_pairs = []

    # Check factors from -number to +number
    for i in range(-abs(number), abs(number) + 1):
        if i != 0 and number % i == 0:
            factor_pairs.append((i, number // i))

    return factor_pairs

def find_numbers_with_sum(product, target_sum):
    factor_pairs = find_factor_pairs(product)

    for pair in factor_pairs:
        if pair[0] + pair[1] == target_sum:
            return pair

    return None

# Test the function
num = int(input("Enter a number: "))
sum_val = int(input("Enter the target sum: "))

result = find_numbers_with_sum(num, sum_val)

if result is not None:
    num1, num2 = result
    print("The numbers are:", num1, "and", num2)
    print("Their product is:", num1 * num2)
else:
    print("No pair of numbers found.")
