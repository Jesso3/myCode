with open("connect 4 input.txt", "r") as file:
    lines = file.read().split()
digits = [int(char) for char in str(lines)]
moves = [[0 for j in range(49)]for i in range(1000)]
print(digits)
for row in range (1000):
    for col in range(49):
        pass