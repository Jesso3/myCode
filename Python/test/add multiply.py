def find_numbers(target_sum, target_product):
    for num1 in range(-100, 101):
        for num2 in range(-100, 101):
            if num1 + num2 == target_sum and num1 * num2 == target_product:
                return num1, num2
    return None

# Test the function
input_sum = int(input("Enter the target sum: "))
input_product = int(input("Enter the target product: "))

result = find_numbers(input_sum, input_product)
if result:
    print(f"The two numbers are: {result[0]} and {result[1]}")
else:
    print("No such numbers found.")
