with open("connect 4 input.txt", "r") as file:
    lines = file.readlines()
lst = [list(map(int, line.strip().split())) for line in lines]
board = [[' ' for col in range(7)] for row in range(7)]
player = 1
for row in range(1000):
    digits = list(str(lst[row][0]))
    print(lst)
    for col in range(49):
        pass
