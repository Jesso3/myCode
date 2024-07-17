with open("connect 4 input.txt", "r") as file:
    lines = file.readlines()
numbers_str = lines
# Split the string into lines and create a 2D list of digits
digit_list = [[int(digit) for digit in line.strip()] for line in numbers_str.split('\n')]

# Print the resulting 2D list
print(numbers_str)