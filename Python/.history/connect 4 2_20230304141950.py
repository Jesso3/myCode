with open("connect 4 input.txt", "r") as file:
    lines = file.read().split()

for line in lines:
    string = str(line)
    print(string[2])