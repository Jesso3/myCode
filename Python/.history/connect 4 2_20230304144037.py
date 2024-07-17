with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')
digits = list(str(lines))

print(digits[5])