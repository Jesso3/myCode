import math

with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')

board = [[0 for x in range(8)] for y in range(8)]
chunks = [lines[i:i+49] for i in range(0, len(lines), 49)]
moves = [[int(digit) for digit in chunk] for chunk in chunks]
move = 1
#print(board)
def testRow(col):
    if board[6][col]==0:
        return 6
    if board[5][col]==0:
        return 5
    if board[4][col]==0:
        return 4
    if board[3][col]==0:
        return 3
    if board[2][col]==0:
        return 2
    if board[1][col]==0:
        return 1
    if board[0][col]==0:
        return 0
for row in range(1):
    

    for col in range(49):
        if move % 3 == 0:
            board[testRow(int(lines[col]))][int(lines[col])]=3
        elif move % 2 == 0:
            board[testRow(int(lines[col]))][int(lines[col])]=2
        else:
            board[testRow(int(lines[col]))][int(lines[col])]=1
        move+=1

for row in board:
    print(row)