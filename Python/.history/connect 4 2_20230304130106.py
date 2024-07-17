with open("connect 4 input.txt", "r") as file:
    lines = file.readlines()
lst = [list(map(int, line.strip().split())) for line in lines]
digits = list(str(lst))
print(digits[10])
board = [[' ' for col in range(7)] for row in range(7)]
player = 1
for row in range(1000):
    for col in range(49):
        pass
