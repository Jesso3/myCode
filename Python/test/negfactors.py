def find_factor_pairs(number):
    factor_pairs = []

    # Check factors from -number to +number
    for i in range(-abs(number), abs(number) + 1):
        if i != 0 and number % i == 0:
            factor_pairs.append((i, number // i))

    return factor_pairs

# Test the function
num = int(input("Enter a number: "))
pairs = find_factor_pairs(num)

print("Factor pairs of", num, "are:")
for pair in pairs:
    print(pair)
