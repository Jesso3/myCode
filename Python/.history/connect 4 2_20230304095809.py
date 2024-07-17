with open("connect 4 input.txt", "r") as file:
    lines = file.readlines()
lst = [list(map(int, line.strip().split())) for line in lines]
board = [[None for col in range(7)] for row in range(7)]
print(lst)