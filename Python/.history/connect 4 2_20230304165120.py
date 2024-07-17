import math

with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')

board = [[0 for x in range(8)] for y in range(8)]
chunks = [lines[i:i+49] for i in range(0, len(lines), 49)]
moves = [[int(digit) for digit in chunk] for chunk in chunks]
move = 1
p1 = 1
p2 = 0 
p3 = 0
# for row in moves:
#     print(row)
def nextPlayer():
    if p1 == 1:
        p1=0
        p2=1
    if p2 == 1:
        p2=0
        p3=1
    if p3 == 1:
        p3=0
        p1=1
def checkPlayer():
    if p1==1:
        return p1
    if p2 ==1:
        return p2
    if p3 ==1:
        return p3
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
    
for row in range(1):

    for col in range(49):
        if checkPlayer() == p1:
            board[testRow(int(lines[col]))][int(lines[col])]=1
        elif checkPlayer() == p2:
            board[testRow(int(lines[col]))][int(lines[col])]=2
        elif checkPlayer() == p3:
            board[testRow(int(lines[col]))][int(lines[col])]=3
        move+=1
        if p1 == 1:
            p1=0
            p2=1
        if p2 == 1:
            p2=0
            p3=1
        if p3 == 1:
            p3=0
            p1=1
for row in board:
    print(row)