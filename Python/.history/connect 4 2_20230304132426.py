with open("connect 4 input.txt", "r") as file:
    lines = file.read().split()
lst = [list(map(int, line.strip().split())) for line in lines]
moves = [list(str(lines))]
games = [[moves[0][10] for col in range(49)] for row in range(1000)]
number_str = str(moves)
p1_moves = []
p2_moves = []
p3_moves = []

print(lines)
    
# board = [[' ' for col in range(7)] for row in range(7)]
# player = 1
# for row in range(1000):
#     for col in range(49):
#         if col % 3 == 0:
#            p3_moves.append()
