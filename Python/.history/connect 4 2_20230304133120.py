with open("connect 4 input.txt", "r") as file:
    lines = file.read().split()
lst = [list(map(int, line.strip().split())) for line in lines]
moves = [list(str(lines))]
games = [[' ' for col in range(49)] for row in range(1000)]
number_str = str(moves)
p1_moves = []
p2_moves = []
p3_moves = []
for line in lines:
    l=[list(str(lines))]
print(games)   
board = [[' ' for col in range(7)] for row in range(7)]
