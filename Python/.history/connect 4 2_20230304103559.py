with open("connect 4 input.txt", "r") as file:
    lines = file.readlines()
num_str = str(lines)

# Create an empty list to store the digits
digits_list = []

# Iterate over each character in the string and append it to the list
for char in num_str:
    digits_list.append(int(char))

# Print the list of digits
print(digits_list)