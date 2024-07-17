import math

with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')
print(lines)
board = [[0 for x in range(8)] for y in range(8)]
chunks = [lines[i:i+49] for i in range(0, len(lines), 49)]
moves = [[int(digit) for digit in chunk] for chunk in chunks]
move = 1
turn = 1
p1_wins = 0
p2_wins = 0
p3_wins = 0
# for row in moves:
#     print(row)
def check_win_conditions(board):
    # Check horizontal win conditions
    for row in board:
        for i in range(5):
            if row[i:i+4] == [1,1,1,1]:
                return 1
            elif row[i:i+4] == [2,2,2,2]:
                return 2
            elif row[i:i+4] == [3,3,3,3]:
                return 3

    # Check vertical win conditions
    for col in range(8):
        for i in range(5):
            if board[i][col] == 1 and board[i+1][col] == 1 and board[i+2][col] == 1 and board[i+3][col] == 1:
                return 1
            elif board[i][col] == 2 and board[i+1][col] == 2 and board[i+2][col] == 2 and board[i+3][col] == 2:
                return 2
            elif board[i][col] == 3 and board[i+1][col] == 3 and board[i+2][col] == 3 and board[i+3][col] == 3:
                return 3

    # Check diagonal win conditions (top left to bottom right)
    for row in range(5):
        for col in range(4):
            if board[row][col] == 1 and board[row+1][col+1] == 1 and board[row+2][col+2] == 1 and board[row+3][col+3] == 1:
                return 1
            elif board[row][col] == 2 and board[row+1][col+1] == 2 and board[row+2][col+2] == 2 and board[row+3][col+3] == 2:
                return 2
            elif board[row][col] == 3 and board[row+1][col+1] == 3 and board[row+2][col+2] == 3 and board[row+3][col+3] == 3:
                return 3
    # Check diagonal win conditions (top right to bottom left)
    for row in range(5):
        for col in range(3, 8):
            if board[row][col] == 1 and board[row+1][col-1] == 1 and board[row+2][col-2] == 1 and board[row+3][col-3] == 1:
                return 1
            elif board[row][col] == 2 and board[row+1][col-1] == 2 and board[row+2][col-2] == 2 and board[row+3][col-3] == 2:
                return 2
            elif board[row][col] == 3 and board[row+1][col-1] == 3 and board[row+2][col-2] == 3 and board[row+3][col-3] == 3:
                return 3
    return 0  # No win condition found

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
    
    for col in range(row*50,49+(row*50)):
        if check_win_conditions(board)==0:
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
        else:
            # print("player", check_win_conditions(board),"wins")
            if check_win_conditions(board) == 1:
                p1_wins+=1
            elif check_win_conditions(board) == 2:
                p2_wins+=1
            elif check_win_conditions(board) == 3:
                p3_wins+=1
            break
    # for rows in board:
    #     print(rows)
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 0

print(p1_wins*p2_wins*p3_wins)