with open("connect 4 input.txt", "r") as file:
    lines = file.read().split()
for line in lines:
    long_number = line

    # Convert the number to a string
    number_str = str(long_number)

    # Use a list comprehension to split the string into 3 substrings of length 1
    digit_list = [int(number_str[i:i+1]) for i in range(0, len(number_str))]

    # Print the list of digits
    print(digit_list)