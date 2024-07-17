import math

with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')

board = [[0 for x in range(8)] for y in range(8)]
chunks = [lines[i:i+49] for i in range(0, len(lines), 49)]
moves = [[int(digit) for digit in chunk] for chunk in chunks]
move = 1
turn = 1
# for row in moves:
#     print(row)

def testRow(col):
    if board[7][col]==0:
        return 7
    elif board[6][col]==0:
        return 6
    elif board[5][col]==0:
        return 5
    elif board[4][col]==0:
        return 4
    elif board[3][col]==0:
        return 3
    elif board[2][col]==0:
        return 2
    elif board[1][col]==0:
        return 1
    
for row in range(10):

    for col in range(0+(row*49),49+49*row):
        if turn==1:
            board[testRow(int(lines[col]))][int(lines[col])]=1
        elif turn==2:
            board[testRow(int(lines[col]))][int(lines[col])]=2
        elif turn == 3:
            board[testRow(int(lines[col]))][int(lines[col])]=3
        move+=1
        if turn!=3:
            turn+=1
        else:
            turn=1
        
for row in board:
    print(row)