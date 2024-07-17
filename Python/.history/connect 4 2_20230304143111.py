with open("connect 4 input.txt", "r") as file:
    lines = file.read().split()

moves = [[0 for j in range(49)]for i in range(1000)]

for line in lines:
    digits = [int(char) for char in str(line)]
    print(digits[0][1])
for row in range (1000):
    for col in range(49):
        pass
